import requests

gist_response = requests.get("https://gist.githubusercontent.com/Multif-Johan/ccc5e88c748232c7dabbc1eb4fb03192/raw/17d34c86b5479fbc8d4534ece5b7a6dd08abd93d/eden-marco.json")
print(gist_response.json())