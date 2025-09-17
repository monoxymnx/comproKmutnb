import requests

response = requests.get('https://api.github.com/users/monoxymnx')

if response.status_code == 200:
    user_data = response.json()

    print("Username:", user_data['login'])
    print("Name:", user_data['name'])
    print("Bio:", user_data['bio'])
    print("Public Repos:", user_data['public_repos'])
    print("Followers:", user_data['followers'])
    print("Following:", user_data['following'])
else:
    print("Failed to retrieve data:", response.status_code)