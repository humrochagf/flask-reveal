# Makefile

######################################

PROJECT    := $(shell basename $(PWD))
PACKAGE    := "flask_reveal"
BUILD_TIME := $(shell date +%FT%T%z)

######################################

.PHONY: install
install: # system-wide standard python installation
	pip install .

.PHONY: install.hack
install.hack: # install development requirements
	pip install -r requirements.txt
	pip install -e .

.PHONY: lint
lint: # lint code
	pylint --load-plugins pylint_flask $(PACKAGE)

.PHONY: test
test: # run tests
	nosetests tests

.PHONY: cover
cover: # coverage tests
	nosetests -w tests --with-coverage --cover-package=flask_reveal

.PHONY: clean
clean: # remove temporary files and artifacts
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rmdir {} +
