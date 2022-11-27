from flask import Flask, render_template, request
MyApp = Flask(__name__)


# From Browser: http://127.0.0.1/add?num1=2&num2=3

@MyApp.route('/')
def home():
    # return "Hello World"
    return render_template("home.html")

@MyApp.route('/add')
def addRoute():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    Sum_result = str(n1+n2)
    return render_template("output.html", sum=Sum_result, num1=n1,num2=n2)

if __name__ == "__main__":
    MyApp.run(debug=True,port=8000)
    # MyApp.run()
