import discord
from discord.ui import Button
from discord import ButtonStyle



class MageButton(discord.ui.Button):
    def __init__(self, user_id, bot):
        super().__init__(style=discord.ButtonStyle.green, label="Mage")
        self.clicked = False
        self.user_id = user_id
        self.bot = bot
    
    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id == self.user_id and not self.clicked:
            self.clicked = True
            await interaction.message.delete()
            await interaction.channel.send("Please enter your player name:")
            def check(message):
                return message.author == interaction.user and message.channel == interaction.channel
            message = await self.bot.wait_for('message', check=check)
            player_name = message.content
            await interaction.channel.send(f"Your player name is: {player_name}")
            return ("mage", player_name)
            

class SwordsmanButton(discord.ui.Button):
    def __init__(self,user_id, bot):
        super().__init__(style=discord.ButtonStyle.green, label="Swordsman")
        self.clicked = False
        self.user_id = user_id
        self.bot = bot 
    
    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id == self.user_id and not self.clicked:
            self.clicked = True
            await interaction.message.delete()
            await interaction.channel.send("Please enter your player name:")
            def check(message):
                return message.author == interaction.user and message.channel == interaction.channel
            message = await self.bot.wait_for('message', check=check)
            player_name = message.content
            await interaction.channel.send(f"Your player name is: {player_name}")
            return ("archer", player_name)


class ArcherButton(discord.ui.Button):
    def __init__(self,user_id, bot):
        super().__init__(style=discord.ButtonStyle.green, label="Archer")
        self.clicked = False
        self.user_id = user_id
        self.bot = bot
    
    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id == self.user_id and not self.clicked:
            self.clicked = True
            await interaction.message.delete()
            await interaction.channel.send("Please enter your player name:")
            def check(message):
                return message.author == interaction.user and message.channel == interaction.channel
            message = await self.bot.wait_for('message', check=check)
            player_name = message.content
            await interaction.channel.send(f"Your player name is: {player_name}")
            return ("swordsman", player_name)

