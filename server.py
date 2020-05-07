from flask import Flask,render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html', times = 5)

@app.route('/play/<times>/<color>')
def playTimes(times,color):
    return render_template('play.html',times = int(times), color = color)

if __name__ =="__main__":
    app.run(debug=True)