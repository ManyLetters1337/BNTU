from typing import Dict

from flask import Flask, render_template
from celery import Celery
from flask_mail import Mail, Message

from orders.models import Orders
from users.models import Users

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

app.config['MAIL_SERVER'] = 'smtp.yandex.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'some-login-post@yandex.ru'
app.config['MAIL_PASSWORD'] = 'Qwerty123'
app.config['MAIL_DEFAULT_SENDER'] = 'some-login-post@yandex.ru'

mail = Mail(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task()
def send_mail_accept_order(user: 'Dict', order: 'Dict'):
    with app.app_context():
        msg = Message("Заказ №" + str(user['student_number']) + str(order['id']), recipients=[user['email']])
        msg.html = render_template('mail_accept_order.html', user=user, order=order)
        mail.send(msg)


@celery.task()
def send_reset_password_email(user: 'Dict', url: str):
    with app.app_context():
        msg = Message("Восстановление пароля", recipients=[user['email']])
        msg.html = render_template('mail_reset_password.html', user=user, url=url)
        mail.send(msg)
