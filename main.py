import random, os, discord
#from anekos import NekosLifeClient, SFWImageTags
from discord import app_commands
from discord.ext import commands

with open(f"./token.txt", "r") as f:
    TOKEN = f.read()


#nekoClient = NekosLifeClient()

prefix = '='

client = commands.Bot(command_prefix='=', intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Fuck me this is gonna take a lot of updating")
    # result = await nekoClient.image(SFWImageTags.NEKO)
    # print(result.url)
    # print("Logged in as {0.user}".format(client))
    # await client.change_presence(status=discord.Status('online'),
    #                              activity=discord.Game(name="Time to conquer the heavens", url="technoblade.com"))
    # await client.get_channel(987005532214804510).send(result.url)
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name="yo")
async def yo(interaction: discord.Interaction):
    await interaction.response.send_message(f"Yo {interaction.user.mention}", ephemeral=True)

@client.tree.command(name="boomer")
async def boomer(interaction: discord.Interaction):
    file = random.choice(os.listdir("./Boomer/"))
    await interaction.response.send_message(file=discord.File("./Boomer/" + file))

@client.tree.command(name="pump")
async def pumps(interaction: discord.Interaction):
    file = random.choice(os.listdir("./Pumps/"))
    await interaction.response.send_message(file=discord.File("./Pumps/" + file))
# @client.event
# async def on_message(message):
#     neko = NekosLifeClient()
#
#     if message.author == client.user:
#         return
#
#     username = str(message.author).split('#')[0]
#     user_id = str(message.author.id)
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#
#     if message.guild.name != "Valoobant":
#         print(f'({message.guild.name}) {username}: {user_message} ({channel})')
#         with open(f"./Cant-logs.txt", "a+") as f:
#             f.write(f"({message.guild.name}) {username}: {user_message} ({channel})\n")
#
#     if message.channel.name != (
#             "boomer-submission-channel" and "pumps-submission-channel" and "dingy-submission-channel"):
#         if 'boomer' in user_message.lower():
#             file = random.choice(os.listdir("./Boomer/"))
#             print(file)
#             await message.channel.send(file=discord.File("./Boomer/" + file))
#         if 'pumps' in user_message.lower():
#             file = random.choice(os.listdir("./Pumps/"))
#             print(file)
#             await message.channel.send(file=discord.File("./Pumps/" + file))
#
#     if message.guild.name != "Valboont":
#         if user_message.lower() == prefix + 'love':
#             await message.channel.send(f'I love you <@{user_id}>')
#             return
#         if user_message.lower() == prefix + 'tom':
#             await message.channel.send(f'Tom is hot')
#             return
#         if user_message.lower() == "i love dingy bot":
#             await message.channel.send(f'I love you too <@{user_id}>!')
#             return
#         if '<@986711862861242448>' in user_message.lower():
#             for x in range(5):
#                 await message.channel.send(f'Stop pinging me <@{user_id}>!')
#             return
#         if user_message.lower() == prefix + "neko":
#             result = await neko.image(SFWImageTags.NEKO)# nsfwLewd, Gasm, spank(gif),
#             await message.channel.send(result.url)
#             return
#         if user_message.lower() == prefix + "kitsune":
#             result = await neko.image(SFWImageTags.FOX_GIRL)# nsfwLewd, Gasm, spank(gif),
#             await message.channel.send(result.url)
#             return
#         if user_message.lower() == prefix + "prussia":
#             for x in range(5):
#                 await message.channel.send(f'https://tenor.com/view/chad-giga-gigachad-prussia-gif-24245950')
#             return
#
#
#     elif user_message.startswith(prefix) and message.channel.name != "idea-submissions":
#         await message.channel.send(f"I don't work in here :angry:")


client.run(TOKEN)