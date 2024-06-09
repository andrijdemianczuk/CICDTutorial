install:
	pip install --upgrade pip && \
	pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py src/*.py lib/*.py tst/*.py
format:
	black *.py src/*.py lib/*.py tst/*.py
test:
	python -m pytest -vv --cov=src --cov=main tst/*.py
deploy:
	#deploy
build:
	python -m textblob.download_corpora
all: install lint format test deploy