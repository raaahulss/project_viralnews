# from flask import Flask, request
# import requests
# app = Flask(__name__)
# scrapping_url = "https://embed.ly/docs/explore/extract?url="
# apikey = "1934f519a63e142e0d3c893e59cc37fe0172e98a"

# @app.route('/result', methods = ['GET', 'POST'])
# def result():
#     if request.method == 'GET':
#         url = request.args.get('url', None)
#         print(request.args)
#         if url:
#             print("here",url)
#             r = requests.get(url)
#             return r.text
#         return "No url information is given"


# if __name__ == '__main__':
#     app.run(debug = True)
import src


app = src.main()


if __name__ == '__main__':
    app.run(host="127.0.0.1")
