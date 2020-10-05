import discord
from discord.ext import tasks

# Import files
from ThirdpartyAPI.earthquake import earthquake
from embed import createembed
import Config.config as config

# Discord related
(discord_bot_token,
 channel_id_earthquake) = config.discordconfig()

client = discord.Client()

# Discord Connect


@ client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# region Earthquake Early Warning


@ tasks.loop(seconds=1)
async def earthquakealert():
    earthquakeinfo = earthquake()
    channel = client.get_channel(int(channel_id_earthquake))
    embed = None

    try:
        if earthquakeinfo['Status']['Code'] != '00':
            print('In')
            return

        if (earthquakeinfo['Title']['String'] == '緊急地震速報（警報）'
                and earthquakeinfo['MaxIntensity']['String'] == ('5弱'
                                                                 or '5強'
                                                                 or '6弱'
                                                                 or '6強'
                                                                 or '7')):
            embed = createembed(6, '', '', '', '', earthquakeinfo)
            await channel.send(embed=embed)
    except Exception as e:
        print('Error: ')
        print(e)
        pass

# endregion

# Loop
earthquakealert.start()

client.run(discord_bot_token)
