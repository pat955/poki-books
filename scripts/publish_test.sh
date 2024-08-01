python update_version.py
poetry install -v
poetry build -vvv
poetry run semantic-release publish
