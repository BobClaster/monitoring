#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os
import re
import urllib.request as urllib2

from engine import DataBase

wall = DataBase()

notific = ''
header = '...'
out = ''

form = cgi.FieldStorage()


articles = wall.get_last_records()




##########################################################################
##                              PRINTING                                ##
##########################################################################

file = open('html/pattern.html', 'r')
pattern = file.read()

header = 'All operators'
out ="""<h1 style="text-align: center;">Моніторинг</h1>
        <!--<form action="/cgi-bin/main.py" style="display: inline; ">
            <input name="search" type="text" placeholder="Пошук">
            <button type="submit">Пошук</button>
        </form>-->
        <hr>

        <table>

        <tr>
            <td align='center'><h2>Напруга (V)</h2></td>
            <td align='center'><h2>Струм (А)</h2></td>
            <td align='center'><h2>Потужність (W)</h2></td>
            <td align='center'><h2>Енергія (Wh)</h2></td>
            <td align='center'><h2>Дата та час</h2></td>
        </tr>
        """
for article in articles:
    out += '<tr>'
    out += "<td align='center'><h3>" + str(article[0]) + "</h3></td>"
    out += "<td align='center'><h3>" + str(article[1]) + "</h3></td>"
    out += "<td align='center'><h3>" + str(article[2]) + "</h3></td>"
    out += "<td align='center'><h3>" + str(article[3]) + "</h3></td>"
    out += "<td align='center'><h3>" + str(article[4])[:19] + "</h3></td>"
    out += '</tr>'

#           OUT
print('Content-type: text/html\n')
print(pattern.format(title=header, content=out, notifications=notific))
