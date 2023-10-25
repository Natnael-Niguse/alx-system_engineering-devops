#!/usr/bin/python3
'''Reads todo list from api for employee id passed'''

import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''
    if len(sys.argv) < 2:
        print('USAGE;', __file__, '<employee id>')
        sys.exit(1)
    eid = sys.argv[1]
    try:
        _eid = int(sys.argv[1])
    except ValueError:
        print('Employee id must be an integer')
        sys.exit(1)

    response = requests.get(base_url + 'users/' + eid)
    response2 = requests.get(base_url + 'todos/')

    user = response.json()
    todos = response2.json()
    user_todos = []

    for todo in todos:
        if todo.get('userId') == user.get('id'):
            user_todos.append(todo)

    completed = []
    titles = []

    for todo in user_todos:
        if todo.get('completed'):
            completed.append(todo)
            titles.append(todo.get('title'))

    print('Employee ' + user.get('name') +
          ' is done with tasks({}/{}):'
          .format(len(completed), len(user_todos)))

    for title in titles:
        print('\t' + title)


if __name__ == '__main__':
    do_request()
