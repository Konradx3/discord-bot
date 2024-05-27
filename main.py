import discord
from discord.ext import commands
from config import BOT_TOKEN, CHANNEL_ID
from ResourceView import ResourceView


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Bot is loaded')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Bot is ready to use')


@bot.command()
async def check_resource(ctx: commands.Context):
    await ctx.send('Wybierz surowiec aby sprawdzić jego cenę w różnych miastach', view=ResourceView())


if __name__ == '__main__':
    bot.run(BOT_TOKEN)
