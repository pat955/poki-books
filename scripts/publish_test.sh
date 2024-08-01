python update_version.py
poetry install -v
poetry build -v
semantic-release version --print
poetry run semantic-release publish
