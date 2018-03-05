#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os
import re


from engine import DataBase

wall = DataBase()

##########################################################################
##                                FORMS                                 ##
##########################################################################

bad_form = False
notific = ''
header = '...'
out = ''

form = cgi.FieldStorage()
#    ADD OPERATOR
volt = form.getfirst("v", "")
volt = html.escape(volt)

amper = form.getfirst("a", "")
amper = html.escape(amper)

watt = form.getfirst("w", "")
watt = html.escape(watt)

watt_hour = form.getfirst("wh", "")
watt_hour = html.escape(watt_hour)



if volt != '' and amper != '' and watt != '' and watt_hour != '':
    wall.add_record(volt, amper, watt, watt_hour)
    print('Content-type: text/html\n')
    # print("")
