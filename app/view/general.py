from flask import g, render_template

from app import app
from app.config import login_manager, APP_MODE
from app.controller import *


@app.context_processor
def get_mode():
    """Выводит в конце страницы 'development', если включен debug и FLASK_ENV=development;
    Если FLASK_ENV=production, то выводит пустую строку"""
    g.mode = ''
    if APP_MODE != "production":
        g.mode = APP_MODE
    return dict(mode=g.mode)


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


@app.route('/')
@app.route('/main')
def main():
    """Открывает начальную страницу"""
    return render_template("main.html")
