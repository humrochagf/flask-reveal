# Makefile

######################################

PROJECT    := $(shell basename $(PWD))
PACKAGE    := "flask_reveal"
BUILD_TIME := $(shell date +%FT%T%z)

######################################

.PHONY: install
install: # system-wide standard python installation
	python setup.py install

.PHONY: install.hack
install.hack: # install development requirements
	pip install -r requirements.txt

.PHONY: lint
lint: # lint code
	pylint --load-plugins pylint_flask $(PACKAGE)

.PHONY: test
test: # run tests
	python setup.py test

.PHONY: cover
cover: # coverage tests
	coverage run --source=. setup.py test && coverage report -m

.PHONY: clean
clean: # remove temporary files and artifacts
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rmdir {} +
