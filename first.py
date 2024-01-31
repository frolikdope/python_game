import curses
import time

def main(stdscr):
    
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100) 

    ball = [sh//2, sw//2]
    ball_speed = [1, 1]

    paddle_left = [sh//2 - 2, 5]
    paddle_right = [sh//2 - 2, sw - 5]

    while True:
        key = w.getch()
        if key == ord('q'):
            break

        ball[0] += ball_speed[0]
        ball[1] += ball_speed[1]

        if ball[0] == 0 or ball[0] == sh - 1:
            ball_speed[0] *= -1
        if ball[1] == 0 or ball[1] == sw - 1:
            ball_speed[1] *= -1

        if (
            paddle_left[0] <= ball[0] <= paddle_left[0] + 4 and
            paddle_left[1] <= ball[1] <= paddle_left[1] + 1
        ) or (
            paddle_right[0] <= ball[0] <= paddle_right[0] + 4 and
            paddle_right[1] - 1 <= ball[1] <= paddle_right[1]
        ):
            ball_speed[1] *= -1
       
        if key == curses.KEY_UP and paddle_right[0] > 0:
            paddle_right[0] -= 1
        elif key == curses.KEY_DOWN and paddle_right[0] < sh - 5:
            paddle_right[0] += 1

        if key == ord('w') and paddle_left[0] > 0:
            paddle_left[0] -= 1
        elif key == ord('s') and paddle_left[0] < sh - 5:
            paddle_left[0] += 1
    
        w.clear()
        w.addch(ball[0], ball[1], 'o')
        w.addch(paddle_left[0], paddle_left[1], '|')
        w.addch(paddle_left[0] + 1, paddle_left[1], '|')
        w.addch(paddle_left[0] + 2, paddle_left[1], '|')
        w.addch(paddle_left[0] + 3, paddle_left[1], '|')
        w.addch(paddle_right[0], paddle_right[1], '|')
        w.addch(paddle_right[0] + 1, paddle_right[1], '|')
        w.addch(paddle_right[0] + 2, paddle_right[1], '|')
        w.addch(paddle_right[0] + 3, paddle_right[1], '|')

        w.refresh()
        time.sleep(0.1)

curses.wrapper(main)
