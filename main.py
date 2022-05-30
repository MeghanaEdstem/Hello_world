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



if __name__ == '__main__':
	app.run(debug=True)


