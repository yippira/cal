
import csv

eventDct = {}
userDct = {}
calFileName = "cal.csv"
passwordFileName = "passwords.csv"


"""
Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
"""
def readCsv(csvfilename):
    rows = []
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

def addUser(username, password):
    userDct[username] = password
    writeToPasswordCsv()

def getPassword(username, password, passwordFile):
    

    passwords = readCsv(passwordFile)

    for i in passwords:
        if (i[0] == username):
            if (i[1] == password):
                return 1
            else:
                return 0

    if username not in passwords:
        return 2

    return 0


def makeEvent(username, event):

    if username in eventDct:
        eventDct[username].append(event)

    else:
        eventDct[username] = [event]

    writeToEventCsv()

def getEvent(username):
    eventDct = dict(readCsv(calFileName))

    if username in eventDct:
        return eventDct[username]

    return 0

def writeToEventCsv():

    with open(calFileName, "w", newline='') as csvfile:

        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', \
                                quoting=csv.QUOTE_MINIMAL)
        
        filewriter.writerow(["username", "events"])

        for usr in eventDct:
            
            entry = [usr, str(eventDct[usr])]

            filewriter.writerow(entry)

def writeToPasswordCsv():
    
    with open(passwordFileName, "w", newline='') as csvfile:

        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', \
                                quoting=csv.QUOTE_MINIMAL)
        
        filewriter.writerow(["username", "password"])

        for usr in userDct:
            
            entry = [usr, str(userDct[usr])]

            filewriter.writerow(entry)

def main():


    while (1):
        
        username = input("Username: ")
        password = input("Password: ")
        
        if (getPassword(username, password, passwordFileName) == 1):
            print(getEvent(username))

        elif (not getPassword(username, password, passwordFileName)):
            print("Invalid password! Exiting now.")
            break

        else:
            print("User not in database. Added user.")
            #addUser(username, password)
            #todo - add user

        x = input("Add event to user? Enter 1 if yes.\n")

        if (x == str(1)):
            event = input("Please input event: ")
            makeEvent(username, event)

        x = input("Input 1 if you wish to continue, and press enter. \n")

        if (x != str(1)):
            break


if __name__ == "__main__":
    main() 
        
    
