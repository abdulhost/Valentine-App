from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'enchanted-book-key')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/chapter1')
def chapter1():
    return render_template('chapter1.html')

@app.route('/chapter2')
def chapter2():
    return render_template('chapter2.html')

@app.route('/chapter3')
def chapter3():
    return render_template('chapter3.html')

@app.route('/final', methods=['GET', 'POST'])
def final():
    if request.method == 'POST':
        vibe = request.form.get('vibe')
        preference = request.form.get('preference', '')
        msg = Message(
            subject="Valentine Vibe from My Rasmalai 💕",
            recipients=[os.environ.get('YOUR_EMAIL', 'your@gmail.com')],
            body=f"Vibe: {vibe}\nAdditional Preference/Message: {preference}\n\nCan't wait, babee!"
        )
        try:
            mail.send(msg)
            flash("Your vibe reached my heart, sweetheart! Celebration unlocked. 🎉", "success")
        except Exception as e:
            flash(f"Page-turn error: {str(e)}. Try again?", "error")
        return redirect(url_for('final'))
    return render_template('final.html')

if __name__ == '__main__':
    app.run(debug=True)