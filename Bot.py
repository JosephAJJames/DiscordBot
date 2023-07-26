import discord
from discord.ext import commands
from datetime import datetime

discordToken = "MTEzMzAzODEwNzQxMTg3Mzg3NA.GLcrH_.1P_2nqRS2PZdTG5crMXtDBqKd2SJhq_PUEeVhc"

def british_short_to_long_date(date_str):
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    long_date_str = date_obj.strftime("%A %d %B")

    day_suffix = "th" if 11 <= date_obj.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(date_obj.day % 10, "th")
    long_date_str = long_date_str.replace(str(date_obj.day), str(date_obj.day) + day_suffix)

    return long_date_str

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot loaded")

@client.command()
async def scrim(ctx):
    channel_id = ctx.channel.id
    if channel_id == 1133047688036892744:
        channel = client.get_channel(1133042922208632883)
        message = ctx.message.content
        value_list = message.split(",")
        value_list.pop(0)
        date_string = value_list[-1].strip()
        await channel.send(british_short_to_long_date(date_string))
        value_list.pop()  # Remove the last element from the list (the date string)
        for x in value_list:
            await channel.send(x.strip())  # Strip whitespace from each element
        await channel.send("Reaction")  # Send the "Reaction" string to the original channel
        emoji = '\N{THUMBS UP SIGN}'
        async for message in channel.history(limit=1):
            await message.add_reaction("👍")  # Add the thumbs-up emoji reaction
            await message.add_reaction("👎")  # Add the thumbs-down emoji reaction
            await message.add_reaction("❓")
    else:
        await ctx.send("You can only use /Scrim in the 'Bot-Scrim' channel")


@client.command()
async def kill(ctx):
    await ctx.send("Bot Closing...")
    exit()



client.run(discordToken)