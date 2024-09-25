from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True


@app.route('/')
def hi_world():
    return 'Hi, World!'


@app.route('/second')
def second():
    return 'Second Function Response'


if __name__ == '__main__':
    app.run(debug=True)
    
