# API Test Automation Suite

Requests/pytest contract suite covering policy CRUD, authorization failures, validation, missing resources, schema shape and pagination. Includes a local FastAPI target and a mutation runner proving five injected behavior changes are detected.

## Run

Install requirements.txt; `pytest -q`. The fixture starts a local target automatically. Set TARGET_URL and TEST_TOKEN for an equivalent API. `python mutations.py` runs baseline plus five isolated mutant servers and requires every mutant to fail.
