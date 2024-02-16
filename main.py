from flask import Flask, url_for, redirect 
import settings as stg

app = Flask(__name__, static_folder=stg.PATH_STATIC )
app.config["SECRET_KEY"] = stg.SECRET_KEY
@app. route("/")
def index():
    url = url_for ("static", "templates/index.html")
    return redirect(url)

@app.route("/post/category")
def post_category():
    return "ТУТ БУДУТЬ КАТЕГОРІЇ ПОСТІВ"

app.run(debug=True)
