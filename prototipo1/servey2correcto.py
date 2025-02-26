from flask import Flask, request, jsonify

app = Flask(__name__)

class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email




users= [
    User(1,"pare", "paredesufrir", "priva@gmail.com"),
    User(2,"mare", "marea2", "user2@gmail.cat"),
    User(3,"tutor","tauron","admin@gmail.cat"),
    User(4,"admin2","12", "friquiton200@gmal.cat"),
    User(5,"sapita","2006","peruchita@gmail.com")
]

class UserDAO:
    def __init__(self):
        self.users = users

    def get_all_users(self):
        result = []
        for user in self.users:
            result.append(user.__dict__)
        return result

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None
    
    def get_user_by_username_email_password(self, username, email, password):
        for user in self.users:
            if user.username == username and user.email == email and user.password == password:
                return user.__dict__
        return None

# Inicialitzar DAOs
user_dao = UserDAO()



app = Flask(__name__)



@app.route('/tapatapp/getuser', methods=['GET'])
def getUser():
    n = str(request.args.get('name'))
    email = str(request.args.get('mail'))
    return "bienvenido tapatapp" + " Nom:" + n + " Email:" + email



@app.route('/prototip1/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.get_all_users())

@app.route('/prototip1/getuser', methods=['GET'])
def get_user_by_username_email_password():
    username = request.args.get('username', default="", type=str)
    email = request.args.get('email', default="", type=str)
    password = request.args.get('password', default="", type=str)

    if not username or not email or not password:
        return jsonify({"error": "No encontrado los parametetros: 'username', 'email', or 'password' Son requeridos"}), 400

    user = user_dao.get_user_by_username_email_password(username, email, password)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario con nombre de usuario, correo electrónico y contraseña proporcionados no encontrados"}), 404




@app.route('/hello', methods=['GET'])
def hello():
    user = str(request.args.get('username'))
    
    if not user:
        return jsonify({"error": "Error, l'usuari no es correcte"}), 404
    
    if not request.args.get('email'):
        return jsonify({"error": "Error, Falta una data"}), 400
    
    return jsonify(user_dao.get_user_by_username("usuari1","prova@gmail.com"))


if __name__ == '__main__':
     app.run(debug=True,host="0.0.0.0",port=10050)
