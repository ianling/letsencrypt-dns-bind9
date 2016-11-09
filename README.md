# letsencrypt-dns-bind9
A python script that handles Let's Encrypt's dns-01 challenge hooks for a BIND9 server.

# Overview
This script uses nsupdate and rndc to add a record to all servers found in a zone's NS records, in order to complete the dns-01 challenge for generating a Let's Encrypt cert.

I personally use dehydrated (link below) to run the script; I don't know if it works with any other letsencrypt clients.

If it's not working for you, you may need to change the paths in the script to your nsupdate and rndc binaries. I run this script on Debian 8 (jessie), so the paths may change depending on your distro. You may also need to run dehydrated as root in order for this script to access nsupdate and rndc.

# Requirements
Python 2
  - tldextract
  - subprocess

nsupdate (make sure it's working so that you're able to make changes to your BIND9 server remotely)

rndc (same deal)

dehydrated (https://github.com/lukas2511/dehydrated)

# Demo
$ ./dehydrated --cron --domain blog.iancaling.com --hook ./bind.py --challenge dns-01
   
    Processing blog.iancaling.com
     + Signing domains...
     + Generating private key...
     + Generating signing request...
     + Requesting challenge for blog.iancaling.com...
    Deploying challenge record to DNS servers...
    Reloading zone...
    zone reload queued
    The zone reload and thaw was successful.
    Challenge deployed!
     + Responding to challenge for blog.iancaling.com...
    Cleaning up challenge record...
    Reloading zone...
    zone reload queued
    The zone reload and thaw was successful.
    Cleanup complete!
     + Challenge is valid!
     + Requesting certificate...
     + Checking certificate...
     + Done!
     + Creating fullchain.pem...
     + Done!
     
$ ls certs/
    blog.iancaling.com
    
