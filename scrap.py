import urllib
import json


# Variables definition


key = "400593844:AAH57kP-ndJV-VbaeitQirBCFwiE9J-gmZI"

website = "https://api.telegram.org/bot"

methodme = "/getme"

getupdates = "/getupdates"

htmlfile = urllib.urlopen(website+key+getupdates)

htmltext = htmlfile.read()

userdata = json.loads(htmltext)
x = 0


# All Functions are defined here
def getallupdates():
    print userdata["result"]


def getupdatebyindex(index):
    print userdata["result"][index]

def getMessageText(index):
    print userdata["result"][index]["message"]["text"]

def getMessageUser(index):
    print userdata["result"][index]["message"]["from"]["username"]

def getUpdatecount():
    allarrays = userdata['result']

    allarrayscount = len(allarrays)

    finalindex = allarrayscount-1

    firstindex = 0

    tryindex = 0

    print "you have " + str(allarrayscount) + " new updates."

    for tryindex in range(0 , finalindex):
        print "update: " +str(userdata["result"][tryindex]["update_id"])+"\n"
        print "message id: " +str(userdata["result"][tryindex]["message"]["message_id"])
        print "names: " +str(userdata["result"][tryindex]["message"]["from"]["first_name"])
        print "last name: " + str(userdata["result"][tryindex]["message"]["chat"]["last_name"])
        print "text: " + str(userdata["result"][tryindex]["message"]["text"])








# Rest of Code

getUpdatecount();


