from flask import Flask, request, jsonify
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id)

listUsers = [
    User(1, "usuari", "12345", "prova@gmail.com"),
    User(2, "user2", "123", "user2@proven.cat"),
    User(3, "admin", "12", "admin@proven.cat")
]

for u in listUsers:
    print(u)

class DAOUsers:
    def __init__(self):
        self.users = listUsers

    def getUserByUsername(self, username):
        for u in self.users:
            if u.username == username:
                return u
        return None

daoUser = DAOUsers()

print(daoUser.getUserByUsername("pare"))
u = daoUser.getUserByUsername("notrobat")
if u:
    print(u)
else:
    print("notrobat")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Benvingut a Tapatapp"

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify(id=user.id, username=user.username, email=user.email)
    else:
        return jsonify(error="User not found"), 404

@app.route('/users', methods=['GET'])
def get_users():
    users = [{"id": u.id, "username": u.username, "email": u.email} for u in daoUser.users]
    return jsonify(users)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(id=len(daoUser.users) + 1, username=data['username'], password=data['password'], email=data['email'])
    daoUser.users.append(new_user)
    return jsonify(id=new_user.id, username=new_user.username, email=new_user.email), 201

if __name__ == '__main__':
    app.run(debug=True)

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id)

listUsers = [
    User(1, "pare", "12345", "prova@gmail.com"),
    User(2, "mare", "123", "user2@proven.cat"),
    User(3, "tutor", "12", "admin@proven.cat")
]

for u in listUsers:
    print(u)

class DAOUsers:
    def __init__(self):
        self.users = listUsers

    def getUserByUsername(self, username):
        for u in self.users:
            if u.username == username:
                return u
        return None

daoUser = DAOUsers()

print(daoUser.getUserByUsername("pare"))
u = daoUser.getUserByUsername("notrobat")
if u:
    print(u)
else:
    print("notrobat")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Bienvenido Tapatapp"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/user/<username>', methods=['GET'])

def get_user(username):
    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify(id=user.id, username=user.username, email=user.email)
    else:
        return jsonify(error="User not found"), 404

import requests

response = requests.get('https://api.example.com/data')

# Comprobar el estado de la respuesta
if response.status_code == 200:
    print("La solicitud fue exitosa")
    print("Contenido de la respuesta:", response.json())
else:
    print("Hubo un error en la solicitud:", response.status_code)

