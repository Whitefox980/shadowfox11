from flask import Flask, request
app = Flask(__name__)

@app.route("/xss")
def xss():
    q = request.args.get("q", "")
    return f"<html><body>Param: {q}</body></html>"

app.run(host="0.0.0.0", port=8080)
