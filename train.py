from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

users = {}

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        if email in users:
            return "User already exists"

        if password != confirm:
            return "Password mismatch"

        users[email] = {
            "name": name,
            "password": password
        }

        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)

        if user and user['password'] == password:
            session['user'] = user['name']
            session['email'] = email
            return redirect('/dashboard')

        return "Invalid credentials"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    user_email = session['email']
    user = users[user_email]

    return render_template('dashboard.html', name=user['name'], email=user_email)

@app.route('/analytics')
def analytics():
  


    return render_template('analytics.html')

@app.route('/request')
def request():
  


    return render_template('request.html')

@app.route('/user_dashboard')
def user_dashboard():
  


    return render_template('user_dashboard.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)