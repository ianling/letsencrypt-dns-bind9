#!/usr/bin/env python3
from sys import argv
from os import remove
from subprocess import call


# CONFIGURATION START
nameservers = ["dns1.iancaling.com"]
zone_name = "iancaling.com."
nsupdate_keyfile = "/home/ianl/iancaling.com.key"
nsupdate_path = "/usr/bin/nsupdate"
# CONFIGURATION END


"""
possible commands:
  1 - deploy_challenge -- deploy the challenge records
  2 - clean_challenge -- clean up the challenge records
  3 - deploy_cert -- do nothing! you have to do this manually!
"""
command = argv[1]
domain = argv[2]
token = argv[4]

if command == "deploy_challenge":
    for nameserver in nameservers:
        print(f" + Deploying challenge record to {nameserver}...")
        batch_file_path = f"/tmp/{nameserver}_{domain}_nsupdate.tmp"
        with open(batch_file_path, "w") as nsupdate_batch_file:
            nsupdate_batch_file.write(f"""server {nameserver}
zone {zone_name}
update add _acme-challenge.{domain} 60 TXT {token}
send
""")
        nsupdate_command = f"{nsupdate_path} -k {nsupdate_keyfile} {batch_file_path}"
        call(nsupdate_command, shell=True)
        remove(batch_file_path)
    print(" + Challenge deployed!")

elif command == "clean_challenge":
    for nameserver in nameservers:
        print(f" + Cleaning up challenge record on {nameserver}...")
        batch_file_path = f"/tmp/{nameserver}_{domain}_nsupdate.clean.tmp"
        with open(batch_file_path, "w") as nsupdate_batch_file:
            nsupdate_batch_file.write(f"""server {nameserver}
zone {zone_name}
update delete _acme-challenge.{domain} TXT
send
""")
        nsupdate_command = f"{nsupdate_path} -k {nsupdate_keyfile} {batch_file_path}"
        call(nsupdate_command, shell=True)
        remove(batch_file_path)
    print(" + Cleanup complete!")

elif command == "deploy_cert":
    pass  # deploy your cert manually

