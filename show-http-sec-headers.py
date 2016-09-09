import urllib2
import sys

def inspect_headers (my_header, headers):
    if my_header in headers:
        print "[+] "+ my_header + ": " + headers[my_header]
    else:
        print "[-] "+  header + " missing"


url = sys.argv[1]

req = urllib2.Request(url)
res = urllib2.urlopen(req)

url_headers = res.info()

print "URL: " + url + "\n"

headers_list = [ "Strict-Transport-Security", "X-Frame-Options",
        "X-XSS-Protection", "X-Content-Type-Options", "Content-Security-Policy"
        ]
for header in headers_list:
    inspect_headers(header, url_headers)

res.close()


