
def get_token():
    with open("token", 'r') as tokenFile:
        return tokenFile.readline()
