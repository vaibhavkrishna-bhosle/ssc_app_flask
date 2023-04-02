from flask import (
    Blueprint,
    request,
    g,
    current_app
)
import pandas as pd
from Auth.model import (
    login
)

Auth_bp = Blueprint('Auth',__name__)

@Auth_bp.route('/login', methods=['GET'])
def get_login():
    try:
        #print for debugging
        print("in get_login")
        
        # Get the parameters from the request
        user_name = request.args.get('user_name')
        print("user_name: ",user_name)
        
    except Exception as e:
        error_message = "Error getting parameters: " + str(e)
        print(error_message)
        response = g.create_error_message(error_message)
        return response
    else:
        status,result = login(user_name)
        if not status:
            response = g.create_error_message(result)
        else:
            response = g.create_data_response(result)
        return response