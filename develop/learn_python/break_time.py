import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(2 * 60 * 30)

    webbrowser.open("https://www.youtube.com/watch?v=vqIzXrXo-6c")
    break_count = break_count + 1
