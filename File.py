from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pp.html')

if __name__ == '__main__':
    port = 50
    app.run(host='0.0.0.0', port=port, debug=True)
