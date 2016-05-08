Elasticsearch with custom lemmatizer
====================================
Elasticsearch doesn’t offer a lemmatizer for following languages out of the box:

* Bulgarian,
* Czech,
* Estonian,
* French,
* Hungarian,
* Macedonian,
* Persian,
* Polish,
* Romanian,
* Russian,
* Slovak,
* Slovene,
* Serbian,
* Ukrainian.

There is a great plugin `LemmaGen <https://github.com/vhyza/elasticsearch-analysis-lemmagen>`_ that solves this shortcoming.
At the time of writing LemmaGen works with ElasticSearch 2.2.0 and older.

We show a simple python example, which connects to Elasticsearch server,
initializes index and mapping, adds documents in Slovenian language and executes a search.
We add documents with following titles: pes, psa, psi, pse, psovanje, pesem, pesmi,
where first 4 titles are about dogs and last 3 have the same first letters, but different meaning.
We show how to execute a search with a query pes (a dog) and retrieve only search results about dogs.
Further reading: `Efficient search in your local language <https://www.linkedin.com/pulse/efficient-search-your-local-language-roman-orač>`_


Install
-------
#. `Download elasticsearch <https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/2.2.0/elasticsearch-2.2.0.zip>`_, extract the zip and move the elasticsearch directory to some path.
#. Go to that path and install Lemmagen plugin: ``./bin/plugin install https://github.com/vhyza/elasticsearch-analysis-lemmagen/releases/download/v2.2.0/elasticsearch-analysis-lemmagen-2.2.0-plugin.zip``
#. Download this project and install requirements with: ``pip install -r requirements.txt``

Run
---
Run ``bin/elasticsearch`` to start elasticsearch server. Run ``python main.py`` to execute the search.
