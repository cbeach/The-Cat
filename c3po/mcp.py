import curses
import colors
import time
import drip
class Mcp:
    
    stdscr = None
    windowRef = None
    windowDelegates = None
    
    def __init__(self):
        self.initCurses()
        
        height, width = self.stdscr.getmaxyx()
        
        self.windowRef = {"drip":curses.newwin(4, width, height-4, 0)}
        self.windowDelegates = {"drip":drip.SnotDrip()}
       
        self.windowDelegates["drip"].initWindow(self.windowRef["drip"])

        self.windowDelegates["drip"].processFrame()
        self.windowRef["drip"].refresh()
        time.sleep(5)

    def initCurses(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        colors.init_colors()



    def __del__(self):
        curses.nocbreak()
        curses.echo()
        self.stdscr.keypad(0)
        curses.endwin()
        
