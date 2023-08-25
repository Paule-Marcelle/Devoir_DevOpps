import os
import subprocess
import requests 

def Arborescence():
    project_name = input("The project's name : ")
    target = os.path.join(os.getcwd(), project_name)
    os.makedirs(target)

    folders = ["data/raw", "data/cleaned", "docs",
               "models", "notebooks", "reports", "src"]

    files = ["LICENSE", "Makefile", "README.md", ".gitignore",
             "requirements.txt", "src/utils.py", "notebooks/main.ipynb"]

    for folder in folders:
        os.makedirs(os.path.join(target, folder))

    for file in files:
        file_path = os.path.join(target, file)
        with open(file_path, 'w') as f:
            file_content = ''
            f.write(file_content)

def repository(repos_name,url_path="https://github.com/Paule-Marcelle/Devoir_DevOpps"):
    get_token= input ("Give your access token")

    result = requests.post(f"{url_path}/user/repos", json=data, headers={
        "Authorization": f"Bearer {get_token}"
    })
    return result.json()['clone_url']

def add(target,addition="."):
    subprocess.run(["git", "add", "origin",repos_url], cwd=target)

def makeCommit(target, message="Initialise the commits"):
    subprocess.run(["git", "commit", "-m", "message"], cwd=target)

def push(target, branch= 'master'):
    subprocess.run(["git", "push", "-u", "origin", branch], cwd=target)

Arborescence()
add(target)
makeCommit()
push()