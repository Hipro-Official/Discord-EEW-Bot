import discord


def createembed(earthquakeinfo):
    file, embed = None
    if earthquakeinfo['MaxIntensity']['String'] == ('5弱' or
                                                    '5強' or
                                                    '6弱' or
                                                    '6強' or
                                                    '7'):
        discord.Embed(title='緊急地震速報（震度5弱）', color=0xFF0000)
        embed.add_field(
            name='震源',
            value=earthquakeinfo['Hypocenter']['Name'])
        embed.add_field(
            name='震源の深さ',
            value=earthquakeinfo['Hypocenter']['Location']['String'])
        embed.add_field(
            name='マグニチュード',
            value=earthquakeinfo['Hyprocenter']['Magnitude']['String'])
        embed.set_thumbnail(url='https://github.com/Hipro-Official/Discord-EEW-Bot/blob/master/EEW_pic/5m.png?raw=true')
        return embed
    elif earthquakeinfo['MaxIntensity']['String'] == '5強':
        discord.Embed(title='緊急地震速報（震度5強）', color=0xFF0000)
        embed.add_field(
            name='震源',
            value=earthquakeinfo['Hypocenter']['Name'])
        embed.add_field(
            name='震源の深さ',
            value=earthquakeinfo['Hypocenter']['Location']['String'])
        embed.add_field(
            name='マグニチュード',
            value=earthquakeinfo['Hyprocenter']['Magnitude']['String'])
        embed.set_thumbnail(url='https://github.com/Hipro-Official/Discord-EEW-Bot/blob/master/EEW_pic/5p.png?raw=true')
        return embed
    elif earthquakeinfo['MaxIntensity']['String'] == '6弱':
        discord.Embed(title='緊急地震速報（震度6弱）', color=0xFF0000)
        embed.add_field(
            name='震源',
            value=earthquakeinfo['Hypocenter']['Name'])
        embed.add_field(
            name='震源の深さ',
            value=earthquakeinfo['Hypocenter']['Location']['String'])
        embed.add_field(
            name='マグニチュード',
            value=earthquakeinfo['Hyprocenter']['Magnitude']['String'])
        embed.set_thumbnail(url='https://github.com/Hipro-Official/Discord-EEW-Bot/blob/master/EEW_pic/6m.png?raw=true')
        return embed
    elif earthquakeinfo['MaxIntensity']['String'] == '6強':
        discord.Embed(title='緊急地震速報（震度6強）', color=0xFF0000)
        embed.add_field(
            name='震源',
            value=earthquakeinfo['Hypocenter']['Name'])
        embed.add_field(
            name='震源の深さ',
            value=earthquakeinfo['Hypocenter']['Location']['String'])
        embed.add_field(
            name='マグニチュード',
            value=earthquakeinfo['Hyprocenter']['Magnitude']['String'])
        embed.set_thumbnail(url='https://github.com/Hipro-Official/Discord-EEW-Bot/blob/master/EEW_pic/6p.png?raw=true')
        return embed
    elif earthquakeinfo['MaxIntensity']['String'] == '7':
        discord.Embed(title='緊急地震速報（震度7）', color=0xFF0000)
        embed.add_field(
            name='震源',
            value=earthquakeinfo['Hypocenter']['Name'])
        embed.add_field(
            name='震源の深さ',
            value=earthquakeinfo['Hypocenter']['Location']['String'])
        embed.add_field(
            name='マグニチュード',
            value=earthquakeinfo['Hyprocenter']['Magnitude']['String'])
        embed.set_thumbnail(url='https://github.com/Hipro-Official/Discord-EEW-Bot/blob/master/EEW_pic/7.png?raw=true')
        return embed
