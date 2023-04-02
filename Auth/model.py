from flask import (
    g,
    current_app
)
import json

def login(user_name):
    try:
        status,cur = g.get_connection()
        if not status:
            error_message = "Error while connecting to Oracle Database: " + str(e)
            print(error_message)
            response = g.create_error_message(error_message)
            return False,response
        cur.execute(f"select user_password,user_role from user_login where user_name = '{user_name}'")
    except Exception as e:
        error_message = "Error while fetching data from Oracle Database: " + str(e)
        print(error_message)
        response = g.create_error_message(error_message)
        return False,response
    else:
        result = cur.fetchall()
    finally:
        cur.close()
        return True,result