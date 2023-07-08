# OpenAI API in Terminal

This is a Python 3 command line application that serves as an interface for the OpenAI API.

## Installation
```bash
$ git clone
$ cd cli-openai
$ make install
```

## CLI Options
* `--help`: Prints the help message with examples of how to use the CLI.
* `--chat`: Starts an interactive chat with the AI.
* `--image`: Takes in a prompt and generates an image.
* `--whisper`: Takes in an audio file and generates a transcription.
* `--translate`: Takes in an audio file and generates a translated transcription.

## Usage Examples
```bash
$ python main.py --chat --model gpt-3.5-turbo
# Enter your prompt and press enter
> please generate a haiku about poker
In smoky rooms, hearts,
Cards dance, fortunes ebbs and flows,
Poker faces know.
> ...
```

```bash
$ python main.py --whisper /path/to/audio/file.mp3
Below is the content of the given audio file in text form:
> Hello, how are you?
```

```bash
$ python main.py --translate /path/to/audio/file.mp3
Below is the translated content of the given audio file in text form:
> This is a sentence in German.
```

```bash
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

