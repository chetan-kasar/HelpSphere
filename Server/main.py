from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
genai.configure(api_key='AIzaSyAMjsZilyZXxmG3mVDmqb6Y4D30ZX-GwNs')

app = Flask(__name__)
CORS(app)
model = genai.GenerativeModel('gemini-pro')

@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    response = model.generate_content(data.get("prompt"))
    return (response.text)

if "__main__" == __name__:
    app.run(debug=True)
