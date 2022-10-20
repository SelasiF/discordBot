
import os #makes me able to create and remove folders (directories),fetch and identify. 
import discord 
import random
import typing
from typing import List
from typing import Tuple 
from discord.ext import commands #obvs makes commands 
#adminstrator permissions will be 8 
## tip to self: run the prgram in python3 to avoid errors!
bot = commands.Bot(command_prefix = '$')

##-------------------------------------------------------------------------
##                              EVENTS
@bot.event 
async def on_ready():
#On ready is basically when its ready the, bot will work then.
    print('Bot is ready.')

@bot.event 
async def on_member_join(member):
    print('(member) has joined dota peeps! ') 

@bot.event 
async def on_member_kick(member):
    print('(member) has left the peeps :( ')


@bot.event() 
async def info_error(ctx,error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Sorry I wasnt ale to do that')


 ##------------------------------------------------------------------------
 ##                         commands

@bot.command()
async def test(ctx):
    pass
##bot.add_command(test)

@bot.command() ##to make the bot say what you ask for 
async def speak(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def add(ctx,a : int,b : int):
    await ctx.send(a + b)
@bot.command()
async def multiply(ctx, a: int, b : int):
    await ctx.send( a * b)



class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx} slapped {to_slap} because *{argument}*'

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

class OutfitChecker(commands.Converter):
    async def convert(self, person1, person):
        return f'{person1} asked  to inspect *{person}*'
@bot.command()
async def outfitcheck(ctx, person, reason: OutfitChecker):
        await ctx.send(reason)
   
class JoinDistance:
    def __init__(self, joined, created):
      self.joined = joined 
      self.created = created 

    @property# question to ask, why is this used
    def delta(self):
        return self.joined - self.created # this is where we get the days for the if condition

class JoinDistanceConverter(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument) #super() gives it properties of parent class or sibling class
        return JoinDistance(member.joined_at, member.created_at)

@bot.command()
async def delta(ctx,*,member : JoinDistanceConverter ):
    is_new = member.delta.days < 100
    if is_new:
        await ctx.send(" hey youre pretty new!")
    else:
        await ctx.send("hm you're not so new.")
    
@bot.command()
async def joined(ctx, *, member:discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.form)




@bot.command()
async def union(ctx, what: typing.Union[discord.TextChannel, discord.Member]): 
    await ctx.send(what)
# what: basically does is it checks if the the first argument is valid, if not itll go to the next. left to right.

##discord preset change later 
@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid = "beer"):  
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))
#.Optional does is if the argument is left empty, itll still go with the presets you laid out before 
#instead of using .Optional you can use .Greedy[], but they can be used together. .Greedy[] just tries to take as many
#the user inputted.
@bot.command()
async def ping(ctx):
    await ctx.send(f' ping is {round(bot.latency * 1000)}ms') #*1000 because it is givin in mili secs

@bot.command( aliases=['8ball', 'wishdubblah'])
async def seer(ctx,*, question):
    responses =[ "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."
    ]
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@bot.command() 
async def r2d2_clean(ctx,amount = 1): # the amount is preset to 1 so itll clear one line whenever it is called 
        await ctx.channel.purge(limit = amount) #.purge just deletes it from the channel it was called in 

@bot.command()
async def kick( ctx , member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

#tips member : discord.Member is an argument used to use @savaze and etc
#     typing.Optional is placed right after an argument you feel like it isnt needed
#       ctx.channel.purge is to delete. i think with .purge you can delete but idk to what extent
#       .Greedy takes as many parameters as it can take 

@bot.command()
async def unban(ctx,* member):
    banned_users = await ctx.guild.bans()

@bot.command()
async def super
#Eror handling 

#@bot.check
#async def globally_block_dms(ctx):         this blocks all dms. is it because of the ctx.guild is set to none? 
#    return ctx.guild is not None               and that causes it to not able to send DMS because the guild doesnt exist




# the difference in this one is that we are using Tuple. Tuple is like the .Greedy 
# now the b
#flag = flag is a class variable witha type of annotation or a class variable thats been assigned by the result of the flag
#my understanding = a flag assigns the value or tells the comp that a certain condition is met or permission.
# burr said a flag is bascially a switch that you set to true or false 






bot.run('OTM3ODI1NDk5NTM3ODc5MTEw.Gyigxd._Yxz1dHAvme-w6GhbYDvdJu6VEqORw0eSLycLI')#this is where we store the token