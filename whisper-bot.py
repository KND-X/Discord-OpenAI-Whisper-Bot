import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import whisper

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
model = whisper.load_model("small")

load_dotenv()
WHISPER_TOKEN = os.getenv('WHISPER_BOT_TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$whisper'):
        for attachment in message.attachments:
            if attachment.content_type.startswith("video") or attachment.content_type.startswith("audio"):
                await attachment.save(attachment.filename)
                transcribe = model.transcribe(attachment.filename)
                chunklength = 1994
                chunks = [transcribe["text"][i:i+chunklength ] for i in range(0, len(transcribe["text"]), chunklength )]
                for chunk in chunks:
                    embed = chunk
                    await message.reply('```'+embed+'```')
                os.remove(attachment.filename)
            else:
                await message.reply("You have send a file that is neither video nor audio")

    if message.content.startswith('$whisper help'):
        await message.reply("Usage: $whisper *audio/video file*")

@client.event
async def on_connect():
    print(f'{client.user} connected.')

client.run(WHISPER_TOKEN)