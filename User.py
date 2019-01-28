from flask import Flask
from flask import jsonify
import mysql.connector
from flask_restful import Resource, Api


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="learnapp"
)

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self, username,password):
        mycursor = mydb.cursor()
        adr = (username,password,)
        mycursor.execute("SELECT * FROM user where username= %s and  password=%s", adr)
        myresult = mycursor.fetchall()
        data = []
        for i in myresult:
            data.append({
                'id': i[0],
                'name': i[1],
                'username': i[2],
                'email': i[3],
                'phone': i[5],
                'class_id': i[6]
            })
        return jsonify({"status": 200, "data": data, "message": "success"})

    def get2(self, username):
        mycursor = mydb.cursor()
        adr = (username,)
        mycursor.execute("SELECT * FROM user where username= %s", adr)
        myresult = mycursor.fetchall()
        data = []
        for i in myresult:
            data.append({
                'id': i[0],
                'name': i[1],
                'username': i[2],
                'email': i[3],
                'phone': i[5],
                'class_id': i[6]
            })
        return jsonify({"status": 200, "data": data, "message": "success"})


class App(Resource):
    @app.route('/')
    def hello_world(self):
        return 'Hello World!'

    @app.route('/login', methods=['GET'])
    def login(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        data = []
        for i in myresult:
            data.append({
                'id': i[0],
                'name': i[1],
                'username': i[2],
                'email': i[3],
                'phone': i[5],
                'class_id': i[6]
            })
        return jsonify({"status": 200,
                        "data": data,
                        "message": "success"
                        })


api.add_resource(User, '/usr/login/<username>/<password>')
api.add_resource(User, '/usr/login/<username>')
# api.add_resource(App,'/login')

if __name__ == '__main__':
    app.run(debug=True)







