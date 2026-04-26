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

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Not Found", message="Rota inexistente"), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify(error="Internal Server Error", message="Erro inesperado"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

