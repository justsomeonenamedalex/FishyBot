import discord
from discord.ext import commands, tasks
import os
import time

client = commands.Bot(command_prefix="f!")


# Functions



# Events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Fishing"))
    print(f"Bot is ready {time.time()}")
    await client.change_presence(activity=discord.Game("Fishing"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments")
        print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'. {time.time()}")
    elif isinstance(error, commands.CommandNotFound):
        print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'. {time.time()}")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to run that command.")
        print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'. {time.time()}")
    else:
        print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'. {time.time()}")


# Tasks

# Checks
@client.command()
@commands.is_owner()
async def owner_check(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}")
    print(f"Passed owner check. {time.time()}")


# Commands - Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} loaded.")
    print(f"Loaded extension {extension} {time.time()}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} unloaded.")
    print(f"Unloaded extension {extension}. {time.time()}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}.")
    print(f"Reloaded {extension}. {time.time()}")

# Commands - Dev
@client.command()
async def bot_activity(ctx, activity=None):
    await client.change_presence(activity=discord.Game(activity))
    await ctx.send(f"Activity set to {activity}")
    print(f"Activity set to {activity}. {time.time()}")


@client.command()
async def goodnight(ctx):
    await ctx.send(f"Goodnight!")
    print(f"Bot shutdown. {time.time()}")
    await client.logout()


@commands.is_owner()
async def invite(ctx):
    await ctx.send("")


# Main Command


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
    print(f"Pong! {round(client.latency * 1000)}ms. {time.time()}")

# Startup

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("")
