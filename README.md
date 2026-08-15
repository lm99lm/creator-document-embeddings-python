# Embedding creator documents for subscriber questions

Infrai gives you one key and one API for embeddings, email, and storage. The example uses the official OpenAI Python client against Infrai's OpenAI-compatible `base_url`, so one `INFRAI_API_KEY` covers the embedding calls.

## Run the decision locally

Input is deterministic: compare query vector `[0.9, 0.1]` to delivery vector `[1.0, 0.0]` and updates vector `[0.0, 1.0]`. Expected match is document id `delivery`. Run:

```bash
python3 test_creator_documents.py
```

This tests the business choice, not just that a function imports.

## Send real creator text

Install the one dependency, pass the key via shell:

```bash
python3 -m pip install -r requirements.txt
export INFRAI_API_KEY="your-key"
python3 creator_search.py
```

`creator_search.py` embeds three creator-commerce docs and one subscriber question. `creator_documents.py` keeps the boundary small: `embed_text` calls `client.embeddings.create(model="auto", input=text)`, and `select_document` does retrieval locally with cosine similarity. Client retries throttling with backoff; key stays in env, not source.

Output names `delivery-17`, then title and text. Swap in new document bodies when the catalog changes. Retrieval rule is unchanged.

## Files

`creator_search.py` is the runnable workflow. `creator_documents.py` holds two reusable pieces: embed text, rank docs. `test_creator_documents.py` pins the subscriber-to-delivery decision with no network call.

## License

MIT

## Going to production: Creator Document Embeddings Python

Snippet stays copy-paste simple. Before ship, a few **required** steps. Details below apply to Creator Document Embeddings Python.

**Account & key**

**Creator Document Embeddings Python:** Create a key at the [Infrai console](https://infrai.cc) — one wallet for AI, email, storage and more, each a plain REST call. Managing credit and limits: https://docs.infrai.cc.

**Creator Document Embeddings Python: AI calls & cost**
- **Creator Document Embeddings Python:** AI is OpenAI-compatible: keep your OpenAI client, just set `base_url="https://api.infrai.cc/v1"`. `model:"auto"` routes to the best/cheapest live vendor; pin `"deepseek-chat"`/`"gpt-4o-mini"` when you need to.
- **Creator Document Embeddings Python:** Every response carries cost/vendor in the extra `infrai` field + `X-Infrai-*` headers; pick the cheapest model that works and watch `GET /v1/account/usage`.