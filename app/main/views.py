from flask import render_template
from app import app
from .request import get_sources, get_articles


@app.route('/')
def index():

    sports = get_sources('sports')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    general = get_sources('general')
    health = get_sources('health')
    science = get_sources('science')
    technology = get_sources('technology')

    return render_template('index.html',
                           sports=sports,
                           business=business,
                           technology=technology,
                           entertainment=entertainment,
                           general=general,
                           health=health,
                           science=science,)


@app.route('/news/<id>')
def articles(id):

    articles_display = get_articles(id)
   
    return render_template('news.html', articles=articles_display,)
