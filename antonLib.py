import requests
import json
import random
import string
from . import session
from . import createdUser
from . import exceptions

#global vars
debug = False

headers = {
    "Host": "d-apis-db.anton.app",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://anton.app",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
}

def defReq(url, data, authToken, path=None, logId=None): #the default request
    defData = {
        "deviceLogId": "D-2V4Z-aUdJ9leOB2RDiXu8jR0N9Hfefaz",
        "isDebug": False,
        "useAuthToken": True,
        "authToken": authToken
    }
    data = {**defData, **data}

    if logId != None:
        data["logId"] = logId
    if path != None:
        data["path"] = path

    response = requests.post(url, headers=headers, data=json.dumps(data))
    checkResponse(response)
    responseObj = json.loads(response.text)
    return responseObj

def getRandomString(length): #generates a random string with letters of a specific length
    letters = string.ascii_lowercase
    resultStr = ''.join(random.choice(letters) for i in range(length))
    return(resultStr)

def checkResponse(response): #checks the response to not contain an error (this code is als and i will update it)
    try:
        responseObj = json.loads(response.text)
    except:
        raise Exception(f"Something went completely wrong. Response: {response.text}, ResponseCode: {response.status_code}")
    responseStatusText = "ok"
    responseStatusError = "false"
    if "status" in responseObj:
        responseStatusText =  responseObj["status"]

    if "message" in responseObj:
        responseMessage =  responseObj["message"]

    if "error" in responseObj:
        responseStatusError =  responseObj["error"]

    if debug == True:
        print("\033[1mDebug:\033[0m")
        print("---------------------")
        print(f"stutusCode: {response.status_code}")
        print(f"responseStatusText: {responseStatusText}")
        print(f"responseText: {response.text}")
        print("---------------------")

    if response.status_code != 200 or responseStatusText != "ok" or responseStatusError == "true" or responseStatusError == True:
        if "status" in responseObj:
            checkError(response.status_code, responseStatusText)
        if "message" in responseObj:
            checkError(response.status_code, responseMessage)

def checkError(statusCode, message):
    if message == "error_not_valid":
        raise exceptions.wrongLoginCode
    elif message.startswith("no filter found for logId"):
        raise exceptions.wrongLogId
    elif message == "error_not_valid":
        raise exceptions.wrongLoginCode
    else:
        print((statusCode, message))
        raise exceptions.unknownException

def loginWithCode(code): #lets you login with the login code
    data = {"params": {
            "value": code,
            "checkCaptcha": False
        }}
    
    response = defReq(url="https://d-apis-db.anton.app/?p=login/step1/step1", data=data, path="/../server-apis-db2/apis/login/step1/step1", authToken="noStoredAuthTokenFound")
    return(session.session(response))


def createUser(name, avatar=None): #creates a user with a default avatar

    with open("defAvatar.json", "r") as avatarData:
        avatarData = json.loads(avatarData.read()) #loads default avatar data
    if avatar != None:
        avatarData = avatar

    data = {"params": {
        "funnelId": getRandomString(32),
        "type": "pupil",
        "name": name,
        "avatar": avatarData,
        "grade": 1,
        "subject": "NATDEU",
        "howKnowAbout": "relatives",
        "guiLanguage": "de",
        "deviceSrc": "2V4Z"
    }}


    response = defReq(url="https://f-apis-db.anton.app/?p=user/create2/create", data=data, path="/../server-apis-db2/apis/user/create2/create", authToken="noStoredAuthTokenFound")
    return createdUser.createdUser(response)


def getEventsFromLogId(logId): #gets events from a log id (i dont quite understand how this works, but you can get the login code from this)
    url = "https://apis-db-logger-s-lb-2.anton.app/apisLogger/subscribe/"
    params = {
        "path": "subscribe",
        "params[logId]": logId,
        "params[filter][name]": "subscribeUser",
        "params[inserted]": "1970-01-01",
        "params[readOnly]": "false",
        "deviceLogId": "D-2V4Z-aUdJ9leOB2RDiXu8jR0N9Hfefaz"
    }

    response = requests.get(url, params=params, headers=headers)
    checkResponse(response)
    response = json.loads(response.text)
    return response["events"]

def getUserCode(logId): #gets the latest events from the log id (which contains the loginCode)
    events = getEventsFromLogId(logId)
    for event in events:
        if event["event"] == "setLoginCode":
            return(event["value"])
        
def logInWithLogId(logId): #logs in with the login code getting the user code from the log id and then logging in with it
    userCode = getUserCode(logId)
    return(loginWithCode(userCode))