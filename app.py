from flask import Flask,render_template

app = Flask(__name__)

student:list = [
    {"idno":"1000","lastname":"lopez","firstname":"jane","course":"bsit","level":"3",},
    {"idno":"2000","lastname":"gomez","firstname":"frank","course":"bsit","level":"2",},
    {"idno":"3000","lastname":"edem","firstname":"kim","course":"bsit","level":"4",},
    {"idno":"4000","lastname":"glydel","firstname":"princess","course":"bsit","level":"1",},
    {"idno":"5000","lastname":"durano","firstname":"dennis","course":"bsit","level":"3",},

]
@app.route("/")
def index()->None:
	return render_template("index.html",data = student,pagetitle="STUDENT LIST")
    
if __name__=="__main__":
	app.run(debug=True)