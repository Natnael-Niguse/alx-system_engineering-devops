#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    # URL of the Reddit API for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to identify your application
    headers = {'User-Agent': 'MyRedditApp/1.0'}

    try:
        # Make the API request
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']

            return subscribers
        else:
            print(f"Status code: {response.status_code}")

    except requests.exceptions.MissingSchema:
        print(f"Invalid subreddit: {subreddit}")

    return 0
