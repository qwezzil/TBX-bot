import discord
from discord.ext import commands
from discord.ui import View
import os


class RoleView(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def toggle(self, interaction, role_id):
        role = interaction.guild.get_role(role_id)
        if not role:
            await interaction.response.send_message("Role not found", ephemeral=True)
            return

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Removed: {role.name}", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Added: {role.name}", ephemeral=True)

  
    @discord.ui.button(label="Sneak Peeks", style=discord.ButtonStyle.primary, custom_id="r_sneak")
    async def b1(self, i, b): await self.toggle(i, 1444046588434710690)

    @discord.ui.button(label="Polls", style=discord.ButtonStyle.primary, custom_id="r_polls")
    async def b2(self, i, b): await self.toggle(i, 1444046590368157880)

    @discord.ui.button(label="Giveaway", style=discord.ButtonStyle.primary, custom_id="r_give")
    async def b3(self, i, b): await self.toggle(i, 1444046587734261910)

    @discord.ui.button(label="Game Night", style=discord.ButtonStyle.primary, custom_id="r_game")
    async def b4(self, i, b): await self.toggle(i, 1444046587046134011)

    @discord.ui.button(label="Updates", style=discord.ButtonStyle.primary, custom_id="r_upd")
    async def b5(self, i, b): await self.toggle(i, 1474637430345826344)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    bot.add_view(RoleView())
    print(f"БОТ В СЕТИ: {bot.user}")

@bot.command()
async def send_roles(ctx):
    embed = discord.Embed(
        title="Roles", 
        description="Choose your role by clicking one of the buttons below. This will give you access to specific channels and let others know your interests. You can change or remove your role at any time.", 
        color=0x2b2d31
    )
    
    embed.set_image(url="https://cdn.discordapp.com/attachments/1474492252842627316/1474755141042438174/roles_banner_for_discord___by_krazibeast_dflgeiu-fullview.png")

    await ctx.send(embed=embed, view=RoleView())

# Запуск
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
