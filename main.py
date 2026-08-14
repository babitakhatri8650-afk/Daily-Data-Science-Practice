from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=['Get','Post'])
def hello_world():
    print(request.method)
    if(request.method=="Post"):
        with open("file.txt") as f:
            f.write(f"The name is {request.form['name']} and email is {request.form['email']}")

        print(request.form)
    else:
        return render_template("contact.html")


app.run(debug=True)
