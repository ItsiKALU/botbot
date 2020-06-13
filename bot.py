import discord
import asyncio
import datetime
import Dtime
from discord.ext    import commands
from discord.ext.commands   import bot
from discord.utils import get

client = discord.Client()
uptime = Dtime.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('봇이 정상적으로 실행되었습니다.')
    messages = [f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', "모든게임을 최저가로 판매", "구매문의 : KALU#0001", "배너문의 : LUCA#2875", ""]
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(5)
    author = await client.get_user(682801545343270958).create_dm()
    await author.send("[ 모든게임 최저가 도우미 ] 봇이 정상적으로 시작되었습니다 !")
    author = await client.get_user(305484336470425600).create_dm()
    await author.send("[ 모든게임 최저가 도우미 ] 봇이 정상적으로 시작되었습니다 !")
    
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="📋접속로그📋")
    await channel.send(f"**{member.mention}**님 모든게임최저가 루카샵에 오신걸 환영합니다 !! 현재 유저수 : {len(list(member.guild.members))}")
    role = discord.utils.get(member.guild.roles, id=int("699938225023614976"))
    await member.add_roles(role)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.channel.id == 708873677122568202:
        if message.author.id == 682801545343270958:
            await message.add_reaction("<:1_:708875436238569533>")
            await message.add_reaction("<:2_:708875456383942666>")
            await message.add_reaction("<:3_:708875476726448158>")
            await message.add_reaction("<:4_:708875650433548379>")
            await message.add_reaction("<:5_:708875657861529642>")
            await message.channel.send("위 이모지를 선택하여 판매자를 평가해주세요 :)")

    if message.channel.id == 708873677122568202:
        if message.author.id == 305484336470425600:
            await message.add_reaction("<:1_:708875436238569533>")
            await message.add_reaction("<:2_:708875456383942666>")
            await message.add_reaction("<:3_:708875476726448158>")
            await message.add_reaction("<:4_:708875650433548379>")
            await message.add_reaction("<:5_:708875657861529642>")
            await message.channel.send("위 이모지를 선택하여 판매자를 평가해주세요 :)")

    if message.content.startswith('!dm0'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id ==682801545343270958:
                        embed = discord.Embed(colour=0xe0ff00, timestamp=message.created_at, title="[ 모든게임 최저가 ]")
                        embed.add_field(name="모든게임 최저가 공지사항 - 루카", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/BEZp5ZS")
                        await i.send(embed=embed)
                except:
                    pass

    if message.content.startswith('!dm1'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id ==305484336470425600:
                        embed = discord.Embed(colour=0xe0ff00, timestamp=message.created_at, title="[ 모든게임 최저가 ]")
                        embed.add_field(name="모든게임 최저가 공지사항 - 칼루", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/BEZp5ZS")
                        await i.send(embed=embed)
                except:
                    pass

    if message.content.startswith('!업타임'):
        await message.channel.send(f"{uptime.hours()}시간 {uptime.minitues()}분 {uptime.seconds()}초 동안 봇이 실행되고 있습니다 .")

client.run("NzIxMjQyMTM1NzM4ODQzMTc2.XuRrYw.IFA5FV0jG1obUdxsL8AneozRVyA")