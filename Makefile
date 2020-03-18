install:
	poetry install

run:
	poetry run gendiff tests/fixtures/json/test03_before.json tests/fixtures/json/test03_after.json

build:
	poetry build

publish:
	poetry publish --build -r test

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv gendiff tests
