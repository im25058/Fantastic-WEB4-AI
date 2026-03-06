import requests
import urllib.parse

def web_search(query):

    # Clean query
    query = query.lower()
    query = query.replace("what is", "")
    query = query.replace("how does", "")
    query = query.replace("examples of", "")
    query = query.replace("?", "")
    query = query.strip()

    encoded_query = urllib.parse.quote(query)

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            data = response.json()

            if "extract" in data:
                return data["extract"]

        return f"No good result found for: {query}"

    except Exception as e:
        return f"Search error: {str(e)}"