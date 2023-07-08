import shutil
import traceback
import uuid

import click
import requests


def download_images(images):
    """
    Download images from URLs.

    Args:
        images (list): List of dictionaries containing image information.

    Returns:
        list: List of downloaded image file paths.
    """
    images_files = []
    for image in images:
        response = requests.get(image["url"], stream=True)
        if response.status_code == 200:
            file_name = f"/Users/dvitto/Downloads/{uuid.uuid4()}.png"
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
        end (str, optional): The ending character for the output message. Defaults to "\n".
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
