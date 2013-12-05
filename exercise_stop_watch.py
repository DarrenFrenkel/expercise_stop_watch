# template for "Stopwatch: The Game"
import simpleguitk as simplegui
# define global variables
enter_time = 0
enter_break = 0
t1 = 0
t2 = 0
num = 0
timer_running = False
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t1):
    minute = 0
    tenths_second = t1 % 10
    second = (t1 - tenths_second) % 100/10 
    subtractor = (t1 - tenths_second) % 100
    ten_second = (t1 -(tenths_second + subtractor))/100
    
    if ten_second > 5:
        minute = ten_second/6
        ten_second = ten_second % 6
     
    return str(int(minute)) + ":" + str(int(ten_second)) + str(int(second)) + "." + str(int(tenths_second))
    pass

def format(t2):
    minute = 0
    tenths_second = t2 % 10
    second = (t2 - tenths_second) % 100/10 
    subtractor = (t2 - tenths_second) % 100
    ten_second = (t2 -(tenths_second + subtractor))/100
    if ten_second > 5:
        minute = ten_second/6
        ten_second = ten_second % 6
    return str(int(minute)) + ":" + str(int(ten_second)) + str(int(second)) + "." + str(int(tenths_second))
    pass

def interval(num):
    string = num
    return str(int(string))

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_running
    timer.start()
    timer_running = True
       
def stop ():
    timer.stop ()
    
def reset ():
    global t1,t2,num
    timer,stop ()
    t1 = 0
    t2 = 0
    num = 0
   

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t1,t2,num,x,y
    if num > 0:
            if t1 != 0:
                t1 -= 1
                if t1 == 0:
                    sound2.play()
            elif t2 != 0:
                t2 -= 1
                if t2 == 0:
                    sound1.play()
            else:
                t1 = x
                t2 = y
                num -= 1
                
                  
def input_handler1(text):
    global enter_time, t1,x
    enter_time = int(text)
    t1 = enter_time * 600
    x = t1

    
def input_handler2(text):
    global enter_break, t2, y
    enter_break = int(text)
    t2 = enter_break * 600
    y = t2
    
    
def input_handler3(text):
    global num
    num = int(text)    

# define draw handler
def draw_handler1(canvas):
    canvas.draw_text(format(t1),[110,180], 60, "White")
    canvas.draw_text(format(t2),[110,330], 60, "Yellow")
    canvas.draw_text(interval(num),[345,60], 40, "Green")
    

    
    
# create frame
frame = simplegui.create_frame('Stop Watch: The Game', 400, 400)

sound1 = simplegui.load_sound('https://www.dropbox.com/s/qwj153wzm7derup/lets_go.ogg?dl=1')
sound2 = simplegui.load_sound('https://www.dropbox.com/s/m921ljc4whji8pc/rest.ogg?dl=1')

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler1)
#frame.set_draw_handler()
frame.add_button("Start", start, 80)
frame.add_button("Stop", stop, 80)
frame.add_button("Reset", reset, 80)
frame.add_input('Excercise',input_handler1,60)
frame.add_input('rest',input_handler2,60)
frame.add_input('intervals',input_handler3,60)

# start frame
frame.start()




# Please remember to review the grading rubric
