import os

# region Global Variables
# DEBUG = 0, RELEASE = 1
currentMode = 0

# For earthquake API
earthquake_endpoint = 'https://api.iedred7584.com/eew/json/'
# endregion

# region Functions


def discordconfig():
    if currentMode == 0:
        discord_bot_token = os.environ.get('DISCORD_BOT_TOKEN_DEBUG')
        channel_id_earthquake = os.environ.get('EARTHQUAKE_CHANNEL_DEBUG')
        return discord_bot_token, channel_id_earthquake
    else:
        discord_bot_token = os.environ.get('DISCORD_BOT_TOKEN')
        channel_id_earthquake = os.environ.get('EARTHQUAKE_CHANNEL')
        return discord_bot_token, channel_id_earthquake
# endregion
