#!/usr/bin/env python3

#Paul Croft
#September 10, 2020

from bottle import get, run, static_file, template

import string


@get("/static/<sfile>")
def staticassets(sfile):
    return static_file(sfile, root="static")

@get("/")
@get("/index")
def indexpage():
    return template("templates/index.html")

def main():
    run(host="0.0.0.0", port=13244, server="eventlet")

    return 0


if __name__ == '__main__':
    exit(main())
