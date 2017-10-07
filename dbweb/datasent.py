#!/usr/bin/python
print "Content-Type: text/html \n"

import cgi
import mysql.connector as mdb

# get data from the form
formData = cgi.FieldStorage()

name = formData.getvalue('name') or ""
phone = formData.getvalue('phone') or ""
email = formData.getvalue('email') or ""
home = formData.getvalue('address') or ""
drama = formData.getvalue('drama') or ""
time = formData.getvalue('time') or ""
quantity = formData.getvalue('quantity') or ""
delivery = formData.getvalue('delivery_mode') or ""
payment = formData.getvalue('payment') or ""

# validate the data input
msg = ""
def validate():
    global msg
    if name == "" :
        print "<font color=red>Please enter Name</font>"
        msg = "error"
        return
    if phone == "" :
        print "<font color=red>Please enter Phone Number</font>"
        msg = "error"
        return
    if email == "" :
        print "<font color=red>Please enter your Email Address</font>"
        msg = "error"
        return
    if home == "" :
        print "<font color=red>Please enter your Home Address</font>"
        msg = "error"
        return
    if drama == "" :
        print "<font color=red>Please select Drama</font>"
        msg = "error"
        return
    if time == "" :
        print "<font color=red>Please select Time</font>"
        msg = "error"
        return
    if quantity == "" :
        print "<font color=red>Please select Ticket Quantity</font>"
        msg = "error"
        return
    if delivery == "" :
        print "<font color=red>Please select Delivery Method</font>"
        msg = "error"
        return
    if payment == "" :
        print "<font color=red>Please select Payment Method</font>"
        msg = "error"
        return

# transfer data into the databse
def saveDB():
    sql = "INSERT INTO ticket"
    sql += " VALUES(" + str(0) + ",'" + name + "','" + phone + "','" + email + "','"+ home + "','"+ drama + "','"+ time +"','"+ quantity + "','"+ delivery + "','"+ payment + "');"
    try:
        dbConn = mdb.connect( host = 'oit2.scps.nyu.edu', user = 'shen', password='shen', database = 'shen')
        cursor = dbConn.cursor()
        cursor.execute(sql)
        dbConn.commit()
    except mdb.Error as e:
        errorNum = e.errno
        errorMsg = e.msg
        msg = 'Database Error - ' + str(errorNum) + errorMsg
        return

    print "<b>Your order has been saved successfully</b>";
    print "<table border = 1>"
    print "<tr> <th> Name </th> <td>" + name + "</td></tr>"
    print "<tr> <th> Phone Number </th> <td>" + phone + "</td></tr>"
    print "<tr> <th> Email Address </th> <td>" + email + "</td></tr>"
    print "<tr> <th> Home Address </th> <td>" + home + "</td></tr>"
    print "<tr> <th> Drama </th> <td>" + drama + "</td></tr>"
    print "<tr> <th> Time </th> <td>" + time + "</td></tr>"
    print "<tr> <th> Quantity </th> <td>" + quantity + "</td></tr>"
    print "<tr> <th> Delivery </th> <td>" + delivery + "</td></tr>"
    print "<tr> <th> Payment </th> <td>" + payment + "</td></tr>"
    print "</table>"
    cursor.close()
    dbConn.close()

validate()
if msg == "":
    saveDB()
