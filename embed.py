import discord


def createembed(earthquakeinfo):
    file, embed = None
    if earthquakeinfo['MaxIntensity']['String'] == ('5弱' or
                                                    '5強' or
                                                    '6弱' or
                                                    '6強' or
                                                    '7'):
        file = discord.File('EEW_pic/5m.png', filename='image.png')
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
        embed.set_thumbnail(url='attachment://image.png')
        return file, embed
    elif earthquakeinfo['MaxIntensity']['String'] == '5強':
        file = discord.File('EEW_pic/5p.png', filename='image.png')
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
        embed.set_thumbnail(url='attachment://image.png')
        return file, embed
    elif earthquakeinfo['MaxIntensity']['String'] == '6弱':
        file = discord.File('EEW_pic/6m.png', filename='image.png')
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
        embed.set_thumbnail(url='attachment://image.png')
        return file, embed
    elif earthquakeinfo['MaxIntensity']['String'] == '6強':
        file = discord.File('EEW_pic/6p.png', filename='image.png')
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
        embed.set_thumbnail(url='attachment://image.png')
        return file, embed
    elif earthquakeinfo['MaxIntensity']['String'] == '7':
        file = discord.File('EEW_pic/7.png', filename='image.png')
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
        embed.set_thumbnail(url='attachment://image.png')
        return file, embed
