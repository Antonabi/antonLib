class createdUser():
    def __init__(self, userData):
        self.logId = userData["logId"]
        self.authToken = userData["authToken"]
        self.params = userData["params"]
        self.name = self.params["name"]
        self.funnelId = self.params["funnelId"]
        self.avatar = self.params["avatar"]
        self.grade = self.params["grade"]
        self.subject = self.params["subject"]
        self.howKnowAbout = self.params["howKnowAbout"]
        self.guiLanguage = self.params["guiLanguage"]
        self.deviceSrc = self.params["deviceSrc"]

class notLoggedInUser():
    def __init__(self, userData):
        self.uniqueName = userData["uniqName"]
        self.hasPhone = userData["recoveryOptions"]["hasPhone"]
        self.hasEMail = userData["recoveryOptions"]["hasEMail"]
        self.isTeacher = userData["recoveryOptions"]["hasGroupTeacher"]
