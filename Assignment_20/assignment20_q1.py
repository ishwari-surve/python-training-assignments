#Even and Odd thread
import threading

def even_numbers():
    print("Even numbers:")
    for i in range(2, 21, 2):
        print(i)

def odd_numbers():
    print("Odd numbers:")
    for i in range(1, 20, 2):
        print(i)

# Create threads
even_thread = threading.Thread(target=even_numbers, name="Even")
odd_thread = threading.Thread(target=odd_numbers, name="Odd")

# Start threads
even_thread.start()
even_thread.join()   # Ensure Even thread finishes first

odd_thread.start()
odd_thread.join()    # Ensure Odd thread finishes after Even

print("Exit from main")

