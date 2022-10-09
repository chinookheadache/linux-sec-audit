"""
Project 1
September 30th 2021
by Zac Fawcett

v1 September 30 2021
-Programmed input files to be read by loops or package function
-Split lists into lines for ease of access using .splitlines()
-Write needed strings to output file

v2 October 1 2021
-added formatting for output

v3 October 3 2021
-changed output formatting to concatination to reduce lines
-Added very basic error handling where if file fails to be written to or read
 then user will get a prompt about which file or process has a problem
-added a constant string variable with filename confirmation at end of code
-added user defined functions for repeating code simplification
"""
"""
Pseudo Code

Import needed packages
use get packages to read required data into lists

outputfile = open (filename) write

password info list = passwd get function

group info list = grp get function

cpu info list = open(cpuinfofile) read

split cpu data = cpu info list.splitlines function

outputfile.write(socketfunction.needed variable)

outputfile.write(cpu info file [needed items]

for (loop) data in password info list:
            dataname = account.needed info
            outputfile.write(account.needed info)
            
serviceslist = osfunction.terminal services call
for (loop) services in serviceslist
            outputfile.write(services)

outputfile.close()
"""

# import needed packages
import pwd
import socket
import os
import grp

# Constant string used for easy changing of file output name and also to signal to
# user what the file name is at end of code
OUTPUTNAME = "Audit Output.txt"

# User defined functions for writing the error message based on specific failure
# function takes a string as argument which is the file associated with attempted execution
# and writes an error message to output based on that argument

def CantRead(string):
    auditFile.write("Can't Read " + string + " File!")

def WriteFail(string):
    auditFile.write("Failed to write " + string)
    

# Read pass.wd and group file into lists using getpwall and getgrall packages
# Add error handling to signal to user that either operation did not work
try:
    accountInfo = pwd.getpwall()
except:
    CantRead("pass.wd")

try:
    grpInfo = grp.getgrall()
except:
    CantRead("Group")

# Create a file for writing output to (will appear in same directory as this .py file
# Add error handling to signal to user that file would not open
try:
    auditFile = open(OUTPUTNAME, "w")
except:
    auditFile.write("Failed to create output file")
    

# Adding formatted splash screen for output file
auditFile.write("SECURITY AUDIT RESULTS" + "\n"
                + "**************************" + "\n"
                + "AUTHORIZED PERSONEL ONLY!!" + "\n"
                + "**************************" + "\n" + "\n" + "\n")


# Open, read in and split by line, the CPU Info file to retrieve needed data
# Add error handling to signal to user that file could not be read, and then close file
try:
    cpuInfoFile = open("/proc/cpuinfo", "r")
    cpuData = cpuInfoFile.read().splitlines()
except:
    CantRead("CPU Info")
finally:
    cpuInfoFile.close()


# Get Machine Name using socket package, write machine name to output file
# Add error handling to signal to user that operation did not work
try:
    machineName = socket.gethostname()
except:
    auditFile.write("Failed to get machine name")

auditFile.write("MACHINE NAME: " + machineName + "\n" + "\n" + "\n" )

                
# Add title for CPU info section, Get CPU info, write to output
auditFile.write("CPU INFORMATION" + "\n"
                + "-----------------------------------" + "\n" + cpuData[0]
                + "\n" + cpuData[1] + "\n" + cpuData[3] + "\n" + cpuData[4]
                + "\n" + cpuData[8] + "\n" + "\n" + "\n")


# Add title for groups section
auditFile.write("LIST OF USERS AND ASSOCIATED GROUPS" + "\n"
                + "-----------------------------------" + "\n")

# print group records with formatted output showing usernames and each group
# user belongs to
auditFile.write("USER".ljust(25) + "GROUPS".rjust(25) + "\n")


# loop through the accountInfo list finding and printing each instance of username and corresponding group
# Add error handling to signal to user that operation did not work
try:
    for account in accountInfo:
        accountName = account.pw_name

        # get default group name
        groupID = account.pw_gid
        groupRecord = grp.getgrgid(groupID)
        auditFile.write(accountName.ljust(25) + groupRecord.gr_name.rjust(25) + "\n")
    

        # get other group membership
        for group in grpInfo:
            if accountName in group.gr_mem:
                auditFile.write("-------------------------".rjust(20)
                                + group.gr_name.rjust(25) + "\n")
               
except:
        WriteFail("Users and Groups")
    
auditFile.write("\n" + "\n")

# Formatting to signal beginning of services list
auditFile.write("SERVICES ON MACHINE / SERVICES STATUS" + "\n"
                + "-----------------------------------" + "\n")

# Get services list and write to output
# Add error handling to signal to user that operation did not work
servicesList = os.popen("systemctl list-unit-files --type service --all").read().splitlines()

try:
    for services in servicesList:
            auditFile.write(services + "\n")
        
except:
    WriteFail("Services List")

# End of output signalling for user
auditFile.write("\n" + "\n" + "**************************" + "\n" + "END OF AUDIT FILE"
                + "\n" + "**************************")

# Signal to user that file is done writing
print("\n" + "Finished writing " + OUTPUTNAME)

# Close file for proper writing                        
auditFile.close()












