import click

from dotenv import load_dotenv
from icecream import ic  # noqa: F401

from audio import transcribe_audio, translate_audio
from chat import start_chat
from image import generate_image
from utils import validate_options

load_dotenv()


@click.command()
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Makes the error messages verbose.",
)
@click.option(
    "-c",
    "--chat",
    is_flag=True,
    help="Start an interactive chat with the AI.",
)
@click.option(
    "-m",
    "--model",
    default="gpt-4",
    help="Model name to use for chat.",
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
    help=(
        "Generate a translated transcription from an audio file. "
        "Translates audio into English."
    ),
)
@click.option(
    "-i",
    "--image",
    type=str,
    help="Generate an image from a prompt.",
)
@click.option(
    "-n",
    "--number-of-images",
    default=1,
    type=int,
    help=(
        "Generate image(s) from a prompt. Specify the number of images to generate. "
        "(Default: 1)"
    ),
)
@click.option(
    "-f",
    "--image-folder",
    default="./images",
    help="Folder to save the generated images. (Default: ./images)",
)
@click.option(
    "-g",
    "--image-model",
    default="dall-e-3",
    help="Model name to use for image generation. (Default: dall-e-3)",
)
@click.option(
    "-s",
    "--image-size",
    default="1024x1024",
    help="Specify the size of the images to generate (default: 1024x1024).",
)
def main(
    verbose,
    chat,
    model,
    whisper,
    translate,
    image,
    number_of_images,
    image_folder,
    image_model,
    image_size,
):
    """
    A command-line tool for interacting with the OpenAI API.
    Supports chat, audio transcription, audio translation, and image generation.
    """

    validate_options(click.get_current_context())

    if chat:
        start_chat(model, verbose)
    elif whisper:
        transcribe_audio(whisper, verbose)
    elif translate:
        translate_audio(translate, verbose)
    elif image:
        generate_image(
            image_model, image, number_of_images, image_folder, image_size, verbose
        )
    else:
        click.echo(main.get_help(click.Context(main)))


if __name__ == "__main__":
    main()
