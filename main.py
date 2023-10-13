from github import Auth, Github
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv('.env')
MY_GITHUB_TOKEN = os.getenv('MY_GITHUB_TOKEN')
auth = Auth.Token(token=MY_GITHUB_TOKEN)
g = Github(auth=auth)
g.get_user().login

filename = f"commits/{str(datetime.now())}.txt"
filecontent = f"This is a new commit on {datetime.now()}"

repo = g.get_repo('hossein-roshandel/autocommit-to-github')
repo.create_file(path=filename, 
                 message='Updating autocommits file', 
                 content=filecontent, 
                 branch='autocommits')

pull_request_body = f'''
SUMMARY
Add another autocommit file

TESTS
  - [x] Authenticate to Github at {datetime.now()}
  - [x] Send an automated pull request for {datetime.now()}
  - [x] Check the pull request at {datetime.now()}
  - [x] Set everything on a cron job :)
'''
pr = repo.create_pull(base="master", head="develop", title="Good job! Keep it up!", body=pull_request_body)

