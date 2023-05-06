import discord
import asyncio
import sqlite3
from discord.ui import Button
from discord import ButtonStyle
import Buttons
from discord.ext import commands
from discord import Embed
from Config import TOKEN
import DatabaseCode
import asyncpg

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', case_insensitive=True, 
                   help_command=commands.DefaultHelpCommand(dm_help=False), 
                   intents=intents, owner_ids={605418818864414762, 678401615333556277})
bot.case_insensitive = True
bot.command_prefix = ['!']

#Create a new Character: Classes -> Mage, Swordsman, Archer
@bot.command(name = "create")
async def create(ctx):
    user_id = ctx.message.author.id
    embed = Embed(title="Character Classes", description="Please select a character")

    # add fields for each character class
    embed.add_field(name="Mage", value="A powerful class, using staffs to deal powerful attacks through the power of magic. The robes associated with a Mage boost's it's magical capabilities however lacks in hard defense.")
    embed.add_field(name="Swordsman", value="A class that excels in close combat, swordsman are trained to handle different types of swords with deadly precision. They boast excellent defense and HP, however suffer against ranged attacks.")
    embed.add_field(name="Archer", value="A class specialized in ranged attacks, archers use their bows and arrows to keep their enemies at bay. They have high mobility and excel at attacking from afar, while maintaining their hides provide protection.")
    # add reactions to the embed for user selection
    embed.set_footer(text="React with the corresponding emoji to select a character")
    #embed.add_field(name="\u200b", value=":one: - Mage\n:two: - Swordsman\n:three: - Archer")
    Mage_Button = Buttons.MageButton(user_id, bot)
    Swordsman_Button = Buttons.SwordsmanButton(user_id, bot)
    Archer_Button = Buttons.ArcherButton(user_id, bot)
    view = discord.ui.View()
    view.add_item(Mage_Button)
    view.add_item(Swordsman_Button)
    view.add_item(Archer_Button)
    message = await ctx.send(embed=embed)
    await ctx.send("Pick a character", view=view)

    

    





async def main():
    # Connect to the PostgreSQL database
    conn = await asyncpg.connect(
        host='your_database_host',
        port=5432,
        user='your_database_user',
        password='your_database_password',
        database='your_database_name'
    )
    await DatabaseCode.create_table(conn)
    #await load_extensions()
    await bot.login(TOKEN)
    await bot.connect()
    await bot.run()




async def load_extensions():
    #await bot.load_extension("jishaku")
    await bot.load_extension("Game")
    await bot.load_extension("DatabaseCode")
    #await bot.load_extension("Battle")
    #await bot.load_extension("Inventory")
    #await bot.load_extension("Potions")    


bot.run(TOKEN)
