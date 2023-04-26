from flask import flask
from flask import render_template
app = flask (__name__)
#ruteo de mi pagina
@app.route('/') 
def index():
    return render_template('empleados/index.html')

    if __name__== '__main__':
        app.run(debug =true)