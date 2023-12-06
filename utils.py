import shutil
import traceback
import uuid

import click
import requests

from icecream import ic  # noqa: F401


def validate_options(ctx):
    """
    Validate the given options.

    Args:
        ctx (click.Context): The click context object.

    Raises:
        click.UsageError: If more than one service is used at the same time.
    """
    options = [
        bool(option)
        for option in [
            ctx.params.get("chat", None),
            ctx.params.get("whisper", None),
            ctx.params.get("translate", None),
            ctx.params.get("image", None),
        ]
    ]
    if sum(options) > 1:
        raise click.UsageError(
            "You can't use more than one service at the same time.\n"
            "Please choose one of the following: "
            "-c (chat), -w (whisper), -t (translate) or -i (image).\n"
            "For more information, run with the --help option.\n"
        )


def clean_path(path):
    """
    Clean the given path.

    Args:
        path (str): The path to clean.

    Returns:
        str: The cleaned path.
    """
    if path.endswith("/"):
        path = path[:-1]

    return path


def download_images(images, image_folder):
    """
    Download images from URLs.

    Args:
        images (list): List of dictionaries containing image information.
        image_folder (str): Folder to save the downloaded images.

    Returns:
        list: List of downloaded image file paths.
    """
    images_files = []
    for image in images:
        response = requests.get(image.url, stream=True)
        if response.status_code == 200:
            file_name = f"{clean_path(image_folder)}/{uuid.uuid4()}.png"
            with open(file_name, "wb") as f:
                shutil.copyfileobj(response.raw, f)
            images_files.append(file_name)

        else:
            display_output("Error downloading: ", color="red", end="")
            display_output(image["url"], color="cyan", end="")

    return images_files


def display_output(output, color="green", end="\n"):
    """
    Display output message in color.

    Args:
        output (str): The output message to display.
        color (str, optional): The color of the output message. Defaults to "green".
        end (str, optional): The ending character for the output message.
                             Defaults to "\n".
    """
    click.echo(click.style(output, fg=color), nl=end == "\n")


def handle_error(exception, verbose=False):
    """
    Handle and display API errors.

    Args:
        exception (Exception): The exception object.
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    display_output(f"Error: {str(exception)}", "red")
    if verbose:
        display_output(traceback.format_exc(), "cyan")
