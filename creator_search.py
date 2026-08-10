"""Runnable creator-commerce retrieval example."""

from creator_documents import CreatorDocument, embed_text, select_document


def main() -> None:
    documents = [
        CreatorDocument("delivery-17", "Digital asset delivery", "Subscribers receive a signed download after purchase."),
        CreatorDocument("update-04", "Subscriber update", "The monthly studio update covers new tutorials and release notes."),
        CreatorDocument("processing-09", "Content processing", "New uploads are transcribed and indexed before publication."),
    ]
    query = "How do subscribers get the digital file after buying it?"
    embedded = [(document, embed_text(document.body)) for document in documents]
    selected = select_document(embed_text(query), embedded)
    print(f"query: {query}")
    print(f"selected: {selected.document_id} - {selected.title}")
    print(selected.body)


if __name__ == "__main__":
    main()

