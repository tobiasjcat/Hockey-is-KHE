#!/usr/bin/env python3

#Paul Croft
#September 10, 2020

from bottle import get, response, run, static_file, template

import string

doublelower = string.ascii_lowercase * 2
doubleupper = string.ascii_uppercase * 2

@get("/static/<sfile>")
def staticassets(sfile):
    return static_file(sfile, root="static")

@get("/ttfs/<ttfsfile>")
def ttfassets(ttfsfile):
    return static_file(ttfsfile, root="ttfs")


@get("/rotfonts.css")
def rotfonts_file():
    response.content_type = 'text/css'
    return template("templates/rotfonts.css")

@get("/")
@get("/index")
def indexpage():
    rotdict = {i:{} for i in range(26)}
    for i in range(26):
        for l,u in zip(string.ascii_lowercase, string.ascii_uppercase):
            rotdict[i][l] = doublelower[doublelower.find(l) + i]
            rotdict[i][u] = doublelower[doublelower.find(u) + i]
    return template("templates/index.html", rotdict=rotdict)

def main():
    run(host="0.0.0.0", port=13244, server="eventlet")

    return 0


if __name__ == '__main__':
    exit(main())
