# OpenAI API in Terminal

This is a Python 3 command line application that serves as an interface for the OpenAI API.

## Installation
```bash
$ git clone https://github.com/patillacode/cli-openai.git
$ cd cli-openai
$ make install
```

## CLI Usage
```bash
Usage: main.py [OPTIONS]

  A command-line tool for interacting with the OpenAI API. Supports chat,
  audio transcription, audio translation, and image generation.

Options:
  -v, --verbose                   Makes the error messages verbose.
  -c, --chat                      Start an interactive chat with the AI.
  -m, --model TEXT                Model name to use for chat.
  -w, --whisper PATH              Generate a transcription from an audio file.
  -t, --translate PATH            Generate a translated transcription from an
                                  audio file. Translates audio into English.
  -i, --image TEXT                Generate an image from a prompt.
  -n, --number-of-images INTEGER  Generate image(s) from a prompt. Specify the
                                  number of images to generate. (Default: 1)
  -f, --image-folder TEXT         Folder to save the generated images.
                                  (Default: ./images)
  -g, --image-model TEXT          Model name to use for image generation.
                                  (Default: dall-e-3)
  -s, --image-size TEXT           Specify the size of the images to generate
                                  (default: 1024x1024).
  --help                          Show this message and exit.
```

## Usage Examples
```bash
$ source venv/bin/activate
$ python main.py --chat --model gpt-3.5-turbo
# Enter your prompt and press enter
> please generate a haiku about poker
In smoky rooms, hearts,
Cards dance, fortunes ebbs and flows,
Poker faces know.
> ...
```

```bash
$ source venv/bin/activate
$ python main.py --whisper /path/to/audio/file.mp3
Below is the content of the given audio file in text form:
> Hello, how are you?
```

```bash
$ source venv/bin/activate
$ python main.py --translate /path/to/audio/file.mp3
Below is the translated content of the given audio file in text form:
> This is a sentence in German.
```

```bash
$ source venv/bin/activate
$ python main.py --image "A blue bottle in space"
> Here is your image: https://example.com/image.png
```

## .zshrc/.bashrc

If you want to use the CLI from anywhere in your terminal, you can add the following to your `.zshrc` or `.bashrc` file:
```bash
cli_openai() {
    start_folder=$(pwd)

    cd /path/to/your/projects/cli-openai
    . venv/bin/activate

    if [[ "$1" == "chat" ]]
    then
        python main.py --chat
    elif [[ "$1" == "transcribe" ]]
    then
        python main.py --whisper $2
    elif [[ "$1" == "translate" ]]
    then
        python main.py --translate $2
    elif [[ "$1" == "image" ]]
    then
        python main.py --image $2
    fi

    cd $start_folder
}
alias chat='cli_openai chat'
alias transcribe='cli_openai transcribe'
alias whisper='cli_openai transcribe'
alias translate='cli_openai translate'
alias dall-e='cli_openai image'
```

