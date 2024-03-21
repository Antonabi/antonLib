from datetime import datetime

class avatarInfo():
    def __init__(self, avatarInfoData):
        self.uid = avatarInfoData["uid"]
        self.created = datetime.fromisoformat(avatarInfoData["created"])
        self.likes = avatarInfoData["likes"]
        self.isFavourite = avatarInfoData["isFavourite"]