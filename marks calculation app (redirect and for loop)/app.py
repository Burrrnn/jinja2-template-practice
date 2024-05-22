from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/result",methods=["POST"])
def result():
    if request.method == "POST":
        score = float(request.form['computer'])
        res =""
        if score>50:
            res="SUCCESS"
        else:
            res="FAIL"
        dict = {'score': score, "result": res}
        return render_template("results.html", results=dict)



@app.route("/success/<int:score>",methods=["GET"])
def success(score):
        res =""
        if score>50:
            res="SUCCESS"
        else:
            res="FAIL"
        dict = {'score': score, "result": res}
        return render_template("results.html", results=dict)


@app.route("/fail/<int:score>", methods=["GET"])

def fail(score):
        res =""
        if score>50:
            res="SUCCESS"
        else:
            res="FAIL"
        dict = {'score': score, "result": res}
        return render_template("results.html", results=dict)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        maths=float(request.form['maths'])
        physics=float(request.form['physics'])
        science=float(request.form['science'])
        
        average = (maths+physics+science)/3
        
        return render_template("form.html",score= int(average))


@app.route("/redirect_to",methods=["GET","POST"])
def redirect_to():
    if request.method == "GET":
        return render_template("redirect.html")
    elif request.method == "POST":
        maths=float(request.form['maths'])
        physics=float(request.form['physics'])
        science=float(request.form['science'])
        
        average = (maths+physics+science)/3

        return render_template("redirect.html",score=int(average))


if __name__ == "__main__":
    app.run(debug=True)
    