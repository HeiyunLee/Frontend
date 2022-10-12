from flask import Flask, render_template, request, redirect, url_for
import sys 
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("hello.html")

@application.route("/apply")
def apply():
    return render_template("apply.html")

@application.route("/applyphoto")
def photo_apply():
    location = request.args.get("location")
    cleaness = request.args.get("cleaness")
    built_in = request.args.get("built")
    print(location, cleaness, built_in)
    # return render_template("applyphoto.html")

@application.route("/upload_done", methods = ["post"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}/jpeg".format(1))
    
    return redirect(url_for("hello"))

@application.route("/")
def list():
    return render_template("list.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0')
