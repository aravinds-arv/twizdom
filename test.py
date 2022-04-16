import requests, json

PAPERQUOTES_API_ENDPOINT = 'https://api.paperquotes.com/apiv1/quotes/?tags=love&random=random&order=?&limit=1'
TOKEN = 'f45946f5d9d776657ae77c4905ce41ff9c800149'
response = requests.get(PAPERQUOTES_API_ENDPOINT, headers={'Authorization': 'TOKEN {}'.format(TOKEN)})

if response.ok:

    quotes = json.loads(response.text).get('results')

    for quote in quotes:
        print(quote.get('quote'))