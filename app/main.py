from flask import Flask
from completionCall import call_playlist_prompt

app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks have a good time</h1>"


# @app.route('/post-json', methods=['POST'])
# def handle_json_data():
#     return call_playlist_prompt()



