import discord
from dotenv import load_dotenv
import os
import sarcasmCommands

load_dotenv()
client = discord.Client()
sarcasm_command = sarcasmCommands.SarcasmCommands()
sarcasm_command.train_bernoulli_model()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.channel.name != 'bot-testing':
        return

    await sarcasm_command.check_model_prediction(message)


client.run(os.environ['DISCORD_TOKEN'])
