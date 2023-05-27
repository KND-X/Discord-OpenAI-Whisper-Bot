# Discord OpenAI Whisper Bot

Discord Bot designed to use OpenAi Whisper functionality


## Installation

- Create discord app https://discord.com/developers/docs/getting-started#step-1-creating-an-app

- Enter Bot section in left sidebar and turn on Message Content Intent

- Click on OAuth2, then on URL Generator, tick bot and applications.commands scopes

- Below in bot permissions tick Send Messages and Read Message History

- Copy the link on bottom of the page, paste into web browser and the bot to a server

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