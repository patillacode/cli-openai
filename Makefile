SHELL := /bin/bash

.PHONY: install

.DEFAULT_GOAL := help

install: python-install

python-install:
	python3 -m venv venv && \
	. venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt
