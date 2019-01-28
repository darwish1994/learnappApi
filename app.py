from flask import Flask
from flask import jsonify, make_response, request
import mysql.connector
from flask_restful import Resource, Api

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="learnapp"
)

app = Flask(__name__)


@app.route('/usr/login/', methods=[ 'POST'])
def get():
    mycursor = mydb.cursor()
    adr = (request.args.get("username"), request.args.get("password"),)
    try:
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
            if len(myresult) > 0:
                return jsonify({"status": 200, "data": data, "message": "success"})
            else:
                return jsonify({"status": -1, "data": "", "message": "fail to login"})
    except NameError:
        return jsonify({"status": -1, "data": "", "message": "fail to login"})
    return jsonify({"status": -1, "data": "", "message": "fail to login"})


@app.route('/usr/register', methods=['POST'])
def addNewUser():
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO user (name,username,email,password,phone,claas_id) VALUES (%s, %s,%s,%s,%s,%s)"
        val = (request.args.get("name"),
               request.args.get("username"),
               request.args.get("email"),
               request.args.get("password"),
               request.args.get("phone"),
               request.args.get("class"))

        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount > 0:
            return jsonify({
                'status': 200,
                'message': "user inserted"
            })
    except Exception as e :
        return jsonify({
            'status': -1,
            'message': str(e)
        })


@app.route('/', methods=['GET'])
def home():
    return "<header>hello to new api " + request.args.get("id") + "</header>"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found data'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
