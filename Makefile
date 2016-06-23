# Makefile

######################################

PROJECT    := $(shell basename $(PWD))
PACKAGE    := "flask_reveal"
BUILD_TIME := $(shell date +%FT%T%z)

######################################

.PHONY: install
install: ## system-wide standard python installation
	python setup.py install

.PHONY: install.hack
install.hack: ## install development requirements
	pip install -r requirements.txt

.PHONY: lint
lint: ## lint code and tests
	pylint --reports no $(PACKAGE) tests/

.PHONY: clean
clean: ## remove temporary files and artifacts
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
