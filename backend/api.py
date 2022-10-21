from flask import *

app = Flask(__name__)

@app.route("/api/hello")
def index():
    return "hello"
@app.route("/api/comic",methods=['GET'])
def get_comic():
    json = [
            {"title":"chainsaw-man","author":"Tatsuki Fujimoto"},
            {"title":"jujutsu-kaisen","author":"Gege Akutami"},
            {"title":"my-hero-academia","author":"Kohei Horikoshi"},
            {"title":"kisei-ju","author":"Hitoshi Iwaaki"}]
    return jsonify(json)