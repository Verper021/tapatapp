import requests

def get_user_by_username(username):
    url = "http://0.0.0.0:10050/tapatapp/getuser"
    params = {'username': username}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print("User found:", response.json())
    else:
        print("Error:", response.json())

if __name__ == "__main__":
    username = input("Enter username to search: ")
    get_user_by_username(username)