class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    def setpassword(self,password):
        self.__password = password

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        return self._post.append(newpost)

shashi = Instagram('shashi','1234567')

print(shashi.username)
print(shashi.getpassword())
print(shashi.accesspost)

shashi.username = 'shashi_123'
print(shashi.username)

shashi.setpassword = 'shashi123'
print(shashi.getpassword())

shashi.accesspost = 'python intro'
shashi.accesspost = 'string'
shashi.accesspost = 'project'
print(shashi.accesspost)