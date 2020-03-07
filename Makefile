install:
	poetry install

run:
	poetry run gendiff tests/fixtures/before.json tests/fixtures/after.json -f plain

build:
	poetry build

publish:
	poetry publish --build -r test

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv gendiff tests
