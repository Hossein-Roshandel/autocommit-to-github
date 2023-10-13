from github import Auth, Github
from dotenv import load_dotenv
import os
from datetime import datetime
import random

TOTAL_RANDOM_FACTOR = 0.2
PR_RANDOM_FACTOR = 0.4

def main():
    #load_dotenv('.env') 
    load_dotenv("/app/.env") # to match docker container path
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


    pulls = repo.get_pulls(state='open', sort='created', base='main')
    if pulls.totalCount == 0 and random.random()<PR_RANDOM_FACTOR:
        pull_request_body = f'''
        SUMMARY
        Add another autocommit file {datetime.now()}

        TESTS
        - [x] Authenticate to Github at {datetime.now()}
        - [x] Send an automated pull request for {datetime.now()}
        - [x] Check the pull request at {datetime.now()}
        - [x] Set everything on a cron job :)
        '''
        pr = repo.create_pull(base="main", head="autocommits", title=f"Good job! Keep it up! At {datetime.now()}", body=pull_request_body)
        print(f"Commit and PR created at {datetime.now()}")
    else:
        print(f"Only a new file created at {datetime.now()}")

if __name__ == "__main__":
    random_num = random.random()
    if  random_num<TOTAL_RANDOM_FACTOR:
        main()
    else:
        print(f"Nothing happened at {datetime.now()} with {random_num}")