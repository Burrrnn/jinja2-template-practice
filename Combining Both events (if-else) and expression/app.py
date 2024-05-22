from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/home", methods=["GET","POST"])
def home():
    if request.method== "GET":
        return render_template("index.html")
    elif request.method=="POST":
        number = float(request.form['english'])
        return render_template("index.html",score=number)


@app.route("/next",methods=["POST"])
def next():
    if request.method == "POST":
        number = float(request.form['maths'])
        return render_template("next.html",score=number)


if __name__ == "__main__":
    app.run(debug=True)