import mysql.connector
from mysql.connector import Error

print("Start of a Python Database Programming Exercise\n")


try:
        connection = mysql.connector.connect(host='classdb.it.mtu.edu',
                                             port='3307',
                                             database='byteme',
                                             user='byteme_rw',
                                             password='password')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)

            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print ("you're connected to - ", record)


            sql_select_Query = "select * from isPartOf"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            print("Total number of rows in isPartOf is - ", cursor.rowcount)
            print ("Printing each row's column values")
            for row in records:
                print("username = ", row[0] )
                print("group_name = ", row[1] )
                print("isHost = ", row[2] )
                

            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

except Error as e:
        print ("error while connecting to MySQL", e)
finally:

    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

#readDbVersion()

print("End of a Python Database Programming Exercise\n\n")
