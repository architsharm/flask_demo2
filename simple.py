from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping")
def ping():
    return "This is ping"



def square(a):
    return a*a     


@app.route("/hello/<username>")
def hello_user(username):
    return "Hello {}".format(username)



@app.route("/random", methods=['POST'])
def post_example():
    return "Hello POST"

# @app.route("/random", methods=['GET'])
# def post_example2():
#     return "Hello GET"
