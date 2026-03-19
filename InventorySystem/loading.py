import time
import sys

def loading_screen():

    print("\nStarting Inventory System...\n")

    for i in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.05)

    print("\nSystem Loaded Successfully!\n")
    time.sleep(1)
