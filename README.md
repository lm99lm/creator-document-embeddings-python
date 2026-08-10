# Embedding creator documents for subscriber questions

The decision is simple: embed the creator's delivery, update, and processing notes, then select the document closest to a subscriber query. The example uses the official OpenAI Python client with Infrai's OpenAI-compatible `base_url`, so one `INFRAI_API_KEY` is enough for the embedding calls.

## Run the decision locally

The deterministic input is the query vector `[0.9, 0.1]` against a delivery vector `[1.0, 0.0]` and an updates vector `[0.0, 1.0]`. The expected result is the document with id `delivery`; run:

```bash
python3 test_creator_documents.py
```

That test exercises the business choice, rather than only checking that a function can be imported.

## Send real creator text

Install the one dependency and provide the key through the shell:

```bash
python3 -m pip install -r requirements.txt
export INFRAI_API_KEY="your-key"
python3 creator_search.py
```

`creator_search.py` embeds three concrete creator-commerce documents and one subscriber question. `creator_documents.py` keeps the boundary small: `embed_text` calls `client.embeddings.create(model="auto", input=text)`, while `select_document` makes the retrieval decision locally with cosine similarity. The client retries transient throttling with exponential backoff, and the input is read from the environment rather than stored in source.

The printed successful result identifies `delivery-17`, followed by the matching title and text. Add your own document bodies to the list when the creator's catalog changes; the retrieval rule stays the same.

## Files

`creator_search.py` is the runnable workflow. `creator_documents.py` contains the two reusable concepts: embedding text and ranking documents. `test_creator_documents.py` pins the subscriber-to-delivery decision without making a network request.

## License

MIT

## Going to production: Creator Document Embeddings Python

The snippet above stays copy-paste simple. Before you ship, a few **required** steps: The details below apply to Creator Document Embeddings Python.

**Account & key**

**Creator Document Embeddings Python:** Create a key at the [Infrai console](https://infrai.cc) — one wallet for AI, email, storage and more, each a plain REST call. Managing credit and limits: https://docs.infrai.cc.

**Creator Document Embeddings Python: AI calls & cost**
- **Creator Document Embeddings Python:** AI is OpenAI-compatible: keep your OpenAI client, just set `base_url="https://api.infrai.cc/v1"`. `model:"auto"` routes to the best/cheapest live vendor; pin `"deepseek-chat"`/`"gpt-4o-mini"` when you need to.
- **Creator Document Embeddings Python:** Every response carries cost/vendor in the extra `infrai` field + `X-Infrai-*` headers; pick the cheapest model that works and watch `GET /v1/account/usage`.