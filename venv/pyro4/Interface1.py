from flask import Flask

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def my_form():
    return render_template('my-form.html')