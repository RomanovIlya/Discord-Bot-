import discord
from discord.ext.tasks import loop
from discord.ext import commands
from discord.utils import get
from discord_together import DiscordTogether
from discord_components import DiscordComponents,Button,ButtonStyle



Prefix='!'
bot = discord.Client()
bot=commands.Bot(command_prefix=Prefix, intents=discord.Intents.all())
bot.remove_command('help')
Bad=["блять","блт","блят","пошёл нахуй","пшл нхй","ахуел","чилипиздрик","пизда","пиздеть","пиздабол","хуй","отъебись","ебало","ебаный","ёбаный","ебанный","ёбанный","Хуевыблядок","Сукаёб","Хуеглот","Мурло","Сучара","Блядогон","Бляхомудия","Впиздячил","Ёбнул","Выебоны","Голоёбица","Глупизди","ДЕРЬМОХЕРОПИЗДОКРАТ"]
ChannelIDJ=971743180674441276
ChannelIDL=971743212802822166


@bot.event
async def on_ready():
    print("-Акк бота-")
    print()
    print(f"Имя бота:{bot.user.name}")
    print(f"ID бота:{bot.user.id}")
    print(f"Токен бота:{'OTcxNzQ4MTM3ODIxNjk2MDUx.YnPA-g.rEcTLJOXa3EdVBLChfnofl0uDIk'}")
    print()
    print('We have logged in as {0.user}'.format(bot))

    DiscordComponents(bot)
    bot.togetherControl=await DiscordTogether('OTcxNzQ4MTM3ODIxNjk2MDUx.YnPA-g.rEcTLJOXa3EdVBLChfnofl0uDIk')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Visual Studio'))

@bot.event
async def on_message(message):
  for i in range(0,len(Bad)):
    if Bad[i] in message.content.lower():
        await message.delete()
  await bot.process_commands(message)

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.name=="Создать канал😎":
        print(f"Пользователь {member.name} зашел на {after.channel.name}")
        category2 = member.guild.get_channel(979704449419313193)
        channel2= await member.guild.create_voice_channel(f"Комната: {member.name}", overwrites=None, category=category2,reason=None)

        await member.move_to(channel2)

    if before.channel and before.channel.name.startswith("Комната: "):
        if len(before.channel.members) == 0:
            await before.channel.delete()


@bot.event
async def on_member_join(member):
    rolee=discord.utils.get(member.guild.roles,name='Every')
    channel=bot.get_channel(ChannelIDJ)
    ch=bot.get_channel(977656826487242842)
    await channel.send(embed=discord.Embed(description=f'Добро пожаловать ``{member}`` на наш сервер! Здесь ты узнаешь много нового!',colour=discord.Color.red()))
    await member.send(embed=discord.Embed(description=f'Добро пожаловать ``{member}`` на IT-Programming!\nРаспологайся! Вы можете узнать мои команды при помощью !help.\nТакже вы можете оставить отзыв о сервере:\nhttps://forms.gle/972LEEfCaRhtwegs7',colour=discord.Color.red()))
    await ch.send(
        embed=discord.Embed(description=f'Добро пожаловать ``{member}`` на наш сервер! Пожалуйста выберети какой вы программист:',colour=discord.Color.red()),
        components=[
            Button(style=ButtonStyle.green,label="Python",emoji='🐍'),
            Button(style=ButtonStyle.green,label="С++",emoji='😈')
        ]
        )
    response=await bot.wait_for("button_click")
    if response.channel==ch:
        if response.component.label=="Python":
            role=discord.utils.get(member.guild.roles,name='🐍Python')
            await member.add_roles(role,rolee)

    respons=await bot.wait_for("button_click")
    if respons.channel==ch:  
        if respons.component.label=="С++":
            c=discord.utils.get(member.guild.roles,name='😈С++')
            await member.add_roles(c,rolee)


@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(ChannelIDL)
    await channel.send(embed=discord.Embed(description=f'``{member}`` покинул наш сервер!',colour=discord.Color.red()))

@bot.event
async def on_command_error(ctx,error):
    pass

@bot.command()
async def join(ctx):
    global voice
    channel=ctx. message.author. voice.channel
    voice=get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected ():
        await voice.move_to(channel)
    else:
        voice=await channel.connect()
        await ctx.send (f"Бот присоеденился к:{channel}")

@bot.command()
async def leave(ctx):
    global voice
    channel=ctx. message.author. voice.channel
    voice=get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected ():
        await voice.disconnect()
    else:
        voice=await channel.connect()
        await ctx.send (f"Бот отключился от :{channel}") 


@bot.command(pass_context=True)
@commands.has_permissions( administrator=True)
async def clear(ctx, amount=100 ):
    await ctx.channel.purge( limit=amount+1)

@bot.command()
async def help(ctx):
    emb=discord.Embed(title="Навигация по коммандам",colour=discord.Color.red())
    emb.add_field(name='{}join :'.format(Prefix),value='Присоединение бота к голосовому каналу')
    emb.add_field(name='{}leave :'.format(Prefix),value='Отсоединение бота от голосового канала')
    emb.add_field(name='{}youtube :'.format(Prefix),value='Смотрим ютуб вместе(сначала присоединитесь к гк)')
    emb.add_field(name='{}card :'.format(Prefix),value='Карточка пользователя')
    
    CH=977545358978744332
    channel=bot.get_channel(CH)
    

    embed=discord.Embed(title="Навигация по коммандам для админов",colour=discord.Color.red())
    embed.add_field(name='{}join :'.format(Prefix),value='Присоединение бота к голосовому каналу')
    embed.add_field(name='{}leave :'.format(Prefix),value='Отсоединение бота от голосового канала')
    embed.add_field(name='{}youtube :'.format(Prefix),value='Смотрим ютуб вместе(сначала присоединитесь к гк)')
    embed.add_field(name='{}card :'.format(Prefix),value='Карточка пользователя')
    embed.add_field(name='{}clear :'.format(Prefix),value='Очищение чата')
    embed.add_field(name='{}mute :'.format(Prefix),value='Заглушение пользователя')
    embed.add_field(name='{}unmute :'.format(Prefix),value='Наоборот mute')
    embed.add_field(name='{}create_voice_channel :'.format(Prefix),value='Создание голосового канала')
    embed.add_field(name='{}create_text_channel :'.format(Prefix),value='Создание текстового канала')


    if ctx.author.id==690187627093033190:
        await ctx.channel.purge( limit=1)
        await channel.send(embed=embed)
        await ctx.send(embed=emb)

    else:
        await ctx.send(embed=emb)

    

@bot.command()
async def youtube(ctx):
    link=await bot.togetherControl.create_link(ctx.author.voice.channel.id,'youtube')
    emb=discord.Embed(title='Youtube',description=f"Вот ссылка:{link} {ctx.author.mention}",colour=discord.Color.red())
    await ctx.send(embed=emb)

@bot.command()
async def card(ctx):
    name=ctx.author.name
    id=ctx.author.id
    photo=ctx.author.avatar_url

    emb=discord.Embed(title="Карта пользователя",colour=discord.Color.red())
    emb.add_field(name='Имя:',value=name)
    emb.add_field(name='ID :',value=id)
    emb.set_thumbnail(url=photo)

    await ctx.send(embed=emb)

@bot.command()
#@commands.has_permissions( administrator=True)
async def mute(ctx,member: discord.Member):
    await ctx.channel.purge( limit=1)
    channel=bot.get_channel(977545358978744332)
    rolee=discord.utils.get(member.guild.roles,name='Every')
    mute=discord.utils.get(member.guild.roles,name='@mute')
    await member.remove_roles(rolee)
    await member.add_roles(mute)
    await member.send(embed=discord.Embed(description=f'Вы были заглушёны',colour=discord.Color.red()))

            
    

@bot.command()
@commands.has_permissions( administrator=True)
async def unmute(ctx,member: discord.Member):
    await ctx.channel.purge( limit=1)
    rolee=discord.utils.get(member.guild.roles,name='Every')
    mute=discord.utils.get(member.guild.roles,name='@mute')
    await member.remove_roles(mute)
    await member.add_roles(rolee)
    await ctx.send(embed=discord.Embed(description=f'``{member}`` больше не заглушён',colour=discord.Color.red()))

@bot.command()
@commands.has_permissions( administrator=True)
async def kick(ctx,member: discord.Member,reason=None):
    await ctx.channel.purge( limit=1)
    channel=bot.get_channel(977545358978744332)
    await member.kick(reason=reason)
    await channel.send(embed=discord.Embed(description=f'``{member}`` был кикнут',colour=discord.Color.red()))

@bot.command()
@commands.has_permissions( administrator=True)
async def ban(ctx,member: discord.Member,reason):
    await ctx.channel.purge( limit=1)
    channel=bot.get_channel(977545358978744332)
    await member.ban(reason=reason)
    await channel.send(embed=discord.Embed(description=f'``{member}`` был выдан бан',colour=discord.Color.red()))

@bot.command()
@commands.has_permissions( administrator=True)
async def create_text_channel(ctx, channel_name):
	guild = ctx.guild
	channel = await guild.create_text_channel(channel_name)

@bot.command()
@commands.has_permissions( administrator=True)
async def create_voice_channel(ctx, channel_name):
	guild = ctx.guild
	channel = await guild.create_voice_channel(channel_name)




bot.run('Your token')

