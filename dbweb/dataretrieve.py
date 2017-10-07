#!/usr/bin/python

import cgi
import mysql.connector as mdb

print "Content-Type: text/html \n"

data = []

def read_data():

    elements = cgi.FieldStorage()
    global filter

    domain = elements.getvalue('searchfrom') or ""
    filter = elements.getvalue('search') or ""

    if filter == "":
        sql = "select * "
        sql += " from ticket "
        sql += " order by order_id"
    else:
        sql = "select * "
        sql += " from ticket "
        sql += "where " + domain + " like '%" + filter + "%'"
        sql += " order by order_id"

    try:
        dbConn = mdb.connect(host='oit2.scps.nyu.edu', user='shen', password='shen', database='shen')
        cursor = dbConn.cursor()
        cursor.execute(sql)
    except mdb.Error as e:
        print "error in exception"
        errorNum = e.errno
        errorMsg = e.msg
        msg = 'Database Error - ' + str(errorNum) + errorMsg
        print msg
        return
    row = cursor.fetchone()
    while row is not None:
        data.append(row)
        row = cursor.fetchone()
    cursor.close()
    dbConn.close()

def a():
    print "end2"

def display():
    global filter
    print """
        <html>
        <head>
            <title>Order history</title>
            <style>
                h1 {
                    text-align: center;
                    font-size: 60px;
                }
                th {
                    font-weight: bolder;
                    background-color: darksalmon;
                }
                td {
                    text-align: center;
                }
                td {
                    background-color: lightyellow;
                }
                #searchbox {
                    margin-left: 200px;
                    font-size:20px;
                }
            </style>
        </head>
        <body>
            <div align="center"><img src="pitcure/picture.jpg" width="400"></div>
            <h1> Order history </h1>
            <form action=dataretrieve.py method=GET>
            <div id="searchbox">
                <b>Search From:</b>
                <select name=searchfrom size=1>
                    <option value="name">Name</option>
                    <option value="phone_number">Phone Number</option>
                    <option value="email_addr">Email Address</option>
                    <option value="home_addr">Home Address</option>
                    <option value="drama">Available Shows</option>
                    <option value="drama_time">Available Time</option>
                    <option value="quantity">Quantity</option>
                    <option value="delivery_mode">Delivery Mode</option>
                    <option value="payment">Payment</option>
                </select>
                <br>
                <b>Search for:</b>
                <input type=text name=search>
                <input type = submit value = search>
            </div>
            <br>
            </form>
            <div align="center">
                <table border= 1>
                <tr>
                    <th>Order id</th>
                    <th>Name</th>
                    <th>Phone Number</th>
                    <th>Email Address</th>
                    <th>Home Address</th>
                    <th>Drama</th>
                    <th>Time</th>
                    <th>Ticket Quantity</th>
                    <th>Delivery Mode</th>
                    <th>Payment</th>
                </tr>
            </div>
    """
    for row in data:
        print "<tr>",
        order_id = row[0]
        name = row[1]
        phone = row[2]
        email = row[3]
        home = row[4]
        drama = row[5]
        time = row[6]
        quantity = row[7]
        delivery = row[8]
        payment = row[9]
        print "<td>" + str(order_id) + "</td><td>" + name + "</td><td>" + phone + "</td><td>" + email + "</td><td>" + home + "</td><td>" + drama + "</td><td>" + time + "</td><td>" + str(quantity) + "</td><td>" + delivery + "</td><td>" + payment +"</td>",
        print "</tr>"
    print "</table>"
    print "<a href='dbweb.html'> Order Again</a>"
    print "</body>"
    print "</html>"

read_data()
display()
