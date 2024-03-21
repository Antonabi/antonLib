from datetime import datetime

class pixelPaintInfo():
    def __init__(self, pixelPaintInfoData):
        self.uid = pixelPaintInfoData["uid"]
        self.created = datetime.fromisoformat(pixelPaintInfoData["created"])
        self.likes = pixelPaintInfoData["likes"]
        self.idFavourite = pixelPaintInfoData["idFavourite"]
        self.isFlagged = pixelPaintInfoData["isFlagged"]
        self.creatorName = pixelPaintInfoData["userName"]
        self.creatorAvatar = pixelPaintInfoData["userAvatar"]
        self.isPublic = pixelPaintInfoData["isPublic"]