from discord.ext import commands
import random


class RockPaperScissors:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def rps(self, ctx, rpos):
        if ctx.message.author.bot:
            return

        choices = ['rock', 'paper', 'scissors']

        if rpos not in choices:
            return await self.bot.say('Invalid Move!')

        choice = random.choice(choices)

        await self.bot.say('I choose ' + choice)

        if rpos == 'rock':
            if choice == 'rock':
                await self.bot.say('Tie')
                return
            if choice == 'paper':
                await self.bot.say('I Won!')
                return
            if choice == 'scissors':
                await self.bot.say('{} Won!'.format(ctx.message.author.mention))
                return
        if rpos == 'paper':
            if choice == 'rock':
                await self.bot.say('{} Won!'.format(ctx.message.author.mention))
                return
            if choice == 'paper':
                await self.bot.say('Tie')
                return
            if choice == 'scissors':
                await self.bot.say('I Won!')
                return
        if rpos == 'scissors':
            if choice == 'rock':
                await self.bot.say('I Won!')
                return
            if choice == 'paper':
                await self.bot.say('{} Won!'.format(ctx.message.author.mention))
                return
            if choice == 'scissors':
                await self.bot.say('Tie')
                return


def setup(bot):
    bot.add_cog(RockPaperScissors(bot))
