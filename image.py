from dotenv import load_dotenv
from icecream import ic  # noqa: F401
from openai import OpenAI
from rich.console import Console

from utils import display_output, download_images, handle_error

load_dotenv()
client = OpenAI()


def generate_image(model, prompt, number_of_images, image_folder, size, verbose=False):
    """
    Generate image(s) from a prompt.

    Args:
        prompt (str): The prompt for generating the image(s).
        number_of_images (int): The number of images to generate.
        image_folder (str): Folder to save the generated images.
        size (str): The size of the generated image(s).
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    try:
        console = Console()
        with console.status("[bold green]Generating..."):
            images = client.images.generate(
                model=model,
                prompt=prompt,
                n=number_of_images,
                size=size,
            )

        with console.status("[bold blue]Downloading..."):
            saved_images = download_images(images.data, image_folder)

        display_output("\nImages saved:", "yellow")
        for image in saved_images:
            display_output(f"- {image}", "cyan")

    except Exception as err:
        handle_error(err, verbose)
