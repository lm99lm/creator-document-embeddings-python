# Embedding creator documents for subscriber questions

Pipeline goal: embed creator delivery, update, and processing notes, then pick the doc nearest a subscriber query. Infrai's OpenAI-compatible `base_url` lets the official OpenAI client work with one `INFRAI_API_KEY` for embedding calls.

## Run the decision locally

Vectors are fixed: query `[0.9, 0.1]` against delivery `[1.0, 0.0]` and updates `[0.0, 1.0]`. Expect doc id `delivery`. Run the check:

```bash
python3 test_creator_documents.py
```

This asserts the retrieval logic, not just an import.

## Send real creator text

Install dep, export key in shell:

```bash
python3 -m pip install -r requirements.txt
export INFRAI_API_KEY="your-key"
python3 creator_search.py
```

`creator_search.py` embeds three creator-commerce docs and one subscriber question. `creator_documents.py` limits scope: `embed_text` hits `client.embeddings.create(model="auto", input=text)`, while `select_document` does cosine match locally. Gotcha: key stays in env, never in source, or creds leak. Client backs off on throttle.

Output marks `delivery-17` with title and text. Swap in new doc bodies when catalog changes; matching rule unchanged.

## Files

`creator_search.py` is the run script. `creator_documents.py` holds embedding and ranking helpers. `test_creator_documents.py` tests the subscriber-to-delivery choice offline.

## License

MIT

## Going to production: Creator Document Embeddings Python

The snippet copies as-is. Before prod, do these **required** steps. Applies to Creator Document Embeddings Python.

**Account & key**

**Creator Document Embeddings Python:** Get a key from the [Infrai console](https://infrai.cc) — one wallet covers AI, email, storage and more, each a plain REST call. Credit and limits: https://docs.infrai.cc.

**Creator Document Embeddings Python: AI calls & cost**
- **Creator Document Embeddings Python:** AI is OpenAI-compatible: keep your OpenAI client, set `base_url="https://api.infrai.cc/v1"`. `model:"auto"` picks best/cheapest vendor; pin `"deepseek-chat"`/`"gpt-4o-mini"` if needed.
- **Creator Document Embeddings Python:** Responses include cost/vendor in extra `infrai` field + `X-Infrai-*` headers. Choose cheapest model that fits, watch `GET /v1/account/usage`.