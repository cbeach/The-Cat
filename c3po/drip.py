import commands
import curses
import time

class SnotDrip:

    window = None

    def __init__ (self):
        pass

    def initWindow (self, cursesWindow):
        self.window = cursesWindow


    def processFrame(self):
#        window.addstr(0,0, commands.getoutput("snot -lu [-5]")[1])
        self.window.addstr(0,0,"all is well", curses.color_pair(1))
        time.sleep(5)
        
