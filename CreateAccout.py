import json
import os
import random
import string
import bcrypt
import shutil
from fastapi import FastAPI
import uvicorn
import sched
import time
import subprocess
import asyncio
from pydantic import BaseModel
app = FastAPI()



parentfolder = os.path.dirname(os.path.abspath(__file__))
print(parentfolder)

UserIDList = []
TokenDict = {}  #"Name":"Token"

#XP to level y = 200*y 

@app.get("/")
def index():
    return {"log": "MeteorBackend"}

@app.get("/login/createaccount")
def appcreateacc(ID: str, Pass: str) -> dict[str, str]:
    return createaccount(ID, Pass)

@app.get("/login/connect")
def appconnect(ID:str, Pass:str) -> dict[str,str]:
    return auth(ID, Pass)

@app.get("/login/logout")
def applogout(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "TokenDoesNotExist"}
    removetoken(JFile["AccountName"])
    return {"log": "ok"}

@app.get("/login/connectbytoken")
def appconnectbytoken(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "TokenDoesNotExist"}
    return {"log": "ok", "username": JFile["AccountName"]}

@app.get("/account/locker/getlocker")
def appgetlocker(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "skins": JFile["Locker"]["Skins"], "backpacks": JFile["Locker"]["Backpacks"], "pickaxes": JFile["Locker"]["Pickaxes"], "gliders": JFile["Locker"]["Gliders"], "contrails": JFile["Locker"]["Contrails"], "loadingscreens": JFile["Locker"]["LoadingScreens"], "emotes": JFile["Locker"]["Emotes"]}

@app.get("/account/locker/getequippedlocker")
def appgetequippedlocker(Token: str)  -> dict[str, str]:
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "skin": JFile["Locker"]["Skin"], "backpack": JFile["Locker"]["Backpack"], "pickaxe": JFile["Locker"]["Pickaxe"], "glider": JFile["Locker"]["Glider"], "contrail": JFile["Locker"]["Contrail"], "loadingscreen": JFile["Locker"]["LoadingScreen"], "emote1": JFile["Locker"]["Emote1"], "emote2": JFile["Locker"]["Emote2"], "emote3": JFile["Locker"]["Emote3"], "emote4": JFile["Locker"]["Emote4"], "emote5": JFile["Locker"]["Emote5"], "emote6": JFile["Locker"]["Emote6"]}

@app.get("/account/locker/setskin")
def appsetskin(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setskin(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setbackpack")
def appsetbackpack(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setbackpack(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setpickaxe")
def appsetpickaxe(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setpickaxe(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setglider")
def appsetglider(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setglider(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setcontrail")
def appsetcontrail(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setcontrail(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setloadingscreen")
def appsetloadingscreen(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setloadingscreen(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setemote1")
def appsetemote1(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setemote1(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setemote2")
def appsetemote2(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setemote2(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setemote3")
def appsetemote3(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setemote3(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setemote4")
def appsetemote4(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setemote4(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setemote5")
def appsetemote5(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setemote5(JFile["AccountName"], Name)
    return {"log": "ok"}
@app.get("/account/locker/setemote6")
def appsetemote6(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    setemote6(JFile["AccountName"], Name)
    return {"log": "ok"}


@app.get("/account/activateBP")
def appactivatebp(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    if JFile["VBucksCount"] >= 950:
        activatepremiumpass(JFile["AccountName"])
        removevbucks(JFile["AccountName"], 950)
        return {"log": "ok"}
    else : 
        return {"log": "notenoughvbucks"}

@app.get("/account/buytiers")
def appbuytiers(Token: str, Tiers: int):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    if JFile["VBucksCount"] >= Tiers*150:
        givebattlestars(JFile["AccountName"], Tiers*10)
        removevbucks(JFile["AccountName"], Tiers*150)
        return {"log": "ok"}
    else : 
        return {"log": "notenoughvbucks"}

@app.get("/account/xpinfo")
def appgetxpinfo(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "Level": JFile["Level"], "XPIntoLevel": JFile["XPIntoLevel"]}

@app.get("/account/tierinfo")
def appgettierinfo(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "HasBP": JFile["BattlePassPossessed"], "Tier": JFile["BattlePassTier"], "BattleStars": JFile["BattleStarsCount"]}

@app.get("/account/vbuckcount")
def appgetvbuckcount(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "Count": JFile["VBucksCount"]}

@app.get("/account/questlog")
def appgetquestlog(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "questlog": JFile["ChallengeProgress"]}

@app.get("/account/questset")
def appgetquestset(Token: str, Name: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    ChallengeSet = open("ChallengesSets/"+set["Name"]+".json", "r")
    JChallengeSet = json.load(ChallengeSet)
    return {"log": "ok", "questset": JChallengeSet}

@app.get("/account/rewardlist")
def appgetrewardlist(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "rewardlist": JFile["RewardsToBeClaimed"]}

@app.get("/account/clearrewardlist")
def appgetrewardlist(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    clearrewardlist(JFile["AccountName"])
    return {"log": "ok"}

class ChallengeRequest(BaseModel):
    Token: str
    ChallengeUp: str


@app.post("/account/updatechallenges")
def appupdatechallenges(request: ChallengeRequest):
    Token = request.Token
    ChallengeUp = json.loads(request.ChallengeUp)
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    progresschallenges(JFile["AccountName"], ChallengeUp)
    return {"log": "ok"}

@app.get("/account/finishgame")
def appfinishgame(Token: str, GameStats): #elim,assist,revive,placement,maxplayers,chest,ammobox,gamemode
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    JGS = json.loads(GameStats)
    #addmatchtostats(JFile["AccountName"], GameStats)
    givexp(JFile["AccountName"], JGS["elim"]*100 + JGS["assist"]*25 + JGS["revive"]*50 + getplacementXP(JGS["placement"], JGS["maxplayers"]) + JGS["chest"]*10 + JGS["ammobox"]*5)
    return {"log": "ok"}

@app.get("/account/lastmatches")
def appgetlastmatches(Token: str):
    JFile = getuserfilebytoken(Token)
    if JFile == "MissingToken":
        return {"log": "Token does not exist"}
    return {"log": "ok", "lastmatches": JFile["PreviousMatches"]}


@app.get("/news")
def appgetnews():
    JNews = json.load(open("News.json", "r"))
    return JNews

@app.get("/shop")
def appgetshop():
    JShop = json.load(open("Shop/Shop.json", "r"))
    return JShop

@app.get("/shop/buy")
def appgetshop(Player: str, Category: str, ID: int):
    JShop = json.load(open("Shop/Shop.json", "r"))
    JFile = readuserfile(Player)
    if not canaffordvbucks(Player, JShop[Category][ID]["Price"]):
        return {"log": "CantAfford"}
    givereward(Player, JShop[Category][ID]["Item"]["RewardID"], JShop[Category][ID]["Item"]["Amount"], JShop[Category][ID]["Item"]["Note"])    
    return {"log": "ok"}

def addmatchtostats(Player: str, GameStats):
    JFile = readuserfile(Player)
    JFile["PreviousMatches"].append(GameStats)
    if not GameStats["gamemode"] in JFile["Stats"]:
        JFile["Stats"][GameStats["gamemode"]] = {"elim": 0, "matchplayed": 0, "top1": 0, "top3": 0, "top6": 0}
    JFile["Stats"][GameStats["gamemode"]]["elim"] += GameStats["elim"]
    JFile["Stats"][GameStats["gamemode"]]["matchplayed"] +=1
    if GameStats["placement"] <= 6:
        JFile["Stats"][GameStats["gamemode"]]["top6"] +=1
        if GameStats["placement"] <= 3:
            JFile["Stats"][GameStats["gamemode"]]["top3"] +=1
            if GameStats["placement"] == 1:
                JFile["Stats"][GameStats["gamemode"]]["top1"] +=1
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return




def getplacementXP(place: int, playernb: int):
    if place == 1:
        return 1000
    if place == 2:
        return 750
    if place == 3:
        return 500
    return int(round(((playernb-place)/playernb)*500))

def createuserfile(ID : str):
    shutil.copy("DefaultAccount.json", "Accounts/"+ID+".json")
    with open("Accounts/"+ID+".json", "r") as file:
        print("Created account named", ID)
        UserIDList.append(ID)
        jfile=readuserfile(ID)
        jfile["AccountName"] = ID
        with open("Accounts/"+ID+".json", "w") as savefile:
            json.dump(jfile, savefile, indent=4)
        file.close
        return

def readuserfile(ID):
    with open("Accounts/"+ID+".json") as file:
        return json.load(file)

def addtoken(ID):

    Token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))
    TokenDict[ID]= Token
    print("Created token for", ID)
    return Token

def removetoken(ID):
    if ID in TokenDict:
        del TokenDict[ID]
        print(ID+"'s token deleted.")
        return
    else:
        print(ID+"'s token could not be deleted as it didn't exist")
        return

def getuserfilebytoken(Token):
    FoundPlayer = [key for key, value in TokenDict.items() if value == Token]
    if len(FoundPlayer) == 1:
        return readuserfile(FoundPlayer[0])
    else:
        print("Token not found")
        return "MissingToken"



def setpass(ID, Pass):
    jfile=readuserfile(ID)
    jfile["Pass"] = Pass.decode("utf-8")
    with open("Accounts/"+ID+".json", "w") as savefile:
        json.dump(jfile, savefile, indent=4)
    print("SetPassword")
    return

def createaccount(ID: str, Pass: str):
    
    if not os.path.exists("Accounts/"+ID+".json") :
        if len(ID)<=2:
            print("Account was not created as ID is too short")
            return {"Log": "IDTooShort"}
        if len(Pass)<=8:
            print("Account was not created as pass is too short")
            return {"log": "PassTooShort"}
        Hash = bcrypt.hashpw(Pass.encode('utf-8'), bcrypt.gensalt())
        createuserfile(ID)
        setpass(ID, Hash)
        return{"log": "AccountCreated", "Token": addtoken(ID)}

    else:
        print("Could not create account", ID, "as another account already has that name")
        return {"Log": "ExistingID"}

def auth(ID: str, Pass: str):
    if not os.path.exists("Accounts/"+ID+".json"):
        print("Connection failed, username does not exist.")
        return {"log": "UserNameNotExist"}
    JFile = readuserfile(ID)
    AccPass = JFile["Pass"]
    if bcrypt.checkpw(Pass.encode('utf-8'), AccPass.encode('utf-8')):
        print(ID, "connected successfully.")
        return {"log": "ConnectionOK", "token": addtoken(ID)}
    else:
        print(ID, "input a wrong pass.")
        return {"log": "PassWrong"}

def getxptolevel(lvl: int):
    return 200*lvl

def getxp(ID: str):
    JFile = readuserfile(ID)
    return JFile["Level"], JFile["XPIntoLevel"]

def getacclvl(ID : str):
    JFile = readuserfile(ID)
    return JFile["AccountLevel"]

def getbattlestarperlvl(lvl: int):
    if lvl%10 == 0:
        return 10
    if lvl%5 == 0:
        return 5
    return 2

def givexp(ID: str, Amount: int):
    XPToGive = Amount
    Lvl, XPIntoLvl = getxp(ID)
    AccLvl = getacclvl(ID)
    while XPToGive > 0 and Lvl < 100:
        if getxptolevel(Lvl+1)-XPIntoLvl > XPToGive:
            XPIntoLvl += XPToGive
            XPToGive = 0
        else:
            XPToGive = XPToGive - (getxptolevel(Lvl+1)-XPIntoLvl)
            Lvl += 1
            AccLvl += 1
            print(ID, "reached level", Lvl)
            givelevelreward(ID, Lvl)
            XPIntoLvl = 0
    setlevel(ID, Lvl, XPIntoLvl)
    setaccountlvl(ID, AccLvl)
    return

def givelevelreward(player: str, lvl: int):
    givebattlestars(player, getbattlestarperlvl(lvl))
    return

def setlevel(player:str, lvl: int, XPIntoLvl: int):
    JFile = readuserfile(player)
    JFile["Level"] = lvl
    JFile["XPIntoLevel"] = XPIntoLvl
    with open("Accounts/"+player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setaccountlvl(player:str, lvl: int):
    JFile = readuserfile(player)
    JFile["AccountLevel"] = lvl
    with open("Accounts/"+player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def givereward(Player:str, RewardID: int, Amount: int, Name: str): #0: vbucks, 1: XP, 2: BattleStars, 3: Skin, 4: Backpack, 5: Glider, 6: Pickaxe, 7: Contrail, 8: Loading screen, 9: Emote, 10: Challenge set
    if RewardID == 0:
        givevbucks(Player, Amount)
    elif RewardID == 1:
        givexp(Player, Amount)
    elif RewardID == 2:
        givebattlestars(Player, Amount)
    elif RewardID == 3:
        addskin(Player, Name)
    elif RewardID == 4:
        addbackpack(Player, Name)
    elif RewardID == 5:
        addglider(Player, Name)
    elif RewardID == 6:
        addpickaxe(Player, Name)
    elif RewardID == 7:
        addcontrail(Player, Name)
    elif RewardID == 8:
        addloadingscreen(Player, Name)
    elif RewardID == 9:
        addemote(Player, Name)
    elif RewardID == 10:
        givechallengeset(Player, Name)
    addtorewardlist(Player, RewardID, Amount, Name)
    return


def addtorewardlist(Player:str, RewardID: int, Amount: int, Name: str):
    JFile = readuserfile(Player)
    JFile["RewardsToBeClaimed"].append({"RewardID": RewardID, "Amount": Amount, "Name": Name})
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def clearrewardlist(Player: str):
    JFile = readuserfile(Player)
    JFile["RewardsToBeClaimed"] = []
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def givechallengeset(Player: str, SetName: str):
    JFile = readuserfile(Player)
    for set in JFile["ChallengeProgress"]:
        if set["Name"] == SetName:
            return
    ChallengeSet = open("ChallengesSets/"+SetName+".json", "r")
    JChallengeSet = json.load(ChallengeSet)
    JFile["ChallengeProgress"].append({"Name": SetName, "Completed": False, "Progression": 0, "Quests": [{"Completed": False, "Progress": 0} for i in range(JChallengeSet["ChallengeCount"])]})
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def progresschallenges(Player: str, challengeup):    #challengeup is a dictionary of the challgenges progressed:
    challengelist = challengeup.keys()
    JFile = readuserfile(Player)
    RewardsToGive=[]   #Rewards are given after the process to avoid save bugs
    for set in JFile["ChallengeProgress"]:
        if not set["Completed"]:
            ChallengeSet = open("ChallengesSets/"+set["Name"]+".json", "r")
            JChallengeSet = json.load(ChallengeSet)
            TempCompleted = 0
            QuestID=-1
            for quest in set["Quests"]:
                QuestID += 1
                if quest["Completed"]:
                    TempCompleted += 1
                else:
                    if JChallengeSet["ChallengeList"][QuestID]["ChallengeName"] in challengelist:
                        quest["Progress"] += challengeup[JChallengeSet["ChallengeList"][QuestID]["ChallengeName"]]
                        if quest["Progress"] >= JChallengeSet["ChallengeList"][QuestID]["AmountToDo"]:
                            quest["Completed"] = True
                            TempCompleted += 1
                            RewardsToGive.append({"RewardID": JChallengeSet["ChallengeList"][QuestID]["Reward"]["RewardID"], "Amount": JChallengeSet["ChallengeList"][QuestID]["Reward"]["Amount"], "Name": JChallengeSet["ChallengeList"][QuestID]["Reward"]["Name"]})
            if set["Progression"] < JChallengeSet["ChallengesToGetReward"] and TempCompleted >= JChallengeSet["ChallengesToGetReward"]:
                print("COMPLETED CHALLENGESET REWARD")
                RewardsToGive.append({"RewardID": JChallengeSet["Reward"]["RewardID"], "Amount": JChallengeSet["Reward"]["Amount"], "Name": JChallengeSet["Reward"]["Name"]})
            set["Progression"] = TempCompleted
            if TempCompleted == JChallengeSet["ChallengeCount"]:
                set["Completed"] = True
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    for i in RewardsToGive:
        givereward(Player, i["RewardID"], i["Amount"], i["Name"])
    return                
                



def givebattlestars(Player: str, Amount: int):
    StarsToGive = Amount
    Tier, Stars = gettier(Player)
    while StarsToGive > 0 and Tier < 100:
        if 10-Stars > StarsToGive:
            Stars += StarsToGive
            StarsToGive = 0
            settier(Player, Tier, Stars)
        else:
            StarsToGive = StarsToGive - (10-Stars)
            Tier += 1
            print(Player, "reached tier", Tier)
            Stars = 0
            settier(Player, Tier, Stars)
            givefreetierreward(Player, Tier)
            givepremiumtierreward(Player, Tier)
            
    if StarsToGive>0 : 
        givexp(Player, StarsToGive*100) #each overflowing battlestar is converted to 100 xp
    settier(Player, Tier, Stars)
    return

def gettier(Player: str):
    JFile = readuserfile(Player)
    return JFile["BattlePassTier"], JFile["BattleStarsCount"]

def settier(player:str, tier: int, stars: int):
    JFile = readuserfile(player)
    JFile["BattlePassTier"] = tier
    JFile["BattleStarsCount"] = stars
    with open("Accounts/"+player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def activatepremiumpass(Player: str):
    JFile = readuserfile(Player)
    JFile["BattlePassPossessed"] = True
    Tier, _ = gettier(Player)
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    for i in range(Tier):
        givepremiumtierreward(Player, i+1)



def givefreetierreward(Player: str, Tier: int):
    JFile = readuserfile(Player)
    BP = json.load(open("BattlePass/FreePass.json"))
    if str(Tier) in BP["Rewards"]:
        givereward(Player, BP["Rewards"][str(Tier)]["RewardID"], BP["Rewards"][str(Tier)]["Amount"], BP["Rewards"][str(Tier)]["Name"])
    return
    

def givepremiumtierreward(Player: str, Tier: int):
    JFile = readuserfile(Player)
    
    if JFile["BattlePassPossessed"]:
        BP = json.load(open("BattlePass/Pass.json"))
        givereward(Player, BP["Rewards"][str(Tier)]["RewardID"], BP["Rewards"][str(Tier)]["Amount"], BP["Rewards"][str(Tier)]["Name"])
        return


def givevbucks(Player: str, Amount: int):
    JFile = readuserfile(Player)
    JFile["VBucksCount"] = JFile["VBucksCount"] + Amount
    print("Gave", Amount, "VBucks to", Player)
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def canaffordvbucks(Player: str, Amount: int):
    JFile = readuserfile(Player)
    return JFile["VBucksCount"] >= Amount

def removevbucks(Player: str, Amount: int):
    JFile = readuserfile(Player)
    JFile["VBucksCount"] = JFile["VBucksCount"] - Amount
    print("Removed", Amount, "VBucks from", Player)
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)





def setskin(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Skin"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setbackpack(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Backpack"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setglider(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Glider"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setpickaxe(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Pickaxe"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setcontrail(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Contrail"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setloadingscreen(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["LoadingScreen"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setemote1(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Emote1"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setemote2(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Emote2"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setemote3(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Emote3"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setemote4(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Emote4"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setemote5(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Emote5"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def setemote6(Player: str, CosmeticName: str):
    JFile = readuserfile(Player)
    JFile["Locker"]["Emote6"] = CosmeticName
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return


def getequippedlocker(Player: str):
    JFile = readuserfile(Player)
    return [JFile["Locker"]["Skin"], JFile["Locker"]["Backpack"], JFile["Locker"]["Glider"], JFile["Locker"]["Pickaxe"], JFile["Locker"]["Contrail"], JFile["Locker"]["LoadingScreen"], JFile["Locker"]["Emote1"], JFile["Locker"]["Emote2"], JFile["Locker"]["Emote3"], JFile["Locker"]["Emote4"], JFile["Locker"]["Emote5"], JFile["Locker"]["Emote6"]]

def getlocker(Player: str):
    JFile = readuserfile(Player)
    return [JFile["Locker"]["Skins"], JFile["Locker"]["Backpacks"], JFile["Locker"]["Gliders"], JFile["Locker"]["Pickaxes"], JFile["Locker"]["Contrails"], JFile["Locker"]["LoadingScreens"], JFile["Locker"]["Emotes"]]


def addskin(Player: str, Name: str):
    JFile=readuserfile(Player)
    JFile["Locker"]["Skins"].extend([Name])
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def addbackpack(Player: str, Name: str):
    JFile=readuserfile(Player)
    JFile["Locker"]["Backpacks"].extend([Name])
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def addglider(Player: str, Name: str):
    JFile=readuserfile(Player)
    JFile["Locker"]["Gliders"].extend([Name])
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def addpickaxe(Player: str, Name: str):
    JFile=readuserfile(Player)
    JFile["Locker"]["Pickaxes"].extend([Name])
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def addcontrail(Player: str, Name: str):
    JFile=readuserfile(Player)
    JFile["Locker"]["Contrails"].extend([Name])
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def addloadingscreen(Player: str, Name: str):
    JFile=readuserfile(Player)
    JFile["Locker"]["LoadingScreens"].extend([Name])
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return

def addemote(Player: str, Name: str):
    JFile=readuserfile(Player)
    JFile["Locker"]["Emotes"].extend([Name])
    with open("Accounts/"+Player+".json", "w") as savefile:
        json.dump(JFile, savefile, indent=4)
    return


#Matchmaking system

scheduler = sched.scheduler(time.time, time.sleep)

class MatchQueue:
    def __init__(self, ServerIP: str, MaxPlayers: int, MaxTime: int, MatchID:int):
        self.ServerIP = ServerIP
        self.MaxPlayers = MaxPlayers
        self.MaxTime = MaxTime
        self.Started = False
        self.MatchID=MatchID
        self.PlayersInQueue = 0
        #if MaxTime != 0:
        #    print("Delay of", MaxTime,"seconds")
        #    scheduler.enter(delay=MaxTime, action=MatchTimeOut, argument=(MatchID,), priority=1)
        #    scheduler.run()

MatchQueues = {} #ID(int):Queue(Object)
PlayerQueue = []
PlayerMoved = {} #PlayerID(int):MatchID(int), used to give players their matchID

main_loop = None
server_process = None
def start_server():
    global server_process
    exe_path = r"D:\Unreal Projects\Meteor\Builds\1.0.0 Beta 2\Server\BRSolo\WindowsServer\MeteorServer.exe"

    if not os.path.exists(exe_path):
        print("Executable not found.")
        return

    server_process = subprocess.Popen(exe_path)
    print(f"Server started with PID: {server_process.pid}")

def stop_server():
    global server_process
    print(f"Terminating process with PID {server_process.pid}")
    server_process.terminate()
    server_process.wait()
    server_process = None
    print("Server terminated.")



def creatematchqueue(ServIP: str, MaxPlrs: int, MaxTme: int):
    MatchID:int = random.randint(1000000, 9999999)
    tempmatch = MatchQueue(ServerIP=ServIP, MaxPlayers=MaxPlrs, MaxTime=MaxTme, MatchID=MatchID)
    MatchQueues[MatchID] = tempmatch
    print("MATCH CREATED Created match with ID", MatchID)
    fillqueue(MatchID)
    if MaxTme > 0:
        main_loop.create_task(starttimeouttimer(MatchID, MaxTme))
    return MatchID

async def starttimeouttimer(MatchID: int, Time: int):
    print("Started time out timer for match", MatchID)
    await asyncio.sleep(Time)
    MatchTimeOut(MatchID)

def MatchTimeOut(MatchID:int):
    if MatchID in MatchQueues:
        print("CALLED MATCH TIMEOUT")
        if not MatchQueues[MatchID].Started:
            StartMatch(MatchID)
            print("Match", MatchID, "timed out.")
    return

def StartMatch(MatchID:int):
    if MatchID in MatchQueues:
        if not MatchQueues[MatchID].Started:
            start_server()
            MatchQueues[MatchID].Started = True
            print("Match", MatchID, "started")
            main_loop.create_task(startdeletetimer(MatchID))
            
    return

async def startdeletetimer(MatchID: int):
    print("Started timer to delete match", MatchID)
    await asyncio.sleep(20)
    DeleteMatchFromList(MatchID)


def DeleteMatchFromList(MatchID:int):
    del MatchQueues[MatchID]
    print("MatchMaking : Removed match", MatchID, "from the list")
    return

def findmatch():
    if MatchQueues:
        for i in MatchQueues.values():
            if not i.Started:
                i.PlayersInQueue += 1
                if i.PlayersInQueue == i.MaxPlayers:
                    StartMatch(MatchQueues[list(MatchQueues)[i]])
                return {"MatchID":i.MatchID}
    MatchmakerPlayerID:int = random.randint(1000000, 9999999)
    PlayerQueue.append(MatchmakerPlayerID)
    return {"MatchmakerPlayerID": MatchmakerPlayerID}
    
def leavequeue(MatchOrPlayerID:int):
    if MatchOrPlayerID in MatchQueues:
        MatchQueues[MatchOrPlayerID].PlayersInQueue -= 1
        fillqueue(MatchOrPlayerID)
    elif MatchOrPlayerID in PlayerQueue:
        PlayerQueue.remove(MatchOrPlayerID)
    elif MatchOrPlayerID in PlayerMoved:
        tempPlayer = PlayerMoved[MatchOrPlayerID]
        del PlayerMoved[MatchOrPlayerID]
        leavequeue(tempPlayer)
    return {"Log": "OK"}

def fillqueue(MatchID:int):
    for i in range(MatchQueues[MatchID].MaxPlayers-MatchQueues[MatchID].PlayersInQueue):
        if PlayerQueue:
            PlayerMoved[PlayerQueue[0]] = MatchID
            del PlayerQueue[0]
        else:
            MatchQueues[MatchID].PlayersInQueue += 1
            if MatchQueues[MatchID].PlayersInQueue == MatchQueues[MatchID].MaxPlayers:
                    StartMatch(MatchID)
            return
    return

def getfindmatchstate(MatchmakerPlayerID:int):
    if MatchmakerPlayerID in PlayerQueue:
        return{"log":"InQueue","PosInQueue": PlayerQueue.index(MatchmakerPlayerID), "PlayersInQueue": len(PlayerQueue)}
    if MatchmakerPlayerID in PlayerMoved:
        TempMatchID = PlayerMoved[MatchmakerPlayerID]
        TempPlayersInQueue = MatchQueues[PlayerMoved[MatchmakerPlayerID]].PlayersInQueue
        del PlayerMoved[MatchmakerPlayerID]
        return{"log": "FoundMatch","MatchID": TempMatchID,"PlayersInQueue": TempPlayersInQueue}
    return {"log": "MatchmakerPlayerID not found"}

def getmatchstate(MatchID:int):
    if MatchID in MatchQueues:
        if MatchQueues[MatchID].Started:
            print("Sent server IP :", MatchQueues[MatchID].ServerIP)
            return {"log": "ok", "ServerIP": MatchQueues[MatchID].ServerIP}
        else :
            return {"log": "ok", "PlayersInQueue": MatchQueues[MatchID].PlayersInQueue}
    return {"log": "error"}

@app.get("/matchmaking/dev/creatematch")   #Called by a bat file for now
def appcreatematch(Pass: str, ServerIP: str, MaxPlayers: int, MaxTime: int):
    if Pass == "azertyuiop":
        return creatematchqueue(ServIP=ServerIP, MaxPlrs=MaxPlayers, MaxTme=MaxTime)
    
@app.get("/matchmaking/dev/startmatch")    #Called by a bat file if the launch is not automatic
def appstartmatch(MatchID:int, Pass: str):
    if Pass == "azertyuiop":
        #return StartMatch(MatchID=MatchID)
        return StartMatch(list(MatchQueues.keys())[0])
    
@app.get("/matchmaking/findmatch")
def appfindmatch():
    return findmatch()

@app.get("/matchmaking/leavequeue")
def appleavequeue(MatchOrPlayerID:int):
    return leavequeue(MatchOrPlayerID=MatchOrPlayerID)

@app.get("/matchmaking/getfindmatchstate")
def appgetfindmatchstate(MatchmakerPlayerID:int):
    return getfindmatchstate(MatchmakerPlayerID)

@app.get("/matchmaking/getmatchstate")
def appgetmatchstate(MatchID:int):
    return getmatchstate(MatchID)



#givechallengeset("123456", "Week0")
#progresschallenges("123456", {"AmmoBoxes":30,"Kills":2})
#progresschallenges("123456", {"Kills": 4})
#progresschallenges("123456", {"ChestTilted": 8})
#progresschallenges("123456", {"DamageAR": 1040})

@app.on_event("startup")
async def on_startup():
    global main_loop
    
    main_loop = asyncio.get_running_loop()
    

uvicorn.run(app, host="26.7.218.233", port=1234)


