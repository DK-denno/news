from flask import render_template
from app import app
from .request import get_sources, get_articles


@app.route('/')
def index():

    display = get_sources()

    return render_template('index.html', display=display)


@app.route('/news/<id>')
def articles(id):

    articles_display = get_articles(id)

    return render_template('news.html',articles = articles_display)
