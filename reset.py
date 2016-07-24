#!/usr/bin/env python
import os
from github3 import login

gh = login(token=os.environ['GITHUB_TOKEN'])
user = 'jantman'
repo_name = 'BoardTest'

repo = gh.repository(user, repo_name)

assert repo.pull_request(1).is_merged() is False
assert repo.pull_request(6).is_merged() is False
assert repo.pull_request(7).is_merged() is True

repo.issue(2).edit(
    title='issue1',
    body='issue1 text',
    assignee='',
    state='open',
    milestone=0,
    labels=[]
)

repo.issue(3).edit(
    title='issue2',
    body="issue2 milestone 0.0.1\nbug, needs decision\nassigned to me",
    assignee='jantman',
    state='open',
    milestone=1,
    labels=['bug', 'needs decision']
)

repo.issue(4).edit(
    title='issue 3 closed',
    body="issue 3 closed",
    assignee='',
    state='closed',
    milestone=0,
    labels=[]
)

repo.issue(5).edit(
    title='issue4',
    body="issue4 with pr\ndocs\nmilestone 0.0.2",
    assignee='',
    state='open',
    milestone=2,
    labels=['Docs']
)

repo.issue(8).edit(
    title='closed issue',
    body='testing',
    assignee='',
    state='closed',
    milestone=1,
    labels=['testing']
)
