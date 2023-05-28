# Discord OpenAI Whisper Bot

Discord Bot designed to use OpenAi Whisper functionality


## Installation

- Install python 3.9.9 and optionally git

- Download and install CUDA toolkit: https://developer.nvidia.com/cuda-11-8-0-download-archive

- Install pytorch for CUDA 11.8:

```bash
  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

- Download ffmpeg: https://ffmpeg.org/download.html, unpack it and add bin folder to the system path

- Create discord app https://discord.com/developers/docs/getting-started#step-1-creating-an-app

- Enter Bot section in left sidebar, turn on Message Content Intent, copy token and store it somewhere

- Click on OAuth2, then on URL Generator, tick bot and applications.commands scopes

- Below in bot permissions tick Send Messages and Read Message History

- Copy the link on bottom of the page, paste into web browser and add the bot to your server

- Git clone or download zip from this repository

- Install Depedancies:

```bash
  pip install -r requirements.txt
```

- Create .env file with following variable:

```bash
  WHISPER_BOT_TOKEN="your bot token"
```

- Run the bot with following command:

```bash
  python whisper-bot.py
```

- Send a message in a channel or dm the bot: $whisper *with attached audio/video file*