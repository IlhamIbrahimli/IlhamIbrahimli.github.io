from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")
@app.route("/about")
def about():
  return render_template("about.html")
@app.route("/exp")
def exp():
  return render_template("exp.html")
@app.route("/edu")
def edu():
  return render_template("edu.html")
@app.route("/contact")
def contact():
  return render_template("contact.html")
if __name__ == "__main__":
  app.run()