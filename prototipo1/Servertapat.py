class User:
     def _init_(self, id, username, password, email):
        self.id=id
        self.username=username
        self.password=password
        self.email=email
        
    def _str_(self):
       return "Id"  + str (self.id)




listUsers= [
    User(1, "usuari", "12345", "prova@gmail.com"),
    User(2, "user2", "123", "user2@proven.cat"),
    User(3, "admin", "12", "admin@proven.cat")
]

for u in listUsers:
     print(u)

class DAOUsers:
     def __init__(self):
          self.users=listUsers
     def getUserByUsername(self,username):
        for u in self.users:
             if u.username == username:
                 return u
             
        
         return None

daoUser = DAOUser ()

print(daoUser.getUserByUsername("usuari1"))
u=daoUser.getUserByUsername("notrobat") 
if(u):
    print(u)
else:
    print(notrobat)
      


app = Flask(__name__)

@app.route('/', methods=['GET'])
 def hello():
    return "Hello World"


if __name__ == '_main_':
     
     app.run(debug=True)


