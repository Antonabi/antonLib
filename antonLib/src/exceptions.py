class wrongLoginCode(Exception):
    def __init__(self, message=""):
        self.message = "Your login code is wrong. Check if you have typed it right."
        super().__init__(self.message)
    pass

class wrongLogId(Exception):
    def __init__(self, message=""):
        self.message = "Your logId is wrong. Check if you have typed it right."
        super().__init__(self.message)
    pass

class authError(Exception):
    def __init__(self, message=""):
        self.message = "You are not authenticated. This error shouldn't be able to pop up, because before you can even do something that you need to be authenticated for you need to log in. This is an error on my side."
        super().__init__(self.message)
    pass

class unavailableName(Exception):
    def __init__(self, message=""):
        self.message = "The unique name you chose is already taken. (Or unavailable)"
        super().__init__(self.message)
    pass

class uidTaken(Exception):
    def __init__(self, message=""):
        self.message = "The uid of your pixel paint image is already taken (published). Maybe you have published it already? \n\n(If you tried, no you cant take bruh. Bruh is MINE and it will be FOREVER)"
        super().__init__(self.message)
    pass

class avatarNonexistent(Exception):
    def __init__(self, message=""):
        self.message = "The avatar you tried to get info from doesnt exist. Check if youve typed it right."
        super().__init__(self.message)
    pass

class imageNonexistent(Exception):
    def __init__(self, message=""):
        self.message = "The pixel paint image you tried to get info from doesnt exist. Check if youve typed it right."
        super().__init__(self.message)
    pass

class unknownException(Exception):
    def __init__(self, message=""):
        self.message = "You got an exception that i havn't covered yet. (This shouldnt normally happen. If you get this error, please make an issue in the github repo: https://github.com/Antonabi/antonLib)"
        super().__init__(self.message)
    pass
