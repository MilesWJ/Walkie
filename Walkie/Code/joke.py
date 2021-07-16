from urllib import request
import json


def request_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    r = request.urlopen(url)

    data = r.read()
    json_data = json.loads(data)

    information = [json_data["setup"], json_data["punchline"]]

    joke = f"{information[0]} {information[1]}"

    return joke
