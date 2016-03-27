from elasticsearch_dsl.document import DocType
from elasticsearch_dsl import analyzer, String

# slovenian lemmanizer
lemmagen_sl = analyzer('lemmagen_sl', type='custom',
                       tokenizer="uax_url_email",
                       filter=["lowercase"],
                       )


class Document(DocType):
    """
    The :class:`Document` class defines a Type in ElasticSearch
    """
    title = String(analyzer=lemmagen_sl)
