import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r') # Print timer with carriage return to overwrite the previous output
        time.sleep(1)
        seconds -= 1

    print('Time\'s up!')

# Input the desired countdown time in seconds
countdown_time = int(input("Enter countdown time in seconds: "))

countdown_timer(countdown_time)
