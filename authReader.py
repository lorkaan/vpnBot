
class Auth:

    def __init__(self, user, passwd):
        if isinstance(user, str) and isinstance(passwd, str):
            self.user = user
            self.passwd = passwd
        else:
            raise ValueError(f'user: {type(user)}, passwd: {type(passwd)}')

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.passwd

    def __repr__(self):
        return (user, passwd)

    def __str__(self):
        return f'{self.user}:{self.passwd}'

def createAuth(token, sep=":"):
    tokenList = token.split(sep)
    return Auth(tokenList[0], tokenList[1])

def readAuthFromFile(filename, num_lines=None):
    auths = []
    with open(filename, 'r') as f:
        if isinstance(num_lines, int):
            # take the first number of lines
            for i in range(num_lines):
                auths.append(createAuth(f.readline()))
        else:
            for line in f.readlines():
                auth.append(createAuth(line))
    return auths