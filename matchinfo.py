
import pandas as pd
from riotwatcher import LolWatcher, ApiError
import json
import  requests


def gethistory(name):
    api_key="RGAPI-b405b394-de14-4259-a708-5da4ab89b383"
    watcher = LolWatcher(api_key)
    my_region="EUN1"
    player=watcher.summoner.by_name(my_region, name)['accountId']
    link="https://eun1.api.riotgames.com/lol/match/v4/matchlists/by-account/{0}?endIndex=10&beginIndex=0&api_key={1}".format(player,api_key)
    match_history=requests.get(link).json()
    match_history=match_history['matches']
    return(match_history)
def datafrommatc(match):
    api_key="RGAPI-b405b394-de14-4259-a708-5da4ab89b383"
    champion=match["champion"]
    link="https://eun1.api.riotgames.com/lol/match/v4/matches/{0}?api_key={1}".format(match['gameId'],api_key)
    game=requests.get(link).json()
    winingteam=100
    if(game["teams"][1]["win"]=="Win"):
        winingteam=200
    info={"Items":[] ,"KDA":1 ,"win/lose":"Victory","Vision":0,"Cs":0}
    for participant in game["participants"]:
        if(participant["championId"]==champion):
            items=[]
            items.append(participant["stats"]["item0"])
            items.append(participant["stats"]["item1"])
            items.append(participant["stats"]["item2"])
            items.append(participant["stats"]["item3"])
            items.append(participant["stats"]["item4"])
            items.append(participant["stats"]["item5"])
            info["Items"]=items
            info["Vision"]=participant["stats"]["wardsPlaced"]+participant["stats"]["wardsKilled"]
            if(participant["teamId"]!=winingteam):
                info["win/lose"]="Defeat"
            try:
                info["KDA"]=(participant["stats"]["kills"]+participant["stats"]["assists"])/participant["stats"]["deaths"]
            except:
                info["KDA"]=participant["stats"]["kills"]+participant["stats"]["assists"]
            cs=participant['timeline']['creepsPerMinDeltas']
            score=0
            try:
                score=cs['10-20']+cs['0-10']+cs['20-30']
                if(score!=0):
                    score=score/3
            except:
                try:
                    score=cs['10-20']+cs['0-10']
                    if(score!=0):
                        score=score/2
                except:
                    score=cs['0-10']
            info["Cs"]=score
    return info

            
            
            
            
            
        
    
