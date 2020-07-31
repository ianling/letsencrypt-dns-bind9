# letsencrypt-dns-bind9
A python3 script that handles Let's Encrypt's dns-01 challenge hooks for a BIND9 server.

See the `python2` branch for the legacy python2.x version.

# Overview
This script uses nsupdate to add a TXT record to all specified nameservers in order to complete the dns-01 challenge for generating a Let's Encrypt certificate.

I personally use dehydrated (link below) to run the script; I don't know if it works with any other letsencrypt clients.

You have to change several variables at the top of the script, as these things will vary depending on your environment:
  - which nameserver(s) to use
  - name of your zone
  - DNSSEC key path
  - nsupdate binary path
  
If the script is not working, make sure all the variables at the top of the script are correct for your environment.
Additionally, verify that you have configured nsupdate properly to be able to make changes to your nameserver before
attempting to use this script.

# Requirements
 * Python 3.6 (or above)
 * nsupdate (test it on the command line first to verify that you're able to make changes to your BIND9 server remotely)
 * dehydrated (https://github.com/lukas2511/dehydrated)

# Demo
    $ ./dehydrated --cron --domain blog.iancaling.com --hook ./bind.py --challenge dns-01
    Processing blog.iancaling.com
     + Signing domains...
     + Creating new directory /home/ianl/dehydrated/certs/blog.iancaling.com ...
     + Generating private key...
     + Generating signing request...
     + Requesting challenge for blog.iancaling.com...
     + Deploying challenge record to dns1.iancaling.com...
     + Challenge deployed!
     + Responding to challenge for blog.iancaling.com...
     + Cleaning up challenge record on dns1.iancaling.com...
     + Cleanup complete!
     + Challenge is valid!
     + Requesting certificate...
     + Checking certificate...
     + Done!
     + Creating fullchain.pem...
     + Done!

# TODO
  - Use a Python library instead of nsupdate (this will eliminate the subprocess and nsupdate binary requirements)
  - Exit more gracefully if some of the DNS records were deployed successfully. i.e. remove the records that got deployed, and THEN crash
