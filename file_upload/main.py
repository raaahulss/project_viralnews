from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask("IDK")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET','POST'])
@cross_origin()
def main():
    print(request)
    return "Works" # [Object]
    # return "Works"

if __name__ == "__main__":
    app.run()