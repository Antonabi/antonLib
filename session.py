import antonLib
from . import avatarInfo
from . import pixelPaintInfo
from . import exceptions
from datetime import datetime

class session():
    def __init__(self, sessionData):
        self.loginCode = sessionData["loginCode"]
        self.logId = sessionData["logId"]
        self.authToken = sessionData["authToken"]
        self.displayName = sessionData["displayName"]
        self.avatar = sessionData["avatar"]

    def changeUniqueName(self, name):

        data = {
        "params": {
            "logId": self.logId,
            "uniqName": name
        }
        }
        antonLib.defReq(url="https://f-apis-db.anton.app/?p=user/setUniqName/set", data=data, path="/../server-apis-db2/apis/user/setUniqName/set", authToken=self.authToken, logId=self.logId)

    def likePixelPaint(self, uid):

        data = {
            "params": {
                "uid": uid,
                "isLiked": True
            }
            }
        antonLib.defReq(url="https://d-apis-db.anton.app/?p=pixelPaint/setLiked/set", data=data, path="/../server-apis-db2/apis/pixelPaint/setLiked/set", authToken=self.authToken, logId=self.logId)
    
    def likeAvatarSuperstar(self, uid):
        
        data = {
            "params": {
                "uid": uid,
                "isLiked": True
            }
            }

        antonLib.defReq(url="https://b-apis-db.anton.app/?p=avatarSuperstar/like/like", data=data, path="/../server-apis-db2/apis/avatarSuperstar/like/like", authToken=self.authToken, logId=self.logId)
    
    def dislikePixelPaint(self, uid):
        
        data = {
            "params": {
                "uid": uid,
                "isLiked": False
            }
            }
        antonLib.defReq(url="https://d-apis-db.anton.app/?p=pixelPaint/setLiked/set", data=data, path="/../server-apis-db2/apis/pixelPaint/setLiked/set", authToken=self.authToken, logId=self.logId)
    
    def dislikeAvatarSuperstar(self, uid):
        data = {
            "params": {
                "uid": uid,
                "isLiked": False
            }
            }

        antonLib.defReq(url="https://b-apis-db.anton.app/?p=avatarSuperstar/like/like", data=data, path="/../server-apis-db2/apis/avatarSuperstar/like/like", authToken=self.authToken, logId=self.logId)
    
    def publishAvatarSuperstar(self, avatarData):
        data = {
            "params": {
                "avatar": avatarData
            }
        }

        response = antonLib.defReq(url="https://f-apis-db.anton.app/?p=avatarSuperstar/publish/publish", path="/../server-apis-db2/apis/avatarSuperstar/publish/publish", authToken=self.authToken, data=data, logId=self.logId)
        return response["uid"]
    
    def publishPixelPaintImage(self, svg, uid): #this thing is buggy and does not work most of the time (you have to create the image manually, then get the uid and paste it here i think)
        data = {
            "params": {
                "svg": svg,
                "uid": uid,
            }
        }

        response = antonLib.defReq(url="https://e-apis-db.anton.app/../server-apis-db2/apis/pixelPaint/publish/publish", path="/../server-apis-db2/apis/pixelPaint/publish/publish", authToken=self.authToken, logId=self.logId, data=data)
        return uid

    def getAvatarData(self, uid): #is really buggy
        data = {
            "params": {
                "uids": [
                    uid
                ],
            }
        }

        response = antonLib.defReq(url="https://e-apis-db.anton.app/?p=pixelPaint/getMetaData/get", path="/../server-apis-db2/apis/avatarSuperstar/getMetaData/get", authToken=self.authToken, logId=self.logId, data=data)
        if len(response["items"]) < 1:
            raise exceptions.avatarNonexistent
        else:
            return avatarInfo.avatarInfo(response["items"][0])
    
    def getPixelPaintData(self, uid):
        data = {
            "params": {
                "imageIds": [
                    uid
                ],
            }
        }

        response = antonLib.defReq(url="https://e-apis-db.anton.app/?p=pixelPaint/getMetaData/get", path="/../server-apis-db2/apis/pixelPaint/getMetaData/get", authToken=self.authToken, logId=self.logId, data=data)
        if len(response["images"]) < 1:
            raise exceptions.imageNonexistent
        else:
            return pixelPaintInfo.pixelPaintInfo(response["images"][0])