import os
import django


def discord_message_process_with_channel(message_text, channel_name):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jbsl3.settings')
    django.setup()
    import discord
    from discord.ext import commands
    if os.path.exists('local.py'):
        from local import DISCORD_BOT_TOKEN, GUILD_ID
        guild_id = GUILD_ID
        token = DISCORD_BOT_TOKEN
    else:
        guild_id = os.getenv('GUILD_ID')
        token = os.getenv('DISCORD_BOT_TOKEN')
    
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='/', intents=intents)
    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(guild_id))
        category = discord.utils.get(guild.categories, name='進行中リーグ')
        target_channel = None
        print(category.text_channels)
        for channel in category.text_channels:
            if channel.name == channel_name:
                target_channel = channel
        if target_channel is not None:
            await target_channel.send(message_text)
        await bot.close()

    bot.run(token)


def discord_message_process(message_text):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jbsl3.settings')
    django.setup()
    import discord
    from discord.ext import commands
    if os.path.exists('local.py'):
        from local import DISCORD_BOT_TOKEN, NOTIFY_ID
        token = DISCORD_BOT_TOKEN
        channel_id = NOTIFY_ID
    else:
        token = os.getenv('DISCORD_BOT_TOKEN')
        channel_id = os.getenv('NOTIFY_ID')
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    @bot.event
    async def on_ready():
        channel = await bot.fetch_channel(channel_id)
        await channel.send(message_text)
        await bot.close()

    bot.run(token)


def league_role_total():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jbsl3.settings')
    django.setup()
    import discord
    from discord.ext import commands
    if os.path.exists('local.py'):
        from local import DISCORD_BOT_TOKEN, GUILD_ID
        guild_id = GUILD_ID
        token = DISCORD_BOT_TOKEN
    else:
        guild_id = os.getenv('GUILD_ID')
        token = os.getenv('DISCORD_BOT_TOKEN')
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    from app.models import League

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(guild_id))
        category = discord.utils.get(guild.categories, name='進行中リーグ')
        channel_names = []
        role_names = []
        for channel in category.channels:
            channel_names.append(channel.name)
        for role in guild.roles:
            role_names.append(role.name)
        for league in League.objects.filter(isLive=True):
            if not league.name in channel_names:
                await category.create_text_channel(league.name)
            if not league.name in role_names:
                colour = discord.Colour.default()
                col_dict = {}
                col_dict['lightblue'] = discord.Colour.blue()
                col_dict['lightgreen'] = discord.Colour.green()
                col_dict['lightsalmon'] = discord.Colour.orange()
                col_dict['lightpink'] = discord.Colour.red()
                col_dict['#FFCCFF'] = discord.Colour.purple()
                col_dict['lightyellow'] = discord.Colour.gold()
                if league.color in col_dict:
                    colour = col_dict[league.color]
                await guild.create_role(name=league.name, colour=colour)

            current_role = discord.utils.get(guild.roles, name=league.name)
            print(current_role)

            for player in league.player.all():
                print(player.discordID)
                member = guild.get_member(int(player.discordID))
                await member.add_roles(current_role)
            print(member)

        await bot.close()

    bot.run(token)


def league_create(league_name):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jbsl3.settings')
    django.setup()
    import discord
    from discord.ext import commands
    if os.path.exists('local.py'):
        from local import DISCORD_BOT_TOKEN, GUILD_ID
        guild_id = GUILD_ID
        token = DISCORD_BOT_TOKEN
    else:
        guild_id = os.getenv('GUILD_ID')
        token = os.getenv('DISCORD_BOT_TOKEN')
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(guild_id))
        category = discord.utils.get(guild.categories, name='進行中リーグ')
        channels = category.channels
        print(channels)
        exist = False
        for channel in channels:
            print(channel.name)
            if channel.name == league_name:
                exist = True
        if not exist:
            await category.create_text_channel(league_name)
        await bot.close()

    bot.run(token)


def role_erase():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jbsl3.settings')
    django.setup()
    import discord
    from discord.ext import commands
    if os.path.exists('local.py'):
        from local import DISCORD_BOT_TOKEN, GUILD_ID
        guild_id = GUILD_ID
        token = DISCORD_BOT_TOKEN
    else:
        guild_id = os.getenv('GUILD_ID')
        token = os.getenv('DISCORD_BOT_TOKEN')
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(guild_id))
        members = guild.members
        for member in members:
            print(member.name)
            role_names = ["J1", "J2", "J3", "J1本戦", "J2本戦", "J3本戦"]
            for role_name in role_names:
                role = discord.utils.get(guild.roles, name=role_name)
                await member.remove_roles(role)
        await bot.close()

    bot.run(token)


def role_create(role_name, color_string):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jbsl3.settings')
    django.setup()
    import discord
    from discord.ext import commands
    if os.path.exists('local.py'):
        from local import DISCORD_BOT_TOKEN, GUILD_ID
        guild_id = GUILD_ID
        token = DISCORD_BOT_TOKEN
    else:
        guild_id = os.getenv('GUILD_ID')
        token = os.getenv('DISCORD_BOT_TOKEN')
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(guild_id))
        colour = discord.Colour.default()
        col_dict = {}
        col_dict['lightblue'] = discord.Colour.blue()
        col_dict['lightgreen'] = discord.Colour.green()
        col_dict['lightsalmon'] = discord.Colour.orange()
        col_dict['lightpink'] = discord.Colour.red()
        col_dict['#FFCCFF'] = discord.Colour.purple()
        col_dict['lightyellow'] = discord.Colour.gold()
        if color_string in col_dict:
            colour = col_dict[color_string]
        await guild.create_role(name=role_name, colour=colour)
        await bot.close()

    bot.run(token)


def role_add(ID, role_name):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jbsl3.settings')
    django.setup()
    import discord
    from discord.ext import commands
    if os.path.exists('local.py'):
        from local import DISCORD_BOT_TOKEN, GUILD_ID
        guild_id = GUILD_ID
        token = DISCORD_BOT_TOKEN
    else:
        guild_id = os.getenv('GUILD_ID')
        token = os.getenv('DISCORD_BOT_TOKEN')
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(guild_id))
        member = guild.get_member(ID)
        role = discord.utils.get(guild.roles, name=role_name)
        print(member)
        print(role)
        await member.add_roles(role)
        await bot.close()

    bot.run(token)


if __name__ == '__main__':
    print('utils manual test')
    # league_create('秘密の部屋')
    # league_role_total()