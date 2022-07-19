import conf
import discord
from discord.ext import commands as cmd
from discord import FFmpegPCMAudio as ffmpeg

intents = discord.Intents.default()
intents.members = True
client = cmd.Bot(command_prefix = '#', intents=intents)

@client.event
async def on_ready():
    print("Logged in...")

@client.event
async def on_member_join(member):
    channel = client.get_channel(conf.ID)
    await channel.send("Welcome " + str(member) + "!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(conf.ID)
    await channel.send("See you later, " + str(member) + "...")

@client.command(pass_context=True)
async def join(context):
    if context.author.voice:
        channel = context.message.author.voice.channel
        voice = await channel.connect()
        player = voice.play(ffmpeg(executable=conf.FFMPEG, source=conf.SRC))
    else:
        await context.send("I am currently not connected to a channel...")

@client.command(pass_context=True)
async def leave(context):
    if context.voice_client:
        await context.guild.voice_client.disconnect()
        await context.send("I have to leave... Bye!")
    else:
        await context.send("Currently busy! Please try again later...")

client.run(conf.TOKEN)