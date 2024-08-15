import json


def reset():
    json.dump({}, 'snipeCount.json')


reset()
