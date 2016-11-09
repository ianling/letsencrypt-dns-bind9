#!/usr/bin/python
import sys
import os
from subprocess import call

# VARIABLES
nameservers = ['dns1.iancaling.com']
zone_name = 'iancaling.com.'
nsupdate_keyfile = '/home/ianl/iancaling.com.key'
nsupdate_path = '/usr/bin/nsupdate'


# possible commands:
#  1 - deploy_challenge -- deploy the challenge records
#  2 - clean_challenge -- clean up the challenge records
#  3 - deploy_cert -- do nothing! you have to do this manually!
command = sys.argv[1]
domain = sys.argv[2]
token = sys.argv[4]

if command == 'deploy_challenge':
    for nameserver in nameservers:
        print ' + Deploying challenge record to '+nameserver+'...'
        batch_file_path = '/tmp/'+nameserver+'_nsupdate.tmp'
        nsupdate_batch_file = open(batch_file_path, 'w+')
        nsupdate_batch_file.write('''server ''' + nameserver + '''
zone ''' + zone_name + '''
update add _acme-challenge.''' + domain + ''' 60 TXT ''' + token + ''' 
send
''')
        nsupdate_batch_file.close()
        nsupdate_command = nsupdate_path + ' -k ' + nsupdate_keyfile + ' ' + batch_file_path
        call(nsupdate_command, shell=True)
        os.remove(batch_file_path)
    print ' + Challenge deployed!'

elif command == 'clean_challenge':
    for nameserver in nameservers:
        print ' + Cleaning up challenge record on '+nameserver+'...'
        batch_file_path = '/tmp/'+nameserver+'_nsupdate.clean.tmp'
        nsupdate_batch_file = open(batch_file_path, 'w+')
        nsupdate_batch_file.write('''server ''' + nameserver + '''
zone ''' + zone_name + '''
update delete _acme-challenge.''' + domain + ''' TXT
send
''')
        nsupdate_batch_file.close()
        nsupdate_command = nsupdate_path + ' -k ' + nsupdate_keyfile + ' ' + batch_file_path
        call(nsupdate_command, shell=True)
        os.remove(batch_file_path)
    print ' + Cleanup complete!'

elif command == 'deploy_cert':
    pass # deploy your cert manually
