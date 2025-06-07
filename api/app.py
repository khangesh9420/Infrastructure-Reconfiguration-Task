from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Khangesh's API!</h1>
    <p>You have reached the home page.</p>
    <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/devops">DevOps Introduction</a></li>
        <li><a href="/find">Find New Tools</a></li>
        <li><a href="/api/message">API Message (JSON)</a></li>
    </ul>
    """

@app.route('/about')
def about():
    return """
    <h1>About</h1>
    <p>This is a simple Flask API created by Khangesh.</p>
    <p>It demonstrates routing and serving multiple pages.</p>
    <a href="/">Back to Home</a>
    """

@app.route('/devops')
def devops_intro():
    return """
    <h1>DevOps Introduction</h1>
    <p>DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).</p>
    <p>Its goal is to shorten the systems development life cycle and provide continuous delivery with high software quality.</p>
    <ul>
        <li>Continuous Integration (CI)</li>
        <li>Continuous Delivery/Deployment (CD)</li>
        <li>Infrastructure as Code</li>
        <li>Monitoring and Logging</li>
    </ul>
    <a href="/">Back to Home</a>
    """
@app.route('/find')
def find():
    return """
    <h1>Find New Tools</h1>
    <p>There are alwys New tools are present in the market specially cloud native tools.</p>
    <p>Its goal is to spread knowledge about new tools.</p>
    <ul>
        <li>K8 (CI)</li>
        <li>ArgocCD (CD)</li>
        <li>Terraform</li>
        <li> prometheus + Grafana</li>
    </ul>
    <a href="/">Back to Home</a>
    """

@app.route('/api/message')
def api_message():
    return jsonify({"message": "Hello Khangesh! You have reached the API endpoint."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
