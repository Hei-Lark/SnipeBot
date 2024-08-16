import json


def reset():
    json.dump({}, 'snipeCount.json')

def updateLeaderboard():
        b = open('cogs/leaderboard.json', 'r')
        board = json.load(b)

        f = open('cogs/snipeCount.json', 'r')
        data = json.load(f)

        scores = [board["first"]["score"], board["second"]["score"], board["third"]["score"]]
        
        for i in data:
            snipes = data[str(i)]['snipes']

            if(snipes == board["first"]["score"]):
                board["first"]["members"].append(i)
            elif(snipes > scores[0]):
                board["third"]["members"] = board["second"]["members"]
                board["second"]["members"] = board["first"]["members"]
                board["first"]["members"] = [i]

                board["first"]["score"] = data[str(i)]["snipes"]

            elif (snipes == board["second"]["score"]):
                board["second"]["members"].append(i)
            elif (snipes > board["second"]["score"]):
                board["third"]["members"] = board["second"]["members"]
                board["second"]["members"] = [i]

                board["second"]["score"] = data[str(i)]["snipes"]

            elif(snipes == board["third"]["score"]):
                board["third"]["members"].append(i)
            elif (snipes > board["third"]["score"]):
                board["third"]["members"] = [i]

                board["third"]["score"] = data[str(i)]["snipes"]

        b = open('cogs/leaderboard.json', 'w')
        print(board)
        json.dump(board, b)

        b = open('cogs/leaderboard.json', 'r')
        json.load(b)
        return

