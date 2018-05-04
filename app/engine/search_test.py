import requests

url = "http://oracleofbacon.org/"
payload = {'a':'Kevin Bacon', 'b': 'Jim Carrey'}
r = requests.post(url, payload)
with open("requests_results.html", "wb") as f:
    f.write(r.content)
