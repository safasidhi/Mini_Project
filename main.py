from flask import *
from public import public
from admin import admin
from user import user

app=Flask(__name__)

# Error handler for 404 Not Found errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('pages-error-404.html'), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('pages-error-404.html'), 500


app.secret_key="qwerty"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(user,url_prefix="/user")

app.run(debug=True,host="0.0.0.0")