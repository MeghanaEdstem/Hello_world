from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
	if request.method == 'GET':
		data = {"data": "Hello World"}
		return jsonify(data)

@app.route('/info', methods=['GET'])
def personaldata():
	if request.method == 'GET' :
		personal_data = {"name": "Meghana", "mail_id": "meghana123@gmail.com"}
		return jsonify(personal_data)


@app.route('/input', methods=['POST'])
def input():
   body = request.json
   return body


@app.route('/add', methods=['POST'])
def addition():
    numbers = request.json
    sum = 0
    for number in numbers['numbers']:
        sum = sum + number
    return str(sum)




if __name__ == '__main__':
	app.run(debug=True)


