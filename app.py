from flask import render_template, redirect, Flask

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html", name="Michael")

if __name__ == "__main__":
    app.run()