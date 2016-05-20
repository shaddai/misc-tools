#!/usr/bin/python

import requests
from optparse import OptionParser

def parse_command_line():
    parser = OptionParser()
    parser.add_option("-s", "--start", dest="start", action="store",
                              help="ID to begin scan with", type="int")
    parser.add_option("-e", "--end", dest="end", action="store",
                              help="Last ID to be scanned", type="int")
    (options, args) =  parser.parse_args()

    if len(args) != 1:
        print ("usage : %prog [options] URL")

    url = ''.join(map(str, args))
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    if not url.endswith('/'):
        url += '/'

    return url, options

def scan(url, conf):
    for id in range(conf.start,conf.end+1):
        query = str(url) + str(id)
        #print "let's get: " + query
        response = requests.get(query, allow_redirects=True, verify=False)
        if response.history:
            print "[+] ID " + str(id) + " redirects to " + response.url


if __name__ == '__main__':
    (url, conf) = parse_command_line()
    scan(url, conf)
