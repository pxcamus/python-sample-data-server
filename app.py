from flask import render_template
from connexion import FlaskApp

app = FlaskApp(__name__)
app.add_api("swagger.yaml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)