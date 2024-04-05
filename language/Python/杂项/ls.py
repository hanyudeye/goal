import curses, os

def main():
    stdscr = curses.wrapper()
    
    for entry in os.listdir('.'):
        pathname = os.path.join('.', entry)
        statinfo = os.stat(pathname)
        
        size = str(statinfo.st_size).replace("B", "")
        mtime = time.ctime(statinfo.st_mtime)
        
        stdscr.addstr("%s %s %s" % (entry, size, mtime))
    
    if stdscr.keypad(1):
        if ord('q') == curses.KEY_QUIT:
            pass
            
if __name__ == '__main__':
    main()
