#!/home/drewcifer/budget.walkersaurus.com/bin/python3

from private import dbConnection

def loginTest(uname, pword):

    #Verify that uname isn't null
    if not uname:
        return 'Please enter a username'

    #Verify that pword isn't null
    if not pword:
        return 'Please enter a password'

    ################################################
    ### Access budget-db and query uname & pword ###
    ################################################

    try:
        # Open database connection; dbConnection uses MySQLdb.connect to create a connection to database.
            # This was done to keep db user and password secure
        db = dbConnection.connect()

        # Prepare a cursor object
        cursor = db.cursor()

        # Execute SQL query
        try:
            cursor.execute("SELECT username, userpassw FROM budget_users WHERE username='" + uname + "'")

            # Fetch results of query and compare password
            queryResults = cursor.fetchone()

            if queryResults:
                if pword == queryResults[1]:
                    result = 'Welcome, ' + uname + '!'
                    loggedIn = True
                else:
                    result = 'Incorrect password'
            else:
                result = 'Invalid username'
        except Exception as ex:
            result = 'Unable to query db: ' + str(ex)

        # Disconnect from db
        db.close()
        
    except Exception as e:
        result = 'Could not connect to db: ' + str(e) 

    return result

def addUser(fname, lname, uemail, uname, pword1, pword2):

    ########################################################
    ###   This function adds new userinfo to budget_db   ###
    ########################################################

    # Validate input, Verify passwords
    if not(lname and uemail and uname and pword1 and pword2):
        result = 'New user information incomplete'
    elif pword1 != pword2:
        result = 'Passwords did not match'
    else:
        try:
            # Open database connection; dbConnection uses MySQLdb.connect to create a connection to database.
                # This was done to keep db user and password secure
            db = dbConnection.connect()
            
            # Prepare a cursor object
            cursor = db.cursor()

            #Query uname & email to ensure they are not already in db
            try:
                cursor.execute("SELECT * FROM budget_users WHERE username='" + uname + "' OR useremail='" + uemail + "'")

                queryResults = cursor.fetchone()

                if queryResults:
                    result = 'username or email already in use'
                else:
                    # Add user info to db
                    try:
                        sql = "INSERT INTO budget_users(username, firstname, lastname, useremail, userpassw) " \
                            + "VALUES('" + uname + "', '" + fname + "', '" + lname + "', '" + uemail + "', '" + pword1 + "')"
                        

                        cursor.execute(sql)
                        db.commit()

                        result = 'Welcome, ' + fname + ', you new user!'

                    except Exception as e:
                        db.rollback()
                        result = 'Could not update database with new user info: ' + str(e)

            except Exception as e:
                result = 'Could not query db to verify username and email: ' + str(e)

            # Disconnect from db
            db.close()
        except Exception as e:
            result = 'Could not connect to db: ' + str(e)
        
    return result

    