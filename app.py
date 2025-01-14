from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(mode):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = ['!', '@', '#', '$', '%', '&']

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + ''.join(symbols)

    # Determine the number of segments based on mode
    if mode == 'simple':
        segments = 3
    elif mode == 'complex':
        segments = 4
    else:
        return "Invalid mode. Choose 'simple' or 'complex'."

    password = []
    for i in range(segments):
        # Add 4 random characters
        segment = ''.join(random.choices(all_characters, k=4))
        password.append(segment)
        # Add a hyphen (except after the last segment)
        if i < segments - 1:
            password.append('-')

    return ''.join(password)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    mode = 'simple'  # Default mode
    if request.method == 'POST':
        mode = request.form.get('mode', 'simple')
        password = generate_password(mode)
    return render_template('index.html', password=password, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)