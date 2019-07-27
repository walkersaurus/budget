#!/home/drewcifer/budget.walkersaurus.com/bin/python3

##################################################################################
###   This module simplifies python-to-html by classifying HTML objects and    ###
###   creating a hierarchy, then allowing a more simplified printing process   ###
##################################################################################

class HTMLobj:
    def __init__(self, tag, attributes="", innerhtml="", parent=""):
        self.tag = tag
        self.attributes = attributes
        self.innerHTML = [innerhtml]

        if isinstance(parent, HTMLobj):
            parent.addInnerHTML(self)
        
        # Determine if HTMLobj requires a closing tag
        self.closeTag = True
        voidTag = ['area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr']
        if (tag in voidTag):
            self.closeTag = False
            self.innerHTML = []

    def addInnerHTML(self, innerValue):
        # This method only works if object is not a void tag
        if self.closeTag:
            self.innerHTML.append(innerValue)

    def addAttribute(self, newAttribute):
        self.attributes += ' ' + newAttribute

    def printHTMLobj(self):
        # Print opening tag 
        if self.closeTag:
            print('<' + self.tag + ' ' + self.attributes + '>')
        else:
            print('<' + self.tag + ' ' + self.attributes + '/>')

        # Loop thru innerHTML list and print each item in list
        for i in self.innerHTML:
            # If innerHTML is a string, print string
            if isinstance(i, str):
                print(i)
            # If innerHTML is another HTML object, printHTMLobj
            elif isinstance(i, HTMLobj):
                i.printHTMLobj()
        # Print closing tag (if necessary)
        if self.closeTag:
            print('</' + self.tag + '>')

class baseHTMLobj(HTMLobj):
    def __init__(self, headDict={}):
        super().__init__('html', 'lang=' + headDict["lang"])

        self.head = headHTMLobj(headDict)
        self.body = HTMLobj('body')

    def printHTMLobj(self):
        print("Content-type:text/html")
        print()
        print("<!DOCTYPE html>")
        print('<html ' + self.attributes  + '>')
        self.head.printHTMLobj()
        self.body.printHTMLobj()
        print('</html>')

class headHTMLobj(HTMLobj):
    def __init__(self, headAttribute={}):
        super().__init__(tag='head')

        if headAttribute["charset"]:
            charsetObj = HTMLobj('meta', attributes='charset="' + headAttribute["charset"] + '"')
            self.addInnerHTML(charsetObj)

        if headAttribute["title"]:
            titleObj = HTMLobj('title', innerhtml=headAttribute["title"])
            self.addInnerHTML(titleObj)

        if headAttribute["description"]:
            descrObj = HTMLobj('meta', attributes='name="description" content="' + headAttribute["description"] + '"')
            self.addInnerHTML(descrObj)

        if headAttribute["author"]:
            authObj = HTMLobj('meta', attributes='name="author" content="' + headAttribute["author"] + '"')
            self.addInnerHTML(authObj)

        if headAttribute["stylesheet"]:
            styleObj = HTMLobj('link', 'rel="stylesheet" type="text/css" href="' + headAttribute["stylesheet"] + '"')
            self.addInnerHTML(styleObj)

        if headAttribute["script"]:
            scrObj = HTMLobj('script', 'src="' + headAttribute["script"] + '"')
            self.addInnerHTML(scrObj)