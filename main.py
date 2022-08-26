import random, os, discord
from anekos import NekosLifeClient, SFWImageTags

with open(f"./token.txt", "r") as f:
    TOKEN = f.read()

client = discord.Client()
nekoClient = NekosLifeClient()

prefix = '='


@client.event
async def on_ready():
    result = await nekoClient.image(SFWImageTags.NEKO)
    print(result.url)
    print("Logged in as {0.user}".format(client))
    await client.change_presence(status=discord.Status('online'),
                                 activity=discord.Game(name="Time to conquer the heavens", url="technoblade.com"))
    # await client.get_channel(987005532214804510).send(result.url)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author).split('#')[0]
    user_id = str(message.author.id)
    user_message = str(message.content)
    channel = str(message.channel.name)

    # if username == "RThom":
    #  role = discord.utils.get(message.guild.roles, name="bot")
    # await message.author.add_roles(role)

    if message.guild.name != "Valoobant":
        print(f'({message.guild.name}) {username}: {user_message} ({channel})')
        with open(f"./Cant-logs.txt", "a+") as f:
            f.write(f"({message.guild.name}) {username}: {user_message} ({channel})\n")

    if message.channel.name != (
            "boomer-submission-channel" and "pumps-submission-channel" and "dingy-submission-channel"):
        if 'boomer' in user_message.lower():
            file = random.choice(os.listdir("./Boomer/"))
            print(file)
            await message.channel.send(file=discord.File("./Boomer/" + file))
        if 'pumps' in user_message.lower():
            file = random.choice(os.listdir("./Pumps/"))
            print(file)
            await message.channel.send(file=discord.File("./Pumps/" + file))

    if message.channel.name == 'bot-testing' or message.channel.name == 'announcements' and message.guild.name != "Valboont":
        if user_message.lower() == prefix + 'love':
            await message.channel.send(f'I love you <@{user_id}>')
            return
        if user_message.lower() == "i love dingy bot":
            await message.channel.send(f'I love you too <@{user_id}>!')
            return
        if '<@986711862861242448>' in user_message.lower():
            for x in range(5):
                await message.channel.send(f'Stop pinging me <@{user_id}>!')
            return
        if user_message.lower() == prefix + "neko":
            result = await nekoClient.image(SFWImageTags.NEKO)  # nsfwLewd, Gasm, spank(gif),
            await message.channel.send(result.url)
            return
        if user_message.lower() == prefix + "prussia":
            for x in range(5):
                await message.channel.send(f'https://tenor.com/view/chad-giga-gigachad-prussia-gif-24245950')
            return

    elif user_message.startswith(prefix) and message.channel.name != "idea-submissions":
        await message.channel.send(f"I don't work in here :angry:")


client.run(TOKEN)