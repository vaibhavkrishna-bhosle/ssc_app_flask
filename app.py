#create a flask app endpoint to fetch data
from flask import (
    Flask, 
    jsonify, 
    request,
    blueprints,
    g,
    current_app
)
from Auth.view import Auth_bp
import cx_Oracle
import constants
import json
from waitress import serve


def get_connection():
    try:
        connect_string = f'tcps://{constants.host}:{constants.port}/{constants.service_name}?wallet_location=Wallet&retry_count=20&retry_delay=3'
        con = cx_Oracle.connect(constants.db_user, constants.db_password, connect_string)
        cur = con.cursor()
        return True,cur
    except Exception as e:
        error_message = "Error while connecting to Oracle Database: " + str(e)
        print(error_message)
        response = create_error_message(error_message)
        return False,response
    
def create_error_message(error_message):
    response = current_app.response_class(response=json.dumps(error_message).encode('utf-8'), 
                                            status=500, 
                                            mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.status_code = 500
    return response

def create_data_response(response):
    response = current_app.response_class(response=json.dumps(response).encode('utf-8'),
                                            status = 200,
                                            mimetype = 'application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.status_code = 200
    return response
    
app = Flask(__name__)
app.register_blueprint(Auth_bp,url_prefix='')

@app.before_request
def before_request():
    g.get_connection = get_connection
    g.create_error_message = create_error_message
    g.create_data_response = create_data_response

if __name__ == '__main__':
    serve(app, 
        host="127.0.0.1", 
        port=5000, 
        debug=True, 
        url_scheme="https")
    