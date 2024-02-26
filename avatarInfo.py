class avatarInfo():
    def __init__(self, avatarInfoData):
        self.created = avatarInfoData["created"]
        self.likes = avatarInfoData["likes"]
        self.isFavourite = avatarInfoData["isFavourite"]