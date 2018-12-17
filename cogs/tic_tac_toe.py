from discord.ext import commands
import asyncio
import random


class TicTacToe:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ttt(self, ctx):
        if ctx.message.author.bot:
            return
    
        players = ['x', 'o']
        positions = {'pos1': 1, 'pos2': 2, 'pos3': 3,
                     'pos4': 4, 'pos5': 5, 'pos6': 6,
                     'pos7': 7, 'pos8': 8, 'pos9': 9}
        board_format = '{} | {} | {}\n--------\n{} | {} | {}\n--------\n{} | {} | {}'
    
        board = await self.bot.say(board_format.format(positions['pos1'], positions['pos2'], positions['pos3'], positions['pos4'], positions['pos5'], positions['pos6'], positions['pos7'], positions['pos8'], positions['pos9']))
    
        async def check_completion(gd):
            status = {'winner': False, 'filled': False}
    
            for player in players:
                if gd['pos1'] == player:
                    if gd['pos4'] == player:
                        if gd['pos7'] == player:
                            status['winner'] = player
                    if gd['pos5'] == player:
                        if gd['pos9'] == player:
                            status['winner'] = player
                    if gd['pos2'] == player:
                        if gd['pos3'] == player:
                            status['winner'] = player
                if gd['pos2'] == player:
                    if gd['pos5'] == player:
                        if gd['pos8'] == player:
                            status['winner'] = player
                if gd['pos3'] == player:
                    if gd['pos6'] == player:
                        if gd['pos9'] == player:
                            status['winner'] = player
                if gd['pos4'] == player:
                    if gd['pos5'] == player:
                        if gd['pos6'] == player:
                            status['winner'] = player
                if gd['pos7'] == player:
                    if gd['pos5'] == player:
                        if gd['pos3'] == player:
                            status['winner'] = player
                    if gd['pos8'] == player:
                        if gd['pos9'] == player:
                            status['winner'] = player
    
            counter = 0
            for position in gd:
    
                if gd[position] not in players:
                    pass
                else:
                    counter = counter + 1
    
            if counter == len(gd):
                status['filled'] = True
    
            return status
    
        async def check_taken(gd, pos):
            pos = 'pos{}'.format(pos)
            if gd[pos] not in players:
                return False
            else:
                return True
        while True:
            user_play = True
    
            while user_play:
                completed: dict = await check_completion(positions)
    
                if completed['winner'] in players:
                    return await self.bot.say('Winner: {}'.format(completed['winner']))
                if completed['filled']:
                    return await self.bot.say('Tie')
    
                prompt = await self.bot.say('Select A Position...')
                response = await self.bot.wait_for_message(author=ctx.message.author)
    
                await self.bot.delete_message(prompt)
    
                taken = await check_taken(positions, response.content)
    
                if taken:
                    await self.bot.delete_message(response)
                    response_prompt = await self.bot.say('That Position Is Already Taken!')
                    await asyncio.sleep(3)
                    await self.bot.delete_message(response_prompt)
                    user_play = True
                else:
                    positions['pos{}'.format(response.content)] = 'x'
    
                    await self.bot.delete_message(response)
    
                    await self.bot.edit_message(board, new_content=board_format.format(positions['pos1'], positions['pos2'], positions['pos3'], positions['pos4'], positions['pos5'], positions['pos6'], positions['pos7'], positions['pos8'], positions['pos9']))
    
                    user_play = False
    
            bot_play = True
    
            while bot_play:
                completed: dict = await check_completion(positions)
    
                if completed['winner'] in players:
                    return await self.bot.say('Winner: {}'.format(completed['winner']))
                if completed['filled']:
                    return await self.bot.say('Tie')
    
                choice = random.randint(1, 9)
    
                taken = await check_taken(positions, choice)
    
                if taken:
                    bot_play = True
                else:
                    positions['pos{}'.format(choice)] = 'o'
    
                    await self.bot.edit_message(board, new_content=board_format.format(positions['pos1'], positions['pos2'], positions['pos3'], positions['pos4'], positions['pos5'], positions['pos6'], positions['pos7'], positions['pos8'], positions['pos9']))
    
                    bot_play = False


def setup(bot):
    bot.add_cog(TicTacToe(bot))
