import requests
def web_search(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    data = response.json()

    if "Abstract" in data and data["Abstract"] != "":
        return data["Abstract"]

    return "No good result found"