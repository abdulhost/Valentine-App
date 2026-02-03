from flask import Flask, render_template

app = Flask(__name__)

# Landing page
@app.route("/")
def landing():
    return render_template("index.html")

# Memories page
@app.route("/memories")
def memories():
    return render_template("memories.html")

# Quiz page
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

# Promises page
@app.route("/promises")
def promises():
    return render_template("promises.html")

# Final page
@app.route("/final")
def final():
    return render_template("final.html")

# Flower page
@app.route("/flower")
def flower():
    return render_template("flower.html")


if __name__ == "__main__":
    app.run(debug=True)
