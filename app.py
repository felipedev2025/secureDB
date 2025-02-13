from flask import Flask, render_template
from database import session, AccessLog

app = Flask(__name__)

@app.route("/")
def index():
    logs = session.query(AccessLog).order_by(AccessLog.timestamp.desc()).limit(10).all()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
  
