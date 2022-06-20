import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel)

    if message.author == client.user:
        return
    elif message.channel.name != 'bot-testing':
        return

    await message.channel.send(f'{message.author.mention} you are messaging in this channel: {channel}')


client.run(os.environ['DISCORD_TOKEN'])
