import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds= True, reactions = True, members = True, presences = True)

Bot = commands.Bot("!m ",intents = intents)
@Bot.event
async def on_ready():
      print("I'm ready")

@Bot.event
async  def on_member_join(member):
      channel = discord.utils.get(member.guild.text_channels, name="the name of your reception room")
      await channel.send(f"The castle gates were opened and  {member} entered the castle gate")
      print("Login successful")

@Bot.event
async  def on_member_remove(member):
      channel = discord.utils.get(member.guild.text_channels, name="the name of your reception room")
      await channel.send(f"The castle gates were opened and  {member} came out of the castle gate")
      print("Logout successful")

Bot.run("your token")