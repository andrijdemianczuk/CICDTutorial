install:
	pip install --upgrade pip && \
	pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py src/*.py lib/*.py tst/*.py
format:
	black *.py src/*.py lib/*.py tst/*.py
test:
	python -m pytest -vv --cov=src tst/*.py
deploy:
	#deploy
build:
	#build container
all: install lint test deploy