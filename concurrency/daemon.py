from threading import Thread
import time

def my_func(): 
    while True: 
        time.sleep(1)

def main(): 
    t = Thread(target=my_func)
    t.start()

    

if __name__ == "__main__": 
    main()