from flask import Flask, render_template, jsonify

app = Flask(__name__)


# This route will render index.html
@app.route("/")
def index():
    return "Home"  

@app.route("/encryption/<message>", methods=["GET"])
def encryption(message):

    response = {"Encrypted Message":message[::-1]}
    
    return jsonify(response)

if __name__ == "__main__":
     app.run(debug = True)


     
   