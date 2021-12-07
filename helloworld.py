from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Tello, world!'

if __name__ == '__main__':
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
