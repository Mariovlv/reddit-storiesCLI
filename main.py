import requests

# Variables
CLIENT_ID = ""
CLIENT_SECRET = ""
PASSWORD = ""
USERNAME = ""
subredd = ''
headers = {'User-Agent': 'MyBot/0.0.1'}

def auth() -> str:
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    data = {'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD}
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    return TOKEN

TOKEN = auth()

def response(token, headers, subr) -> dict:
    headers = {**headers, **{'Authorization': f"bearer {token}"}}
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    res = requests.get(f"https://oauth.reddit.com/r/{subr}", headers=headers)
    return res.json()['data']['children']

def stories(subredd):
    resp = response(TOKEN, headers, subredd)
    for storie in resp:
        print('--------------------------------------------------')
        print('Author: ' , storie['data']['author'])
        print('Title: ' ,storie['data']['title'])
        print(storie['data']['selftext'].strip())
        print('URL: ' , storie['data']['url'])


stories(subredd)
