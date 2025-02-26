from flask import Flask, request, jsonify

app = Flask(__name__)

class User:
    def __init__(self, id, username, password, email=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"id: {self.id}, username: {self.username}, email: {self.email}"

listUsers = [
    User(id=1, username="pare", password="12345", email="pare@gmail.com"),
    User(id=2, username="mare", password="123", email="mare@gmail.com"),
    User(id=3, username="tutor", password="12", email="tutor@gmail.com")
]

class DAOUsers:
    def __init__(self):
        self.users = listUsers
    
    def getUserByUsername(self, username):
        for u in self.users:
            if u.username == username:
                return u
        return None

user_dao = DAOUsers()

@app.route('/tapatapp/getuser', methods=['GET'])
def get_user_by_username():
    username = request.args.get('username', default='', type=str)
    user = user_dao.getUserByUsername(username)
    if user:
        return jsonify(id=user.id, username=user.username, email=user.email)
    else:
        return jsonify(error="User not found"), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")
