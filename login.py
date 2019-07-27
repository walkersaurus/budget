#!/home/drewcifer/budget.walkersaurus.com/bin/python3

import cgi 
from custom_py import htmlDOM, dbScripts

def main():

    loggedIn = False

    ########################################################
    ###   Get username and password from landing page    ###
    ###   and compare to usernames and passwords in db   ###
    ########################################################

    # Create instance of FieldStorage
    loginForm = cgi.FieldStorage()

    # Get data from login form
    uname = loginForm.getvalue('uname')
    pword = loginForm.getvalue('pword')

    # Get result of login query
    result = dbScripts.loginTest(uname, pword)

    #######################
    ###   Create HTML   ###
    #######################

    # Set details in head
    headDict = {
        "lang" : "en",
        "title" : "Login",
        "charset" : "utf-8",
        "description" : "Logs user into budget app",
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