import cx_Oracle
import os
from flask import Flask, jsonify, render_template
import datetime

os.environ['TNS_ADMIN'] = ".\Wallet_SSC"


def get_user_logins():
    connection = cx_Oracle.connect('admin', 'SatyamSSC@12#', 'ssc_medium')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user_login')
    result = cursor.fetchall()
    cursor.close()
    return result

user_logins = get_user_logins()

print(user_logins)