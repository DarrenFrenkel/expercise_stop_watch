#Need to download simpleguitk to run this script
import simpleguitk as simplegui

# define global variables

enter_time = 0
enter_break = 0
training_minutes = 0
resting_seconds = 0
interval_num = 0 
initial_training_minutes = 0
initial_resting_seconds = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def workout_watch(training_minutes):
    '''This helper function converts minutes into
    a stop watch format '''
    minute = 0
    tenths_second = training_minutes % 10
    second = (training_minutes - tenths_second) % 100/10 
    subtractor = (training_minutes - tenths_second) % 100
    ten_second = (training_minutes -(tenths_second + subtractor))/100
    
    if ten_second > 5:
        minute = ten_second/6
        ten_second = ten_second % 6
     
    return str(int(minute)) + ":" + str(int(ten_second)) + str(int(second)) + "." + str(int(tenths_second))

def resting_watch(resting_seconds):
    '''This helper function converts seconds into
    a stop watch format '''
    minute = 0
    tenths_second = resting_seconds % 10
    second = (resting_seconds - tenths_second) % 100/10 
    subtractor = (resting_seconds - tenths_second) % 100
    ten_second = (resting_seconds -(tenths_second + subtractor))/100
    
    if ten_second > 5:
        minute = ten_second/6
        ten_second = ten_second % 6
        
    return str(int(minute)) + ":" + str(int(ten_second)) + str(int(second)) + "." + str(int(tenths_second))

def interval(interval_num):
    '''This helper function converts your interval in int into a string 
    so it could be read by our event handler '''
    string = interval_num
    return str(int(string))

# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    '''This event handler starts the stop watches'''
    global timer_running
    timer.start()
       
def stop ():
    '''This event handler stops the stop watches'''    
    timer.stop ()
    
def reset ():
    '''This event handler resets the stop watches''' 
    global training_minutes,resting_seconds,interval_num
    timer.stop()
    training_minutes = 0
    resting_seconds = 0
    interval_num = 0
   
# define event handler for timer with 0.1 sec interval

def timer_handler():
    '''This time handler play alarms, reduces intervals and restarts the clock'''
    global training_minutes, resting_seconds, interval_num, initial_training_minutes, initial_resting_seconds
    if interval_num > 0:
            if training_minutes != 0:
                training_minutes -= 1
                if training_minutes == 0:
                    rest.play()
            elif resting_seconds != 0:
                resting_seconds -= 1
                if resting_seconds == 0:
                    go.play()
            else:
                training_minutes = initial_training_minutes
                resting_seconds = initial_resting_seconds
                interval_num -= 1
                                  
def train_input_handler(text):
    '''Adds training time in minutes'''
    global enter_time, training_minutes, initial_training_minutes
    enter_time = int(text)
    training_minutes = enter_time * 600
    initial_training_minutes = training_minutes
    
def rest_input_handler(text):
    '''Adds resting time in seconds'''    
    global enter_break, resting_seconds, initial_resting_seconds
    enter_break = int(text)
    resting_seconds = enter_break * 10 
    initial_resting_seconds = resting_seconds 
        
def intervals_input_handler(text):
    '''Adds intervals'''  
    global interval_num
    interval_num = int(text)    

# define draw handler

def draw_handler(canvas):
    '''This draw handlers draw the training stop watch, the resting 
    stop watch and the interval number'''
    canvas.draw_text(workout_watch(training_minutes),[110,180], 60, "White")
    canvas.draw_text(resting_watch(resting_seconds),[110,330], 60, "Yellow")
    canvas.draw_text(interval(interval_num),[345,60], 40, "Green")
       
# create frame

frame = simplegui.create_frame('Stop Watch: The Game', 400, 400)

# create sound variables

go = simplegui.load_sound('https://www.dropbox.com/s/qwj153wzm7derup/lets_go.ogg?dl=1')
rest = simplegui.load_sound('https://www.dropbox.com/s/m921ljc4whji8pc/rest.ogg?dl=1')

# register event handlers

timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

#frame.set_draw_handler()

frame.add_button("Start", start, 80)
frame.add_button("Stop", stop, 80)
frame.add_button("Reset", reset, 80)
frame.add_input('Excercise, Enter Minutes',train_input_handler,140)
frame.add_input('Rest, Enter Seconds',rest_input_handler,140)
frame.add_input('intervals',intervals_input_handler,140)

# start frame

frame.start()

