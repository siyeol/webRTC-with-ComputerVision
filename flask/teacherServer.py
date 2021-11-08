from flask import Flask, request, Response

app = Flask(__name__)

IPlist = []
# for CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST') # Put any other methods you need here
    return response



@app.route('/recvIP', methods=['POST'])
def image():
    studentIP = request.get_json()
    global IPlist
    IPlist.append(studentIP)

@app.route('/sendIPlist', methods=['GET'])
def image():
    global IPlist
    return IPlist

if __name__ == '__main__':
	# without SSL

    app.run(debug=True, host='0.0.0.0')
