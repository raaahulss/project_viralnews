from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from random import choices
app = Flask("IDK")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

public_article_return = {
  "published": True,
  "models": {
    "viralness": 0.5,
    "sentiment": 0.5,
  },
  "details": {
    "title": "abc",
    "source": "def",
    "authors": "ghi",
    "published_date": "1591080596",
    "content": "jkl",
    "op_url": "www.mno.com"
  },
  "error" : ""
}

twitter_url = {
  "published": True,
  "models": {
    "viralness": 0.5,
    "sentiment": 0.5,
    "public_opinion": 0.5
  },
  "details": {
    "title": "abc",
    "source": "def",
    "authors": "ghi",
    "published_date": "1591080596",
    "content": "jkl",
    "op_url": "www.mno.com"
  },
  "metrics": {
    "retweets": 123,
    "favourites": 123,
    "responses": 123,
    "trending": True,
  },
  "error": ""
}

file_upload_resp= {
  "published": False,
  "models": {
    "viralness": 0.5,
    "sentiment": 0.5,
  },
  "details": {
    "title": "abc",
    "source": "",
    "authors": "",
    "published_date": "",
    "content": "jkl",
    "op_url": ""
  },
  "metrics": "",
  "error": ""
}
error = {
    "error": {
      "err_code" : "ERR_ABC",
      "err_msg" : "Error : This error suggests probability is not on your side."
  }
}


@app.route("/api/url", methods=['GET','POST'])
@cross_origin()
def url_upload():
    population = [0,1,2]
    weights = [0.33,0.33,0.33]
    choice = choices(population, weights)[0]
    print(choice)
    if choice == 0:
        return  jsonify(public_article_return )# [Object]
    elif choice == 1:
        return jsonify(twitter_url)
    else :
        return jsonify(error)
    # return "Works"

@app.route("/api/file", methods=['GET','POST'])
@cross_origin()
def file_upload():
    # print(request)
    population = [0,1]
    weights = [0.5,0.5]
    choice = choices(population, weights)[0]
    if choice == 0:
        return jsonify(file_upload_resp) # [Object]
    else :
        return jsonify(error)
    # return error
    # return "Works"
 









if __name__ == "__main__":
    app.run()