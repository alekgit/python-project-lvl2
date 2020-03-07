install:
	poetry install

run:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --build -r test

lint:
	poetry run flake8 ./brain_games/
