from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Task 22 - Kubernetes CI/CD and GitOps</h1>
    <h2>Flask Application is Running Successfully!</h2>
    <p>Developed by Ninusri PS</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
