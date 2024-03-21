# antonLib

antonLib is a python library created for interacting with the learning platform "anton.app".

## Installing

To install antonLib simply type

```bash
pip install antonLib
```

into your command prompt.

To dwonload the source code you can just type this.

```bash
git clone https://github.com/Antonabi/antonLib.git
```

### Requirements

If you downloaded the source code you have to install the requirements like this:

```bash
pip install -r requirements.txt
```

## Usage

With antonLib you can make a lot of things. View the full documentation [here]("https://github.com/Antonabi/antonLibDoc/").

### Examples

Here ill list a few examples that show what the library does.

#### Logging in

There are two different ways of logging in with antonLib.  
The first one is the simplest:

```python
import antonLib

session = antonLib.loginWithCode("yourLoginCode") #creates a session object
```

For the second one you need to have your logId:

```python
import antonLib

session = antonLib.logInWithLogId("yourLogId") #also creates a session object
```

If you dont know what a logId is, [here]("https://anotherDoclink.com") is a description.

#### Pixel Paint

When you are logged in, you can do many things. Here is how you like a pixel paint image:

```python
import antonLib

session = antonLib.loginWithCode("yourLoginCode") #logging in

session.likePixelPaint("imageUid") #liking the image
```

If you dont know how to get the uid of an image, its actually quite simple.  
To get it, you just need to click on the image, and then click on "share image". Then you will get a link that looks like this: `https://anton.app/pixelPaintImage/RqfT06Mp`. The uid is at the end of the link. In this example it is "RqfT06Mp".

#### Creating Users

With antonLib you can also create users. Creating a user is very simple. This is an example script that does it:

```python
import antonLib

createdUser = antonLib.createUser("username") #creating the user

session = antonLib.logInWithLogId(createdUser.logId) #logging in (you have to log in with the logId because a created user object doesnt give you a login code)
```

#### Full Documentation

Check out the full documentation [here]("https://github.com/Antonabi/antonLibDoc/").
