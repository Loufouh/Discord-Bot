
def get_token():
    with open("bot.token", 'r') as tokenFile:
        return tokenFile.readline()