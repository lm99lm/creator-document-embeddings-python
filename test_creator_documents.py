from creator_documents import CreatorDocument, select_document


def test_subscriber_query_selects_delivery_document() -> None:
    documents = [
        (CreatorDocument("delivery", "Delivery", "A file arrives after payment."), [1.0, 0.0]),
        (CreatorDocument("updates", "Updates", "A monthly note lists new lessons."), [0.0, 1.0]),
    ]
    selected = select_document([0.9, 0.1], documents)
    assert selected.document_id == "delivery"

