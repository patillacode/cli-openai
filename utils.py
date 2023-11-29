import shutil
import traceback
import uuid

import click
import requests

from icecream import ic  # noqa: F401


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


def split_message(message, max_line_length=90, min_line_length=60):
    lines = []
    current_line = ""

    words = message.split()

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += word + " "
        else:
            if len(current_line) >= min_line_length:
                lines.append(current_line.rstrip())
                current_line = word + " "
            else:
                lines.append(current_line.rstrip() + word + " ")
                current_line = ""

    if current_line:
        lines.append(current_line.rstrip())

    return lines
