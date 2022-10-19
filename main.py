import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!!', intents= intents)


@bot.command()
async def chooseFromChannel(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author

    try:
        channel = bot.get_channel(member.voice.channel.id)
        curMembers=[]
        for member in channel.members:
            curMembers.append(member.id)
        #chosen = await bot.fetch_user(random.choice(curMembers))
        chosen = random.choice(curMembers)
        await ctx.send(f"<@{chosen}> was chosen!")
    except AttributeError:
        return await ctx.send("User is not in a channel.")
bot.run(os.getenv('TOKEN'))