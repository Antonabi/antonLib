class avatarInfo(): #class/object for the avatar superstar avatar info
    def __init__(self, avatarInfoData):
        self.created = avatarInfoData["created"] #when it was created
        self.likes = avatarInfoData["likes"]
        self.isFavourite = avatarInfoData["isFavourite"] #for some reason this exists but i dont know why, because only pictures in pixel paint can be favourited (as far as i know)
