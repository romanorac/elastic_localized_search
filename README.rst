Localized search with ElasticSearch
===================================
ElasticSearch doesn’t offer Bulgarian, Czech, Estonian, French, Hungarian, Macedonian, Persian, Polish, Romanian, Russian, Slovak, Slovene, Serbian, Ukrainian lemmanizers out of the box.
There is a great plugin LemmaGen that solves this shortcoming. At the time of writting LemmaGen works with ElasticSearch 2.2.0 and older.

With elastic_localized_search we show a simple Python example, which connects to ElasticSearch server,
initializes index and mapping, adds documents in Slovenian language and executes a search.
We add documents with following titles: pes, psa, psi, pse, psovanje, pesem, pesmi,
where first 4 titles are about dogs and last 3 have the same first letters, but different meaning.
We show how to execute a search with a query pes (a dog) and retrieve only search results about dogs.

Install
-------
`Download elasticsearch <https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/2.2.0/elasticsearch-2.2.0.zip>`_.

Extract the zip and move the elasticsearch directory to some path.

Go to that path and install slovenian lemmatizer:

.. code-block:: bash

    ./bin/plugin install https://github.com/vhyza/elasticsearch-analysis-lemmagen/releases/download/v2.2.0/elasticsearch-analysis-lemmagen-2.2.0-plugin.zip

Run
---
Run ``bin/elasticsearch`` to start elasticsearch server. Run ``main.py`` to execute the search.

