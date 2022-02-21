
def get_token():
    with open("token.txt", 'r') as tokenFile:
        return tokenFile.readline()