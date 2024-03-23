# Games

Here is shown how to use to pixelPaint and avatarSuperstar functions of antonLib.

## PixelPaint

To do anything with pixelPaint you first need a session. [Here](accountStuff.md#logging-in) is how to create one.  

### PixelPaint Functions

Here is a list of all functions of pixelPaint:

```python
import antonLib

session = antonLib.logInWithLogId("yourLogId")

session.likePixelPaint("uid") #likes a pixelPaint image
session.dislikePixelPaint("uid") #dislikes a pixelPaint image
session.publishPixelPaintImage(svg, uid) #publishes a pixelPaint image (WARNING: this is very buggy and only works least of the time) (the svg can be whatever you want) (doesnt require coins)
session.getPixelPaintData("uid") #gets info about an pixelPaint image
```

### PixelPaintData Attributes

```python
import antonLib

session = antonLib.logInWithLogId("yourLogId")
pixelPaintData = session.getPixelPaintData("uid")

pixelPaintData.uid #uid of the image
pixelPaintData.created #when the image was created
pixelPaintData.likes #amount of likes
pixelPaintData.idFavourite #something idk
pixelPaintData.isFlagged #if it is flagged
pixelPaintData.creatorName #name of the creator
pixelPaintData.creatorAvatar #avatar of the creator
pixelPaintData.isPublic #if it is public (when you try to get info about your own unpublished images)
```

## AvatarSuperstar

To do anything with avatarSuperstar you first need a session. [Here](accountStuff.md#logging-in) is how to create one.  

### AvatarSuperstar Functions

Here is a list of all functions of pixelPaint:

```python
import antonLib

session = antonLib.logInWithLogId("yourLogId")

session.likeAvatarSuperstar("uid") #likes an avatar
session.dislikeAvatarSuperstar("uid") #dislikes an avatar
session.publishAvatarSuperstar(avatarData) #publishes an avatar (doesnt require coins)
session.getAvatarData("uid") #gets info about an avatar
```

### AvatarSuperstar Attributes

```python
import antonLib

session = antonLib.logInWithLogId("yourLogId")
avatarData = session.getAvatarData("uid")

avatarData.uid #uid of the image
avatarData.created #when the image was created
avatarData.likes #amount of likes
avatarData.isFavourite #if it is favourited
```
