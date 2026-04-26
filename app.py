from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Sinapse API Online!", "status": "success"}

@app.route("/health")
def health():
    return(jsonify(status = "ok", service = "sinapse", version = "1.0.0"))

@app.route("/echo/<text>")
def echo(text):
    return (jsonify(echo=text))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

