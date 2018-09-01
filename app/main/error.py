from app import app
from flask import render_template
@app.errorhandler(404)
def no_page(error):
    '''
    this function returns the template error.html in the case of an error 404/page not found error
    we pass in the 404 in the route as it is the expected error code in case a page is not found
    '''

    return render_template('error.html'),404