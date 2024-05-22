from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/home",methods=["GET","POST"])
def home():
    if request.method== "GET":
        return render_template("index.html")
    else:
        num = float(request.form['english'])
        return render_template("index.html",score=num)

if __name__ == "__main__":
    app.run(debug=True)