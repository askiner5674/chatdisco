import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, world!')

client.run('MTA3NTMwMTY1OTA5NTMzOTAzOA.GMc_Qm.BWJ9UHBAKS61PxMs9EZdALZb3y3R_JFkNwQon0')