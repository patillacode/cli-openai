import os

import click
import openai

from dotenv import load_dotenv

from audio import transcribe_audio, translate_audio
from chat import start_chat
from image import generate_image

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


@click.command()
@click.option("-h", "--help", is_flag=True, help="Prints the help message.")
@click.option("-v", "--verbose", is_flag=True, help="Makes the error messages verbose.")
@click.option("-c", "--chat", is_flag=True, help="Start an interactive chat with the AI.")
@click.option(
    "-m", "--model", default="gpt-3.5-turbo", help="Model name to use for chat."
)
@click.option(
    "-w",
    "--whisper",
    type=click.Path(exists=True),
    help="Generate a transcription from an audio file.",
)
@click.option(
    "-t",
    "--translate",
    type=click.Path(exists=True),
    help="Generate a translated transcription from an audio file.",
)
@click.option("-i", "--image", help="Generate an image from a prompt.")
@click.option(
    "--number_of_images",
    default=1,
    type=int,
    help="Generate image(s) from a prompt. Specify the number of images to generate.",
)
@click.option(
    "--size",
    default="1024x1024",
    help="Specify the size of the images to generate (default: 1024x1024).",
)
def main(help, verbose, chat, model, whisper, translate, image, number_of_images, size):
    """
    A command-line tool for interacting with the OpenAI API.
    Supports chat, audio transcription, audio translation, and image generation.

    Args:
        help (bool): Prints the help message.
        verbose (bool): Makes the error messages verbose.
        chat (bool): Start an interactive chat with the AI.
        model (str): Model name to use for chat.
        whisper (str): Generate a transcription from an audio file.
        translate (str): Generate a translated transcription from an audio file.
        image (str): Generate an image from a prompt.
        number_of_images (int): Specify the number of images to generate. (default: 1)
        size (str): Specify the size of the images to generate (default: 1024x1024).
    """
    if chat:
        start_chat(model, verbose)
    elif whisper:
        transcribe_audio(whisper, verbose)
    elif translate:
        translate_audio(translate, verbose)
    elif image:
        generate_image(image, number_of_images, size, verbose)
    else:
        click.echo(main.get_help(click.Context(main)))


if __name__ == "__main__":
    main()
