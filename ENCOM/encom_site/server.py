from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('main.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/courses.html')
def courses():
    return render_template('courses.html')

@app.route('/snake.html')
def snake():
    return render_template('snake.html')

@app.route('/platformer.html')
def platformer():
    return render_template('platformer.html')

@app.route('/shooter.html')
def shooter():
    return render_template('shooter.html')

@app.route('/drift.html')
def drift():
    return render_template('drift.html')            

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')