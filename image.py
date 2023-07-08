import openai

from rich.console import Console

from utils import display_output, download_images, handle_error


def generate_image(prompt, number_of_images, size, verbose=False):
    """
    Generate image(s) from a prompt.

    Args:
        prompt (str): The prompt for generating the image(s).
        number_of_images (int): The number of images to generate.
        size (str): The size of the generated image(s).
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    try:
        console = Console()
        with console.status("[bold green]Generating..."):
            images = openai.Image.create(
                prompt=prompt,
                n=number_of_images,
                size=size,
            )

        with console.status("[bold blue]Downloading..."):
            saved_images = download_images(images.data)

        display_output("\nImages saved to Downloads folder:", "yellow")
        for image in saved_images:
            display_output(f"- {image}", "cyan")

    except Exception as e:
        handle_error(e, verbose)
