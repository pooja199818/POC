from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def first():
    return render_template('first.html')

@app.route('/second')
def second():
    return render_template('second.html')    

@app.route('/third', methods=['POST'])
def third():
    return render_template('third.html') 


if __name__ == '__main__': 
    app.debug=True  
    app.run(host='0.0.0.0',port=5555)  

