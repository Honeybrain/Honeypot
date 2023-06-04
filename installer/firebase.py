import requests

def create_account(username, password):
    signup_url = 'http://localhost:8000/user/signup'
    data = {
        'password': password,
        'email': username
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(signup_url, json=data, headers=headers)

    if response.status_code == 200:
        print('User created successfully')
        print(response.json())
    else:
        print(f'Error creating user: {response.text}')
        raise Exception(f"Could not create user.")