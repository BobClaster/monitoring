#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os
import re


from engine import Session

wall = Session()

##########################################################################
##                                FORMS                                 ##
##########################################################################

bad_form = False
notific = ''
header = '...'
out = ''

form = cgi.FieldStorage()
#    ADD OPERATOR
lux = form.getfirst("lux", "")
lux = html.escape(lux)

hum = form.getfirst("hum", "")
hum = html.escape(hum)

temp = form.getfirst("temp", "")
temp = html.escape(temp)



if lux != '' and hum != '' and temp != '':
    wall.add_record(lux, hum, temp)
    print('Content-type: text/html\n')
    print(pattern.format(title=header, content="Added", notifications=notific))
