install:
	pip install --upgrade pip && \
	pip install -r requirements.txt
	python -m textblob.download_corpora
lint:
	pylint --disable=R,C *.py src/*.py lib/*.py tst/*.py
format:
	black *.py src/*.py lib/*.py tst/*.py
test:
	python -m pytest -vv --cov=src --cov=main tst/*.py
deploy:
	docker login -u ademianczuk -p ${{ secrets.DOCKER_PAT }}
	docker push ademianczuk/cicdtutorial:latest
run:
	docker run -p 127.0.0.1:8080:8080 6803f9b1b946
build:
	docker build -t ademianczuk/cicdtutorial .
all: install lint format test run build deploy
