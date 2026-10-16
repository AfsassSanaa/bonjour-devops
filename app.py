from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
   return "Bonjour depuis mon PC !"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)