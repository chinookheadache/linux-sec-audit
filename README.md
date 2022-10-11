# linux-sec-audit
zac fawcett

Linux Based Security audit script, outputs a security audit of the system it is run on, into a file

This script will take an audit of the system it is run on and output the following info into a file:

-Machine Name

-List of all users and the group they are associated with

-From /proc/cpuinfo get the following:

    processor
    
    vendor_id
    
    model
    
    model name
    
    cache
    
-All services on machine and their current status

The output file name and path can be changed in the python code
