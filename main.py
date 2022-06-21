import discord
import os

import sarcasmCommands

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

    sarcasm_command.check_model_prediction(message)


# client.run(os.environ['DISCORD_TOKEN'])
client.run('OTg4Mjg5MjY5Mjk2NjYwNTQw.GWnWvU.PzuEv_MeQGatXqFrtBCLwb5JARMuFRes6qOjNc')
