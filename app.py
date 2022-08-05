from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '5f145fdeec2850'
app.config['MAIL_PASSWORD'] = 'c750cc5e4f51ab'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']
        print(email)
        msg = Message('Hello', sender='no-reply@travens.id', recipients=[email])
        msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
        msg.html = '<b>Hey Paul</b>, sending you this email from my <a href="https://google.com">Flask app</a>, lmk if it works'
        with app.open_resource("document.pdf") as fp:  
            msg.attach("document.pdf", "application/pdf", fp.read())  
        mail.send(msg)
        return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)