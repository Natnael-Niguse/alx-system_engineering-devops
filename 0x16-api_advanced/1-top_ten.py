import requests
'''Get and print the titles of the first 10 hot posts'''

BASE_URL = 'http://reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    '''Get and print the titles of the first 10 hot.'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(BASE_URL.format(subreddit),
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data[0:10]:
            print(post.get('data', {}).get('title'))
    else:
        print("None")
