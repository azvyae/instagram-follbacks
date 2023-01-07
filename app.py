import json


def loadFiles(account):
    data = {}
    with open(f"./accounts/{account}/followers.json") as file:
        data["followers_json"] = json.load(file)

    with open(f"./accounts/{account}/following.json") as file:
        data["following_json"] = json.load(file)

    try:
        with open(f"./accounts/{account}/exclude.json") as file:
            data["excluded_json"] = json.load(file)
    except FileNotFoundError:
        print("Continuing without excluded accounts")

    try:
        with open(f"./accounts/{account}/unfollowed.json") as file:
            data["unfollowed_json"] = json.load(file)
    except FileNotFoundError:
        print("Continuing without unfollowed accounts")

    return data


def prepareData(data):
    followingList = []
    for following in data["following_json"]["relationships_following"]:
        followingList.append(following["string_list_data"][0]["value"])

    for follower in data["followers_json"]["relationships_followers"]:
        if follower["string_list_data"][0]["value"] in followingList:
            followingList.remove(follower["string_list_data"][0]["value"])

    if data.get("excluded_json") != None:
        for exclude in data["excluded_json"]["excluded"]:
            if exclude in followingList:
                followingList.remove(exclude)
    if data.get("unfollowed_json") != None:
        for unfollowed in data["unfollowed_json"]["unfollowed"]:
            if unfollowed in followingList:
                followingList.remove(unfollowed)

    return followingList


def printUsers(followingList):
    if len(followingList) > 0:
        for user in followingList:
            print(user)
    else:
        print("There are no users you follow but don't follow back")
