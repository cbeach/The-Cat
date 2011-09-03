import curses
import time

if __name__=="__main__":


    scr = curses.initscr()
    curses.cbreak()
    curses.echo()
    curses.start_color()

    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)

    scr.keypad(1)
    try:
        height,width = scr.getmaxyx()
        num = min(height,width)
        for x in range(num):
            scr.addch(x,x,'X', curses.color_pair(1))

        # Print Hello World along the top
        scr.addstr(0,10,"Hello World")

        #Draw some lines
        for x in range(8):
            scr.addch(4,x,curses.ACS_HLINE)
        scr.addch(4,8,curses.ACS_PLUS)
        scr.addch(4,9,curses.ACS_LRCORNER)

        scr.refresh()
        time.sleep(3)
    finally:	
        curses.nocbreak()
        scr.keypad(0)
        curses.echo()
        curses.endwin()

