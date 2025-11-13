from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'alguma_chave_secreta'

ADMIN_EMAIL = "admin@admin.com"
ADMIN_SENHA = "1234"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha') 

        if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
            session['admin'] = True
            return redirect(url_for('dashboard'))
        else:
            return "Login inválido"

    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if not session.get('admin'):
        return redirect(url_for('login'))
    return render_template("dashboard.html")

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)