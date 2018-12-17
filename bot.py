from discord.ext import commands
import config
import os
from datetime import datetime

bot = commands.Bot(command_prefix=config.prefix)


@bot.event
async def on_ready():
    print('Ready!')


if __name__ == "__main__":
    for extension in os.listdir('cogs'):
        extension = extension[:-3]
        if extension == '__pycach':
            pass
        else:
            try:
                bot.load_extension('cogs.{}'.format(extension))
                print('{} Loaded\nTime: {}\n'.format(extension, datetime.now()))
            except Exception as e:
                print('Failed to load extension {}\nReason: {}'.format(extension, e))


bot.run(config.token)
