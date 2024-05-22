from flask import Flask,render_template,request

app = Flask(__name__)

# jinja2 template use following structure for html

# {%...%} use for conditions, statements
# {{}} expression to print output
# {#...#} use for creating comments

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        input_num = float(request.form['english'])
        return render_template("submit.html",input = input_num)

if __name__ == "__main__":
    app.run(debug=True)