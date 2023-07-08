SHELL := /bin/bash

.PHONY: help chat transcribe translate image

.DEFAULT_GOAL := help

help:
	@echo "Please use 'make <target>' where <target> is one of the following:"
	@echo "  chat           Start an interactive chat with the AI."
	@echo "  transcribe     Generate a transcription from an audio file."
	@echo "  translate      Generate a translated transcription from an audio file."
	@echo "  image          Generate an image from a prompt."

chat:
	. venv/bin/activate && python main.py --chat

transcribe:
	. venv/bin/activate && python main.py --whisper $(audio_file)

translate:
	. venv/bin/activate && python main.py --translate $(audio_file)

image:
	. venv/bin/activate && python main.py --image "$(prompt)"
