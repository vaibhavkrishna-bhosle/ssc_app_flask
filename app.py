from flask import Flask, jsonify, render_template
import datetime
from sqlalchemy import create_engine


def get_user_logins():
    tns = "(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-hyderabad-1.oraclecloud.com))(connect_data=(service_name=geaa991f6dcda9b_ssc_medium.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"
    engine = create_engine('oracle+cx_oracle://admin:SatyamSSC#12#@'+tns)
    connection = engine.connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user_login')
    result = cursor.fetchall()
    cursor.close()
    return result

app = Flask(__name__)
@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0)
                   ]

    return render_template('index.html', times=dummy_times)


@app.route('/user_logins', methods=['GET'])
def user_logins():
    user_logins = get_user_logins()
    return jsonify(user_logins)

if __name__ == '__main__':
    print("Starting Python Flask Server For User Logins")
    app.run(host='127.0.0.1', port=8080, debug=True)