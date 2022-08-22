import requests


class GitApi():

    def consume_git_api():
        url = 'https://api.github.com/users/stackbuilders/repos'
        
        response = requests.get(url)

        if response.status_code == 200:
            repos = response.json()
        else: 
            repos = "API error"
        
        print(repos)

        return repos
