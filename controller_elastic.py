import json

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index
from elasticsearch_dsl import Q
from elasticsearch_dsl import Search
from models_elastic import Document
from elasticsearch_dsl.document import DocTypeMeta


class ControllerElastic:
    def __init__(self, hosts, index_name):
        """
        initialize elastic controller

        :param hosts: list of hostnames, eg. ["localhost"]
        :param index_name: index name in elasticsearch
        """
        self.client = Elasticsearch(hosts=hosts)
        self.index_name = index_name

    def initialize_index(self, delete_if_exists=False):
        """
        Initialize index with mapping in ElasticSearch

        :param delete_if_exists: delete index, if exists
        :return: None
        """

        def update_index_settings():
            """
            Function updates settings for slovenian lemmatization of words.
            As far as we know, elasticsearch-dsl library does not support
            custom filter settings.

            :return: None
            """
            analysis_settings = {
                "analysis": {
                    "filter": {
                        "lemmagen_filter_sl": {
                            "type": "lemmagen",
                            "lexicon": "sl"
                        }
                    },
                    "analyzer": {
                        "lemmagen_sl": {
                            "type": "custom",
                            "tokenizer": "uax_url_email",
                            "filter": [
                                "lemmagen_filter_sl",
                                "lowercase"
                            ]
                        }
                    }
                }
            }
            self.client.cluster.health(index=self.index_name,
                                       wait_for_status='green',
                                       request_timeout=2)
            self.client.indices.close(index=self.index_name)
            self.client.indices.put_settings(json.dumps(analysis_settings),
                                             index=self.index_name)
            self.client.indices.open(index=self.index_name)

        index = Index(self.index_name, using=self.client)
        if delete_if_exists and index.exists():
            index.delete()

        index.settings(
            # use higher number in production
            number_of_replicas=0
        )

        # register models
        index.doc_type(Document)
        index.create()
        update_index_settings()  # set lemmanizer

    def index_document(self, title):
        """
        Save document to elastic search

        :param title: document's title
        :return: True, if saved successfully
        """
        if title:
            document = Document(title=title.lower())
            document.save(using=self.client)
            return True
        return False

    def search(self, doc_type, query=""):
        """
        Execute search query and retrive results

        :param doc_type: Type in ElasticSearch
        :param query: search query
        :return: list with results
        """
        results = []
        if type(query) in [str, unicode] and type(doc_type) == DocTypeMeta:
            q = Q("multi_match",
                  query=query.lower(),
                  fields=["title"])

            s = Search()
            s = s.using(self.client)
            s = s.index(self.index_name)
            s = s.doc_type(doc_type)
            s = s.query(q)
            print "search query: " + str(s.to_dict())

            response = s.execute()

            for resp in response:
                results.append(resp)
        return results
