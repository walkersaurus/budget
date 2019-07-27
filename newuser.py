#!/home/drewcifer/budget.walkersaurus.com/bin/python3

######################################################################################
###   THIS SCRIPT TAKES NEW USER'S INFORMATION AND UPDATES DB, THEN LOGS THEM IN   ###
######################################################################################

import cgi
from custom_py import htmlDOM, dbScripts

def main():

    #####################################################
    ###   Get new user's information, check against   ###
    ###   existing db records, then update db         ###
    #####################################################

    # Create instance of FieldStorage
    loginForm = cgi.FieldStorage()

    # Get data from login form
    fname = loginForm.getvalue('fname')
    lname = loginForm.getvalue('lname')
    uemail = loginForm.getvalue('email')
    uname = loginForm.getvalue('uname')
    pword1 = loginForm.getvalue('pword1')
    pword2 = loginForm.getvalue('pword2')

    try:
        result = dbScripts.addUser(fname, lname, uemail, uname, pword1, pword2)  
    except Exception as e:
        result = 'Error: ' + str(e)

    #######################
    ###   Create HTML   ###
    #######################

    #Set details in head
    headDict = {
        "lang" : "en",
        "title" : "Welcome New User!",
        "charset" : "utf-8",
        "description" : "New User Login",
        "author" : "Drew Walker",
        "stylesheet" : "frontend/budget.css",
        "script" : ""
    }

    # Create base & body Objects
    baseHTML = htmlDOM.baseHTMLobj(headDict)

    # Create HTML objects to go into the body
    header1 = htmlDOM.HTMLobj('h1', innerhtml='Walkersaurus Budget', parent=baseHTML.body)
    p1 = htmlDOM.HTMLobj('p', innerhtml=result, parent=baseHTML.body)

    #Print HTML
    baseHTML.printHTMLobj()

main()