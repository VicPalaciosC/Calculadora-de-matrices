from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Manual')
def Manual():
    return render_template('Manual.html')

@app.route('/DyD')
def DyD():
    return render_template('DyD.html')

if __name__ == '__main__':
   app.run(debug=True)
