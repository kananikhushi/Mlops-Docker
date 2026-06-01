from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <form action="/greet" method="post">
            Enter your name:
            <input type="text" name="name">
            <input type="submit" value="Greet me!">
        </form>
    </body>
    </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['name']
    return f'Hello, {user_input}! Welcome to Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)