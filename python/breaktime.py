import webbrowser
import time

breaks_needed = 3
break_count = 0

print("This program started on " +time.ctime())
while (break_count < breaks_needed):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=TF6cnLnEARo&list=FLu6epfqtMTz99jfrE9pL7ng&index=12")
    break_count = break_count + 1
    print ("Take a break!")
    
