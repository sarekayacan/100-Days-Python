#Countdown Timer
import time
start = int(input("Enter the number to start the countdown from: "))
speed = float(input("Enter the countdown speed: "))

print("\n--- Countdown begins ---")
original_start = start  
while start > 0 :
    print(start)
    if start == (original_start / 2):
        print("Halfway there")
    time.sleep(speed)
    start -= 1
        
print("Countdown complete!")