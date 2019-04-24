import mysql.connector
from mysql.connector import Error

def findActiveGroups(usrID,txt):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from isPartOf natural join GroupPlaying where username="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        text=""
        try:
            for row in records:
                text=(row[0]+"\n")
                
        except:
            print("No active groups")
        finally:
            txt.insert(INSERT,text)

#Finds all groups where user i host. 
def findMyGroups(usrID,txt):
    if (connection.is_connected()):
        sqlQuery = "select group_name from Groups where host_name="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        text=""
        try:
            for row in records:
                text=(row[0]+"\n")
        except:
            print("No active groups")
        finally:
            txt.insert(INSERT,text)




#Check if group name is in Group table
def checkGroup(groupName):
    if (connection.is_connected()):
        sqlQuery = "select group_name from Groups where group_name="+"'"+groupName+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==groupName
            return True
        except:
            return False


#Check if user is already a part of the group:
def checkJoin(groupName):
    if (connection.is_connected()):
        sqlQuery = "select username from isPartOf where group_name="+"'"+groupName+"' and username="+"'"+usrID+"';"
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            for row in records:
                if row==usrID:
                    print("User already part of group")
                    return True #User is already part of the group
                else:
                    print("User is not part of group")
                    return False
        except:
            print("User is not part of group")
            return False
           
    
    
    

#Check if user is in User table, if not it adds the user to User table
def checkUser(usrID):
    global connection
    if (connection.is_connected()):
        sqlQuery = "select username from User where username="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==usrID
            print("already a user!")
            #cursor.close()
            return
        except:
            ##sqlQuery = "insert into User values("+"'"+usrID+"'"+");"
            ##print("user created")
            cursor = connection.cursor()
            args=(usrID)
            cursor.callproc('addUser',args=(usrID,))
            print("user created")
            connection.commit()
            #cursor.close()
            
            
    else:
        connect()
        checkUser(usrID)

#Creating a new group. User is automatically the host
def createGroup(groupName):
    global connection
    connect()
    checkUser(usrID)
    #Check to see that there's not already a group with the same name
    if (not checkGroup(groupName)): 
            cursor = connection.cursor()
            cursor.callproc('addGroup',args=(groupName,usrID,1))
            cursor.callproc('addPart',args=(usrID,groupName,1))
            print("group created")
            cursor.close()
            connection.commit()
            
    else:
         print("groupName already exist, so group can't be created with this name.")
  
def joinGroup(groupName):
    global connection
    connect()
    checkUser(usrID)
    #Check to see that there exist a group with with name 'groupName'
    if(checkGroup(groupName)):
        if(not checkJoin(groupName)):
            sqlQuery = "update Groups set number_user=number_user+1 where group_name="+"'"+groupName+"';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()
            print("Hva")
            sqlQuery = "insert into isPartOf values("+"'"+usrID+"'"+","+"'"+groupName+"'"+",0);"
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            print("group created")
            connection.commit()
            cursor.close()
            listenToGroup(groupName)
    else:
         print("There's no group named"+groupName)
         return
    #Refresh thel list of active and inactive groups in the GUI 
  
#Check if user is host
def checkHost(groupName):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from Groups where group_name="+"'"+groupName+"' and host_name="+"'"+usrID+"';"
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==groupName #This means the user is host
            cursor.close()
            print("The user is Host")
            return True
        except:
            cursor.close()
            return False
            print("The user is not Host")
            
   

#Check if group is avtive, then listens to the group       
def listenToGroup(groupName):
    if isActive(groupName):
        isHost=checkHost(groupName)
        syncGroup=groupName
        syncToGroup(groupName) ##This function needs to check the isHost variable and push/pull accordingly
    else:
        print("Couldn't listen to this group because it's not active")
        
#Check if the host is pushing to the GroupPlaying table, if not give a messege that the host is inactive and that the user can't listen to this group
def isActive(groupName):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from GroupPlaying where group_name="+"'"+groupName+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==groupName #This means the group is active
            cursor.close()
            print("The group is active")
            return True
        except:
            cursor.close()
            return False
            print("The group is not active")
            
    

def connect():
    global connection
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
           

    except Exception as e:
        print ("error while connecting to MySQL", e)





    
def disconnect():
    global connection
    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")






#readDbVersion()

connect()
checkUser('krass')
print("End of a Python Database Programming Exercise\n\n")
