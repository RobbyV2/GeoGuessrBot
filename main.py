"""
TODO:
One lobby at a time unless geoguessr supports otherwise.
Mode switching (invite button changes & only admins).
Async loading of geoguessr pro accounts, make a db of codes that are in use with players, if the code exists, use another account, otherwise send an existing one and warn the player, add to info as well.
Add generic useful geoguessr utilities.
Fix long wait times through some means (get cookie, set cookie, api calls).
Play against the bot.
Switch to use cogs for each command.
Loading screen in terminal.

INFO:
Currently, it's set the team duels on the account, so that's what shows up by default on the code.
"""

import json
import asyncio
import datetime
import typing

import discord
from discord.ext import commands
from discord import app_commands

from utils.getCode import getCode
from utils.switchModes import switchMode

with open("config.json") as config_file:
    config = json.load(config_file)

token = config["token"]
appid = config["appid"]
prefix = config["prefix"]
admins = config["admins"]
version = "0.0.1"
start_time = datetime.datetime.utcnow()

config_file.close

intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(
    command_prefix=prefix,
    intents=intents,
    case_insensitive=True,
    reconnect=True,
    application_id=appid,
)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(
        """
  ___   ___    ____   __  ____ 
 / __) / __)  (  _ \ /  \(_  _)
( (_ \( (_ \   ) _ (( 🌍 )) (  
 \___/ \___/  (____/ \__/ (__) 
"""
    )
    try:
        synced = await bot.tree.sync()
        if int(len(synced)) == 1:
            print(f"{len(synced)} slash command loaded.")
        else:
            print(f"{len(synced)} slash commands loaded.")
    except Exception as e:
        print(f"There was an error loading the slash commands.")
    print(f"""Logged in as {bot.user.name}! ID: {bot.user.id} Prefix: {prefix}""")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"😈 Rainbolt"
        )
    )


@bot.tree.command(name="invite", description="Get the bot's invite link.")
async def invite(interaction: discord.Interaction):
    permissions = discord.Permissions(517547220545)
    url = f"https://discord.com/api/oauth2/authorize?client_id={appid}&permissions={permissions.value}&scope=bot"
    await interaction.response.send_message("### GGBot Invite:\n" + url, ephemeral=True)


@bot.tree.command(name="info", description="Shows bot information.")
async def invite(interaction: discord.Interaction):
    uptime = datetime.datetime.utcnow() - start_time
    days, seconds = uptime.days, uptime.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    info_message = (
        f"Bot version: `{version}`\n"
        f"Accounts with GeoGuessr Pro: `1`\n"
        f"Bot uptime: `{days} days, {hours} hours, {minutes} minutes, {seconds} seconds`"
    )

    await interaction.response.send_message(info_message, ephemeral=True)


@bot.tree.command(name="get_code", description="Sends a GeoGuessr lobby join code.")
async def get_code(interaction: discord.Interaction):
    await interaction.response.send_message("Please wait..", ephemeral=True)
    try:
        loop = asyncio.get_event_loop()
        code = await loop.run_in_executor(None, getCode)

        code = f"### GeoGuessr Lobby Link\nhttps://www.geoguessr.com/join/{code}?s=Url\n\nCode: `{code}`"
        await interaction.followup.send(content=code, ephemeral=True)
    except Exception as e:
        await interaction.followup.send(
            content=f"### An error occurred:\n```bash\n{e}```", ephemeral=True
        )


@bot.tree.command(name="switch_mode", description="Switches GeoGuessr game modes.")
async def switch_mode(interaction: discord.Interaction, mode: str):
    await interaction.response.send_message("Please wait..", ephemeral=True)
    try:
        loop = asyncio.get_event_loop()
        switch_mode_func = await loop.run_in_executor(None, switchMode, mode)
        if switch_mode_func is None:
            pass
        await interaction.followup.send(
            content="### Switched mode to " + mode + ".", ephemeral=True
        )
    except Exception as e:
        await interaction.followup.send(
            content=f"### An error occurred:\n```bash\n{e}```", ephemeral=True
        )


@switch_mode.autocomplete("mode")
async def switch_mode_autocomplete(
    interaction: discord.Interaction, current: str
) -> typing.List[app_commands.Choice[str]]:
    data = []
    for mode_choice in ["Team Duels", "Duels", "Battle Royale Distance"]:
        data.append(app_commands.Choice(name=mode_choice, value=mode_choice))
    return data


bot.run(token)
