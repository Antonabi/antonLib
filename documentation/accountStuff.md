# Managing Accounts

Here is shown how you can log in, what you can do in a session and how to create a user.

## Logging In

To log in you just simply create a session like this:

```python
import antonLib

session = antonLib.loginWithCode("yourLoginCode") #logging in
```

(This logs in with a login code)

You can also log in with the log id of the account:

```python
import antonLib

session = antonLib.logInWithLogId("yourLogId")
```

### Session Attributes

Here are all of the attributes that a session object gives you:

```python
session.loginCode #the login code of the user
session.logId #the logId of the user
session.authToken #the auth token of the user (only useful with a logId)
session.displayName #the display name of the user (not the unique name)
session.avatar #the avatar of the user (returns a json)
```

### Session Functions

Here is a list of all the functions of a session:

```python
session.changeUniqueName("name") #changes the unique name of a user (not the display name)
session.likePixelPaint("uid") #likes a pixelPaint image
session.dislikePixelPaint("uid") #dislikes a pixelPaint image
session.likeAvatarSuperstar("uid") #likes an avatarSuperstar avatar
session.dislikeAvatarSuperstar("uid") #dislikes an avatarSuperstar avatar
session.publishAvatarSuperstar(avatarData) #publishes an avatarSuperstar (returns the uid) (doesnt require coins)
session.publishPixelPaintImage(svg, uid) #publishes a pixelPaint image (WARNING: this is very buggy and only works least of the time) (the svg can be whatever you want) (doesnt require coins)
session.getAvatarData("uid") #gets info about an avatar
session.getPixelPaintData("uid") #gets info about an pixelPaint image
```

Here are the attributes of the [avatarData](games.md#avatarsuperstar-attributes) and [pixelPaintData](games.md#pixelpaintdata-attributes).

## Creating Users

Here is an example of creating a user and then logging in:

```python
import antonLib

createdUser = antonLib.createUser("username") #creating the user (you can also set a custom avatar)

session = antonLib.logInWithLogId(createdUser.logId) #logging in (you have to log in with the logId because a created user object doesnt give you a login code)

```

### Created User Attributes

Here are the attributes of a createdUser object:

```python
session.logId #the logId of the user
session.authToken #the auth token of the user (only useful with a logId)
session.name #the display name of the user (not the unique name)
session.funnelId #something I dont have any clue what it is but I still wanted to include
session.avatar #the avatar of the user (returns a json)
session.grade #the grade of the user (defaults to 1, may I will make it cutomizable)
session.subject #the subject the user wanted to start with (its like the grade, deafults to NATDEU (German))
session.howKnowAbout #how to user got to know anton app (same like grade and subject, defaults to "relatives")
session.guiLanguage #language of the gui (wow) (defaults to german)
session.deviceSrc #something about what your device is idk (I have 100 percently doxxed myself) (defaults to 2V4Z)
```

## NotLoggedInUser

When you try to log in whith a unique name instead of the login code (only works with login code not log id), you will get some info about this user instead of a simple auth error. (I dont know why anton does that)  

```python
import antonLib

notLoggedInUser = antonLib.loginWithCode("uniqueName") #an example script
```

Here are the infos you get:

```python
notLoggedInUser.uniqueName #the unique name
notLoggedInUser.hasPhone #returns True if you have your phone number set
notLoggedInUser.hasEMail #returns True if you have your email set
notLoggedInUser.isTeacher #returns True if the account is teacher (wow)
```
