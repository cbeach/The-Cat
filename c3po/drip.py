import commands
import curses
import time
import re

class SnotDrip:

    window = None

    def __init__ (self):
        pass

    def initWindow (self, cursesWindow):
        self.window = cursesWindow


    def processFrame(self):
        ticketNumbers = self.lastNTickets(10)
        ticketNumbers.sort(reverse=True)
           
        self.subjects = self.getTicketSubjects(ticketNumbers)

        self.tickets = {}

        for i in range(len(ticketNumbers)):
            self.tickets[ticketNumbers[i]] = self.subjects[i]

        for i in self.tickets:
            print i, self.tickets[i]


    def postToWindow(self):
        height, width = self.window.getmaxyx() 

    def lastNTickets(self, numberOfTickets):

        #get the latest 5 tickets in the queue
        rawSnot = commands.getoutput("snot -lu [-%d]" % (numberOfTickets))

        #parse parse the tickets using spaces as delimeters
        parsedSnot = rawSnot.split(' ')
        ticketNumbers = []
        
        #find all of the strings that are numbers
        for i in parsedSnot:
            try:
                ticketNumbers.append(int(i))
            except ValueError:
                pass 

        del rawSnot
        del parsedSnot
        return ticketNumbers
    
    def getTicketSubjects(self, ticketNumbers):
        tickets = []  
        for i in ticketNumbers:
              tickets.append(commands.getoutput("snot -s %d" % (i)))
        
        parsedTickets = []

        for i in tickets:
            parsedTickets.extend(i.split('\n'))

        subjects = []
     
        for i in parsedTickets:
            if(i.find("Subject: ") != -1):
                if(i.find("Re: ") == -1):
                    subjects.append(i)

        return subjects

    def stopCurses(self):
        curses.nocbreak()
        curses.echo()
        self.stdscr.keypad(0)
        curses.endwin()

def main():
    SnotDrip().processFrame()



if __name__ == "__main__":
    main()
