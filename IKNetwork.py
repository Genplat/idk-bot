import discord
from discord.ext import commands
#from discord.ext.commands import MissingPermissions
from discord.ext.commands import has_permissions
from random import randint
import time
from discord import ActionRow, Button, ButtonStyle
from discord import app_commands
#from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.all()
intents.messages = True

IKNetwork = commands.Bot(command_prefix="ik!",intents=intents)
IKNetwork.remove_command("help")

embedinvite = discord.Embed(title="Invite Bot")
embedinvite = embedinvite.add_field(name="Invite YOUR_BOT_NAME:",value="YOUR LINK HERE")

print("IK Newtork | IK")
print("By Genplat")

token = "YOUR TOKEN HERE"

@IKNetwork.event
async def on_ready():
    print("Iniciando. . .")
    print('IK Newtork | Example Bot | IdK Random Bot.')
    print("")
    #await IKNetwork.change_presence(status=discord.Status.dnd, activity=custom)
    await IKNetwork.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="ik!help | YOUR_BOT_NAME"))
    print("Bot Iniciado!")

@IKNetwork.event
async def on_guild_join(guild):
    channel = await guild.create_text_channel("ik-network")
    embed = discord.Embed(
        title="Welcome | IK Network",
        description=f"El bot se ha añadido con exito al servidor. <a:ik_check:1038404454153736273> \n Espero que disfrutes de usar este bot multiproposito. Hecho por Genplat Dev \n Para ver los creditos usa ik!credits \n \n **Mi prefijo es:** `ik!` \n Usa `ik!help view` para ver todas las categorias de comandos",
        colour=discord.Color.green()
    )
    await channel.send(embed=embed)

@IKNetwork.event
async def on_member_join(member):
    memberid = member.id
    embed = discord.Embed(
        title="Welcome | IK Network <:ik_info:1038408927307640952>",
        description=f"Nombre: <@{memberid}> \n Bienvenido al servidor!!! Pasalo bien \n Bot By: Genplat Dev \n Tu ID: {memberid}",
        colour=discord.Color.orange()
    )
    await member.send(embed=embed)

@IKNetwork.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="ERROR:",
            description="Comando desconocido, para ver la lista de comandos usa `ik!help view` y se mostrara la lista. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title="ERROR:",
            description="Argumentos invalidos, para ver la lista de comandos usa `ik!help view` y se mostrara la lista. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="ERROR:",
            description="Faltan argumentos obligatorios, para ver la lista de comandos usa `ik!help view` y se mostrara la lista. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="ERROR:",
            description="Permisos insuficientes, para ver la lista de comandos usa `ik!help view` y se mostrara la lista. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def help(ctx, cmdhlp='', helpcat=''):
    if(cmdhlp == ''):
        #await ctx.channel.send("Error: Se necesita un comando del que obtener ayuda, para ver los comandos usa `ik!help view` y se mostrara la lista.")
        embed = discord.Embed(
            title="ERROR:",
            description="Se necesita un comando del que obtener ayuda, para ver la lista de comandos usa `ik!help view` y se mostrara la lista. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == 'view'):
        if(helpcat == ''):
            embed = discord.Embed(
                title="Yo que se | Comandos - Categorias <:ik_info:1038408927307640952>",
                description="Categorias de comandos: \n _**Usa**_ `ik!help view <categoria>` _**para ver la categoria**_ \n \n Administración: `ik!help view adm` (4 comandos) \n Diversión: `ik!help view fun` (3 comandos) \n Otros: `ik!help view misc` (5 comandos) \n Funciónes: `ik!help view funct` (2 funciónes) \n \n Hecho Por: Genplat Dev",
                colour=discord.Color.green()
            )
            await ctx.channel.send(embed=embed)
        if(helpcat == "adm"):
            embed = discord.Embed(
                title="Yo que se | Comandos - Administración <:ik_info:1038408927307640952>",
                description="Comandos de `administración`: \n Para ver mas información sobre un comando usa `ik!help <comando>` \n ik!purge <cantidad>: Elimina una cierta cantidad de mensajes \n ik!ban <usuario>: Banea un usuario \n ik!hackban <id>: Banea un usuario por la ID \n ik!banmalicious: Banea usuarios maliciosos de la blacklist \n By Genplat",
                colour=discord.Color.green()
            )
            await ctx.channel.send(embed=embed)
        elif(helpcat == "fun"):
            embed = discord.Embed(
                title="Yo que se | Comandos - Diversión <:ik_info:1038408927307640952>",
                description="Comandos de `diversión`: \n Para ver mas información sobre un comando usa `ik!help <comando>` \n ik!say <texto>: Haz que el bot diga algo \n ik!sayembed <titulo> <descripción>: Haz que el bot diga algo via embed \n ik!roulette <numero>: Gira la ruleta \n ik!serverinfo: Mira la información del server \n ik!ship <member> <member>: Calcula la provavilidad entre dos usuarios \n By Genplat",
                colour=discord.Color.green()
            )
            await ctx.channel.send(embed=embed)
        elif(helpcat == "misc"):
            embed = discord.Embed(
                title="Yo que se | Comandos - Otros <:ik_info:1038408927307640952>",
                description="Comandos de `otros`: \n Para ver mas información sobre un comando usa `ik!help <comando>` \n ik!invite: Invita al bot \n ik!credits: Mira los creditos \n ik!serverinfo: Mira la información del server \n ik!profile <@user>: Mira el perfil del bot de alguien \n ik!premium: ¡Compra premium para obtener ventajas! \n By Genplat",
                colour=discord.Color.green()
            )
            await ctx.channel.send(embed=embed)
        elif(helpcat == "funct"):
            embed = discord.Embed(
                title="Yo que se | Funciónes <:ik_info:1038408927307640952>",
                description="Funciónes del bot: \n Para ver mas información sobre una funcion usa `ik!help <funcion>` \n Welcomer: Envia un mensaje de bienvenida a los miembros nuevos \n Guia: Muestra un mensaje y crea un canal donde enviarlo al unirse a un nuevo servidor (el bot) \n By Genplat",
                colour=discord.Color.green()
            )
            await ctx.channel.send(embed=embed)
        elif(helpcat == ''):
            pass
        else:
            embed = discord.Embed(
                title="ERROR:",
                description="Categoria incorrecta. Usa `ik!help view` para ver las categorias disponibles. <a:ik_cross:1038404494079307776>",
                colour=discord.Color.red()
            )
            await ctx.channel.send(embed=embed)
    elif(cmdhlp == "credits"):
        embed = discord.Embed(
            title="Credits | Help",
            description="Descipción: Muestra los creditos \n Uso: ik!credits",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "sayembed"):
        embed = discord.Embed(
            title="SayEmbed | Help <:ik_info:1038408927307640952>",
            description="Descipción: Envia un mensaje usando embeds (usar parametros con comillas) \n Uso: ik!sayembed <titulo> <descripcion>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "invite"):
        embed = discord.Embed(
            title="Invite | Help <:ik_info:1038408927307640952>",
            description="Descipción: Invita al bot \n Uso: ik!invite",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "say"):
        embed = discord.Embed(
            title="Say | Help <:ik_info:1038408927307640952>",
            description="Descipción: Envia un mensaje usando el bot \n Uso: ik!say <mensaje>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "purge"):
        embed = discord.Embed(
            title="Purge | Help <:ik_info:1038408927307640952>",
            description="Descipción: Borra cierta cantidad de mensajes \n Uso: ik!purge <cantidad>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "ban"):
        embed = discord.Embed(
            title="Ban | Help <:ik_info:1038408927307640952>",
            description="Descipción: Banea a un miembro \n Uso: ik!ban <usuario>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "hackban"):
        embed = discord.Embed(
            title="HackBan | Help <:ik_info:1038408927307640952>",
            description="Descipción: Banea a un usuario que no este en el servidor \n Uso: ik!hackban <id>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "roulette"):
        embed = discord.Embed(
            title="Roulette | Help <:ik_info:1038408927307640952>",
            description="Descipción: Gira la ruleta y mira si tu numero coincide con otro aleatorio de 1 a 100 \n Uso: ik!roulette <numero>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "banmalicious"):
        embed = discord.Embed(
            title="BanMalicious | Help <:ik_info:1038408927307640952>",
            description="Descipción: Banea a los usuarios maliciosos \n Uso: ik!banmalicious",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "welcomer"):
        embed = discord.Embed(
            title="Welcomer | Help",
            description="Descipción: Envia un mensaje de bienvenia por DM cuando un usuario se une al servidor \n Tipo: Función",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "guia"):
        embed = discord.Embed(
            title="Guia | Help",
            description="Descipción: Crea un canal y manda un mensaje de guia cada vez que el bot se une a un servidor al nuevo servidor \n Tipo: Función",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "serverinfo"):
        embed = discord.Embed(
            title="ServerInfo | Help <:ik_info:1038408927307640952>",
            description="Descipción: Muestra la información del servidor \n Uso: ik!serverinfo",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "profile"):
        embed = discord.Embed(
            title="Profile | Help <:ik_info:1038408927307640952>",
            description="Descipción: Muestra la información de un usuario (Perfil de IK), si no hay un miembro se mandara la tuya \n Uso: ik!profile <@member>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "ship"):
        embed = discord.Embed(
            title="Ship | Help <:ik_info:1038408927307640952>",
            description="Descipción: Calcula el porcentaje entre dos miembros \n Uso: ik!ship <usuario> <usuario>",
            colour=discord.Color.green()
        )
        await ctx.channel.send(embed=embed)
    elif(cmdhlp == "premium"):
        embed = discord.Embed(
            title="Premium | Help <:ik_premium:1043865972286685214>",
            description="Descipción: ¡Obten IKNetwork Premium! ¡Obten ventajas exclusivas! \n Uso: ik!premium",
            colour=discord.Color.magenta()
        )
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title="ERROR:",
            description="Comando invalido, para ver la lista de comandos usa `ik!help view` y se mostrara la lista. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
        #await ctx.channel.send("Comandos: \n \n ik!invite: Invia al bot \n ik!say: Envia un mensaje usando el bot \n ik!sayembed: Envia un mensaje en embed usando el bot \n \n \n By: Genplat")

@IKNetwork.command()
async def invite(ctx):
    embed = discord.Embed(
        title="Invite Bot:",
        description="Invita al bot del cp (Ya ni se que poner): \n AQUI TU LINK",
        colour=discord.Color.gold()
    )
    await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def credits(ctx):
    embed = discord.Embed(
        title="yo que se | Creditos <:ik_info:1038408927307640952>",
        description="Hecho por: Genplat \n \n Server oficial: https://discord.gg/TULINK \n Ver comandos: `ik!help view` \n ¡Gracias por usar! \n \n Hecho Por: Genplat Dev",
        colour=discord.Color.purple()
    )
    await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def say(ctx, *,message='', messagemore=''):
    if(message != ''):
        if(messagemore != ''):
            await ctx.channel.send("Error: Tienes que poner comillas para mas de un mensaje")
        else:
            await ctx.channel.send(message)
    else:
        await ctx.channel.send("Error: Se necesita algo que decir")

@commands.has_permissions(administrator=True)
@IKNetwork.command()
async def purge(ctx, number: int):
    await ctx.channel.purge(limit=number)
    embed = discord.Embed(
        title="Purge | Finish",
        description="Listo! Mensajes eliminados. <a:ik_check:1038404454153736273>",
        colour=discord.Color.green()
    )
    await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def sayembed(ctx, title: str, description: str):
    embed = discord.Embed(
        title=title,
        description=description,
        colour=discord.Color.green()
        )

    await ctx.channel.send(embed=embed)

@IKNetwork.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed = discord.Embed(
            title="Ban | Yo que se",
            description=f"Se ha baneado al usuario con exito. <a:ik_check:1038404454153736273>",
            colour=discord.Color.green()
    )
        
    await ctx.channel.send(embed=embed)

@IKNetwork.command()
@commands.has_permissions(ban_members=True)
async def hackban(ctx, userID:int):
    await ctx.guild.ban(discord.Object(id=userID))
    embed = discord.Embed(
        title="HackBan | Yo que se",
        description=f"Se ha hackbaneado baneado al usuario con exito. <a:ik_check:1038404454153736273>",
        colour=discord.Color.green()
    )
    await ctx.channel.send(embed=embed)

@IKNetwork.command()
@commands.has_permissions(ban_members=True)
async def banmalicious(ctx):
    embed = discord.Embed(
        title="BanMalicious | IK Network",
        description=f"Se estan baneando los usuarios maliciosos... <a:ik_loading:1038401625460576277>",
        colour=discord.Color.teal()
    )
    embedprocban = await ctx.channel.send(embed=embed)
    embedprocbanid = embedprocban.id
        # Aquí metes a tus usuarios para banearlos
        await ctx.guild.ban(discord.Object(id=ID DEL HDP QUE QUERAS METER EN BLACKLIST))
    await embedprocban.delete()
    embed = discord.Embed(
        title="BanMalicious | IK Network",
        description=f"Se han baneado los usuarios maliciosos con exito. <a:ik_check:1038404454153736273>",
        colour=discord.Color.green()
    )
    await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def roulette(ctx, eleccion:int):
    numero = randint(1, 300)
    if(eleccion == ''):
        embed = discord.Embed(
            title="ERROR:",
            description=f"Se necesita un numero para apostar. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
    else:
        if(eleccion == numero):
            embed = discord.Embed(
                title="Ruleta | yo que se",
                description=f"¡Felicidades! Has ganado la ruleta. <a:ik_check:1038404454153736273>",
                colour=discord.Color.green()
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Ruleta | yo que se",
                description=f"Has fallado, mas suerte la proxima vez. <a:ik_cross:1038404494079307776>",
                colour=discord.Color.red()
            )
            await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def guildsview(ctx):
    if(ctx.author.id == TU_ID):
        activeservers = IKNetwork.guilds
        embed = discord.Embed(
            title="Servidores | yo que se Administration <:ik_info:1038408927307640952>",
            description=f"Servidores donde esta el bot:",
            colour=discord.Color.green()
        )

        for guild in activeservers:
            #await ctx.send(guild.name)
            #print(guild.name)
            #print(activeservers)
        #await ctx.channel.send(f"{activeservers}")
            embed = embed.add_field(name="Server: ",value=(f"{guild.name}"))
        embed = embed.set_footer(text="By Genplat Dev")
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title="ERROR:",
            description="NO ESTAS AUTORIZADO PARA USAR ESTE COMANDO. <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def serverinfo(ctx):
    channels = len(ctx.guild.channels)
    embed = discord.Embed(title = f"Info De {ctx.guild.name} <:ik_info:1038408927307640952> | yo que se", description = "Información del server", color = discord.Colour.purple())
    embed.add_field(name = '🆔ID Del Server', value = f"{ctx.guild.id}", inline = True)
    embed.add_field(name = '📆Creado El', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
    embed.add_field(name = '👑Dueño', value = f"{ctx.guild.owner}", inline = True)
    embed.add_field(name = '👥Miembros', value = f'{ctx.guild.member_count} Members', inline = True)
    embed.add_field(name = '💬Canales', value = f'{channels} Canales', inline = True)
    embed.set_footer(text = f"#yo que se | Info De {ctx.guild.name}")    
    await ctx.send(embed=embed)

@IKNetwork.command()
async def profile(ctx, member : discord.Member=None):
    autor = str()
    if member == None:
        autor = str(ctx.author.id)
    blacklist = # AQUI TU BLACKLIST
    pana = # Aqui podes poner a tus panas o yo que se
    admins = # Aquí a tus admins
    gf = # Tu novia (Si es que tienes, edater)
    owner = # Tu ID
    botid = # ID Del bot
    premium = # Tus usuarios premium
    if(member == None):
        if(autor in owner):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{ctx.author.id}> \n Insigneas: <:ik_crown:1038538799522795622><:ik_premium:1043865972286685214> \n Tipo: Owner \n ID: {autor}",
                colour=discord.Color.gold()
            )
            await ctx.channel.send(embed=embed)
        elif(autor in pana):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{ctx.author.id}> \n Insigneas: <:ik_shield:1038539891031687198><:ik_premium:1043865972286685214> \n Tipo: Pana \n ID: {autor}",
                colour=discord.Color.purple()
            )
            await ctx.channel.send(embed=embed)
        elif(autor in admin):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{ctx.author.id}> \n Insigneas: <:ik_staff:1038539939761098762><:ik_premium:1043865972286685214> \n Tipo: Admin \n ID: {autor}",
                colour=discord.Color.teal()
            )
            await ctx.channel.send(embed=embed)
        elif(autor in gf):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{ctx.author.id}> \n Insigneas: <:ik_sword:1038539839424958555><:ik_premium:1043865972286685214> \n Tipo: gf \n ID: {autor}",
                colour=discord.Color.magenta()
            )
            await ctx.channel.send(embed=embed)
        elif(autor in blacklist):
            embed = discord.Embed(
                title="USUARIO MALICIOSO | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{ctx.author.id}> \n Tipo: USUARIO MALICIOSO \n ID: {autor}",
                colour=discord.Color.red()
            )
            await ctx.channel.send(embed=embed)
        elif(autor in botid):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{ctx.author.id}> \n Tipo: Bot Oficial<:ik_bot:1038541221548798013> \n Versión: 1.0",
                colour=discord.Color.dark_grey()
            )
            await ctx.channel.send(embed=embed)
        elif(memberid in premium):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Insigneas: <:ik_premium:1043865972286685214> \n Tipo: Usuario \n ID: {memberid}",
                colour=discord.Color.blurple()
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Profile | IK Network <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{ctx.author.id}> \n Insigneas: \n Tipo: Usuario \n ID: {autor}",
                colour=discord.Color.blue()
            )
            await ctx.channel.send(embed=embed)
    else:
        memberid = str(member.id)
        if(memberid in owner):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Insigneas: <:ik_crown:1038538799522795622><:ik_premium:1043865972286685214> \n Tipo: Dueño \n ID: {memberid}",
                colour=discord.Color.gold()
            )
            await ctx.channel.send(embed=embed)
        elif(memberid in pana):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Insigneas: <:ik_shield:1038539891031687198><:ik_premium:1043865972286685214> \n Tipo: Pana \n ID: {memberid}",
                colour=discord.Color.purple()
            )
            await ctx.channel.send(embed=embed)
        elif(memberid in admin):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Insigneas: <:ik_staff:1038539939761098762><:ik_premium:1043865972286685214> \n Tipo: admin \n ID: {memberid}",
                colour=discord.Color.teal()
            )
            await ctx.channel.send(embed=embed)
        elif(memberid in gf):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Insigneas: <:ik_sword:1038539839424958555><:ik_premium:1043865972286685214> \n Tipo: gf \n ID: {memberid}",
                colour=discord.Color.magenta()
            )
            await ctx.channel.send(embed=embed)
        elif(memberid in enemies):
            embed = discord.Embed(
                title="USUARIO MALICIOSO | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Tipo: USUARIO MALICIOSO \n ID: {memberid}",
                colour=discord.Color.red()
            )
            await ctx.channel.send(embed=embed)
        elif(memberid in botid):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Tipo: Bot Oficial<:ik_bot:1038541221548798013> \n Versión: 1.0",
                colour=discord.Color.dark_grey()
            )
            await ctx.channel.send(embed=embed)
        elif(memberid in premium):
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Insigneas: <:ik_premium:1043865972286685214> \n Tipo: Usuario \n ID: {memberid}",
                colour=discord.Color.blurple()
            )
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Profile | yo que se <:ik_info:1038408927307640952>",
                description=f"Nombre: <@{memberid}> \n Insigneas: \n Tipo: Usuario \n ID: {memberid}",
                colour=discord.Color.blue()
            )
            await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def ship(ctx, member : discord.Member=None, member2 : discord.Member=None):
    numero = randint(1, 100)
    if(member == None):
        embed = discord.Embed(
            title="ERROR:",
            description=f"Se necesitan dos miembros para calcular la provavilidad <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
    elif(member2 == None):
        embed = discord.Embed(
            title="ERROR:",
            description=f"Se necesitan dos miembros para calcular la provavilidad <a:ik_cross:1038404494079307776>",
            colour=discord.Color.red()
        )
        await ctx.channel.send(embed=embed)
    else:
        antifakemembers = member.id
        if(member.id != '1037096372207374446'):
            if(numero == 100):
                embed = discord.Embed(
                    title="Ship | yo que se",
                    description=f"Las probabilidades entre {member} y {member2} son... ¡INCREIBLE! un 100%, mis mejores deseos. <a:ik_check:1038404454153736273>",
                    colour=discord.Color.green()
                )
                await ctx.channel.send(embed=embed)
            elif(99 >= numero):
                if(numero >= 50):
                    embed = discord.Embed(
                        title="Ship | yo que se",
                        description=f"Las probabilidades entre {member} y {member2} son... un {numero}%, hacen buena pareja. <a:ik_check:1038404454153736273>",
                        colour=discord.Color.green()
                    )
                    await ctx.channel.send(embed=embed)
                else: pass
            elif(49 <= numero):
                if(numero >= 25):
                    embed = discord.Embed(
                        title="Ship | yo que se",
                        description=f"Las probabilidades entre {member} y {member2} son... un {numero}%, mejor sean solo mejores amigos, ¿ok?. <a:ik_cross:1038404494079307776>",
                        colour=discord.Color.red()
                    )
                    await ctx.channel.send(embed=embed)
                else: pass
            elif(numero <= 24):
                if(numero >= 2):
                    embed = discord.Embed(
                        title="Ship | yo que se",
                        description=f"Las probabilidades entre {member} y {member2} son... un {numero}%, No lo veo yo muy claro... <a:ik_cross:1038404494079307776>",
                        colour=discord.Color.red()
                    )
                    await ctx.channel.send(embed=embed)
                else: pass
            elif(numero == 1):
                embed = discord.Embed(
                    title="Ship | yo que se",
                    description=f"Las probabilidades entre {member} y {member2} son... un {numero}%, Claramente, mejor dejense uno al otro con su vida... <a:ik_cross:1038404494079307776>",
                    colour=discord.Color.red()
                )
                await ctx.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Ship | yo que se",
                    description=f"Las probabilidades entre {member} y {member2} son... un... un... nada, no lo he poido comprobar... Igualmente, que les vaya bien <a:ik_cross:1038404494079307776>",
                    colour=discord.Color.red()
                )
                await ctx.channel.send(embed=embed)

@IKNetwork.command()
async def premium(ctx):
    embed = discord.Embed(
        title="Premium | yo que se<:ik_premium:1043865972286685214>",
        description=f"Para obtener pornhub premium y tener una insignea especial en tu `ik!profile` y mas ventajas que vendran mas adelante, contacta con `TU TAG, TU METODO DE PAGO O LA MIERDA QUE SEA`, el precio actual es de 5$ y es un unico pago, en ningun momento perderas tus ventajas, aprobecha antes de que se añadan mas cosas y suban los precios!!!",
        colour=discord.Color.gold()
    )
    await ctx.channel.send(embed=embed)


IKNetwork.run(token)
