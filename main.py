from time import sleep

from controller_elastic import ControllerElastic
from models_elastic import Document

if __name__ == '__main__':
    # create connection with elastic search
    ce = ControllerElastic(hosts=["localhost"], index_name="example")

    # initialize index
    ce.initialize_index(delete_if_exists=True)

    # index documents
    other_titles = ["psovanje", "pesem", "pesmi"]
    dog_titles = ["pes", "psa", "psi", "pse"]
    document_titles = other_titles + dog_titles

    for document_title in document_titles:
        ce.index_document(document_title)

    sleep(1)  # wait that data gets indexed

    # search
    search_hits = ce.search(Document, "PES")
    for search_hit in search_hits:
        if search_hit["title"] in other_titles:
            raise Exception(search_hit["title"] + "should not be here")
    print "search hits: " + str(search_hits)
