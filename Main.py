from riotwatcher import LolWatcher, ApiError
import pickle
import Player as p

lol_watcher = LolWatcher('RGAPI-fcaf5b63-e4e6-4c9d-9b2d-0a2eb574762a')
#
# match=lol_watcher.match.by_id(region="americas",match_id="NA1_4258092340")
#
# info=match.get('info')
# participants=info.get('participants')
# print(participants)
#
# for i in participants:
#     print("Summoner:" +str(i.get('participantId')))
#     print("Champ",i.get('championName'))
#     print("Name:",i.get('summonerName'))
#     print("Kills:",i.get('kills'))
#     print("Deaths",i.get('deaths'))

print(p.x)
# def main():
#     x = input("Enter 1 to add a match, enter 3 to check stats")
#     if x==1:
#         addMatch()
#     else:
#         # checkStats()


def addMatch():
    validMatch=False
    while not validMatch:
        try:
            id=input("Enter Match ID")
            match=lol_watcher.match.by_id(region="americas",match_id=id)
        except:
            print("not a valid match ID try again")

# def checkStats():
#     x=input("please enter the summoner name or type ALL to display all player stats")
#     if x=="ALL":
#         # outputAll()
#     else if x in playerDict

