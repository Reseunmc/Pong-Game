__author__ = 'Re'
from cs1lib import *

#constant definitions
WINDOW_HEIGHT=400
WINDOW_WIDTH=400
PADDLE_MOVEMENT=10
R=10
PADDLE_HEIGHT=80
PADDLE_WIDTH=20
RPADDLE_HEIGHT=380
SLEEP_TIME=.02
CHANGE_DIRECTION=-1
X_VELOCITY=-3
Y_VELOCITY=-3

#function to draw the ball
def draw_ball():
    set_fill_color(0,1,1)
    draw_circle(ball_x,ball_y,R)

#function to draw the bluepaddles
def draw_paddles():
    set_fill_color(0,0,1)
    draw_rectangle(right_paddle_x,right_paddle_y,PADDLE_WIDTH,PADDLE_HEIGHT)
    draw_rectangle(left_paddle_x,left_paddle_y,PADDLE_WIDTH,PADDLE_HEIGHT)

#funtion to make the image visible
def redraw_sleep():
    request_redraw()
    sleep(SLEEP_TIME)

#function to produce pong game
def pong_game():
#variables for the right_paddle_x and right_paddle_y locations of the corners of the rectangles
# and the height and width constants
    X_VELOCITY=-3
    Y_VELOCITY=-3
    ball_x=200
    ball_y=200
    left_paddle_x=0
    left_paddle_y=0
    right_paddle_x=380
    right_paddle_y=320

#variables made global to be referenced in previous functions
    global right_paddle_x,right_paddle_y,left_paddle_y,left_paddle_x,ball_x,ball_y

#makes the background black
    set_clear_color(0,0,0)

#removes borders and smoothens
    disable_stroke()
    clear()
    enable_smoothing()

#while the window is open draw these rectangles
    while not window_closed():
        draw_paddles()
        draw_ball()
        ball_x=ball_x+X_VELOCITY
        ball_y=ball_y+Y_VELOCITY

#bounces the balls of of the left paddle
        if ball_y>=left_paddle_y and ball_y<=left_paddle_y+PADDLE_HEIGHT and ball_x==PADDLE_WIDTH:
            X_VELOCITY=X_VELOCITY*CHANGE_DIRECTION

#bounces the balls of the right paddle
        if ball_y>=right_paddle_y and ball_y<=right_paddle_y+PADDLE_HEIGHT and ball_x==right_paddle_x:
            X_VELOCITY=X_VELOCITY*CHANGE_DIRECTION

#to bounce the ball off of the horizontal top and bottom walls
        if ball_y==5 or ball_y==WINDOW_HEIGHT-5:
            Y_VELOCITY=Y_VELOCITY*CHANGE_DIRECTION

#Changes the color when the ball hits the paddles
        if X_VELOCITY==-3:
            clear()
            draw_paddles()
            draw_ball()

#Changes the color when the ball hits the paddles
        if X_VELOCITY==3:
            clear()
            draw_paddles()
            set_fill_color(1,0,1)
            draw_circle(ball_x,ball_y,R)
            set_fill_color(0,0,1)

#If the q key is pressed the cs1 quit function is called to close the window and quit the game
        if is_key_pressed("q"):
            cs1_quit()

#states that if the ball leaves the window from the left or right side, the game ends
        if ball_x+R<=0 or ball_x-R>=WINDOW_WIDTH:
            enable_stroke()
            set_stroke_width(20)
            set_stroke_color(1,1,1)
            draw_text("GAME OVER. PRESS SPACEBAR.",50,200)
            request_redraw()
            disable_stroke()

#restarts the game by recalling the start graphics
        if is_key_pressed(" ") and ball_x>=WINDOW_WIDTH:
            start_graphics(pong_game,"Pong Lab",WINDOW_WIDTH,WINDOW_HEIGHT)

        elif is_key_pressed(" ") and ball_x<=0:
             start_graphics(pong_game,"Pong Lab",WINDOW_WIDTH,WINDOW_HEIGHT)

#if left_paddle_x is pressed or held down, the left rectangle(paddle) moves up by 10 pixels per iteration(10PPI)
        if is_key_pressed("a") and left_paddle_y>=0:
            left_paddle_y=left_paddle_y-PADDLE_MOVEMENT

#if z is pressed/held down, the left paddle moves down 10PPI
        if is_key_pressed("z") and left_paddle_y<=WINDOW_HEIGHT-80:
            left_paddle_y=left_paddle_y+PADDLE_MOVEMENT

#if k is pressed/held down, the right paddle moves up 10PPI
        if is_key_pressed("k") and right_paddle_y>=0:
            right_paddle_y=right_paddle_y-PADDLE_MOVEMENT

#if the m key is pressed/held down, the right paddle moves down 10PPI
        if is_key_pressed("m") and right_paddle_y<=WINDOW_HEIGHT-80:
            right_paddle_y=right_paddle_y+PADDLE_MOVEMENT

#redraws the image so that it will be repeatedly visual
        redraw_sleep()
        clear()

#allows for the previous paddle image iteration to be removed and a new one to be quickly redrawn
#at the next location to simulate a moving object
start_graphics(pong_game,"Pong Lab",WINDOW_WIDTH,WINDOW_HEIGHT)