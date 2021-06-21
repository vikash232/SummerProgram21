#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

x = mydata.getvalue("c")


o = subprocess.getoutput("sudo " + x)
print("<center>")
print("Command Run : ",x)

print("<br />")
print("<br />")

print("\t\t\t--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("<br />")
print("<br />")

print(" Your Output is :",o)
print("</center>")
