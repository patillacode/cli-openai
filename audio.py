from dotenv import load_dotenv
from icecream import ic  # noqa: F401
from openai import OpenAI
from rich.console import Console

from utils import display_output, handle_error

load_dotenv()
client = OpenAI()


def transcribe_audio(audio_file, verbose=False):
    """
    Generate a transcription from an audio file.

    Args:
        audio_file (str): The path to the audio file.
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    try:
        console = Console()
        with console.status("[bold green]transcribing..."):
            transcript = client.audio.transcriptions.create(
                file=open(audio_file, "rb"),
                model="whisper-1",
                response_format="text",
            )
        display_output(
            "Below is the content of the given audio file in text form:\n", "yellow"
        )
        display_output(f"{transcript}\n")
    except Exception as e:
        handle_error(e, verbose)


def translate_audio(audio_file, verbose=False):
    """
    Generate a translated transcription from an audio file.

    Args:
        audio_file (str): The path to the audio file.
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    try:
        console = Console()
        with console.status("[bold green]translating..."):
            translation = client.audio.translations.create(
                file=open(audio_file, "rb"),
                model="whisper-1",
                response_format="text",
            )
        display_output(
            "Below is the translated content of the given audio file in text form:\n",
            "yellow",
        )
        display_output(f"{translation}\n")
    except Exception as e:
        handle_error(e, verbose)
