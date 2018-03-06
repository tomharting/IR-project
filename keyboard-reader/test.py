import termios, sys, time
def getch(inp=sys.stdin):
    old = termios.tcgetattr(inp)
    new = old[:]
    new[-1] = old[-1][:]
    new[3] &= ~(termios.ECHO | termios.ICANON)
    new[-1][termios.VMIN] = 1
    try:
        termios.tcsetattr(inp, termios.TCSANOW, new)
        return inp.read(1)
    finally:
        termios.tcsetattr(inp, termios.TCSANOW, old)


inputstr = ''
while '\n' not in inputstr:
    c = getch()
    if not inputstr: t = time.time()
    inputstr += c
elapsed = time.time() - t