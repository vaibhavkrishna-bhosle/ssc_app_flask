from sqlalchemy import create_engine

tns = "(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-hyderabad-1.oraclecloud.com))(connect_data=(service_name=geaa991f6dcda9b_ssc_medium.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"
engine = create_engine('oracle+cx_oracle://username:password@'+tns)
connection = engine.raw_connection()
cursor = connection.cursor()
cursor.execute('SELECT * FROM user_login')
result = cursor.fetchall()
print(result)
cursor.close()