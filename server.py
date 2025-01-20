from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the issue1 page
@app.route('/issue1')
def issue1():
    return render_template('issue1.html')

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5001)