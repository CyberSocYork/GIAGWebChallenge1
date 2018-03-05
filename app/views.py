from flask import Flask, render_template, request, url_for,redirect
from app import app, validate


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/authenticate',methods=['POST','GET'])
def authenticate():

    validate.validated = True

    return ""


@app.route('/keyPage',methods=['GET'])
def keyPage():

    if request.method =="GET":

        if validate.validated:
            return ("""<html><head></head><body><p>the key is : 4436nZvfEEz8 <p></body></html>""")
        else:
            return ("""<html><head></head><body><p>404 not found <p></body></html>""")



if __name__ == '__main__':
    app.run()
