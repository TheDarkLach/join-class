import webbrowser
import schedule
import time

#Zoom link for each period, example: "https://us05web.zoom.us/j/83426406403?pwd=V0FwTjVhbEhrVmRBbXVpa0UyUmhhdz09"
P1 = " "
P2 = " "
P3 = " "
P4 = " "

#Time each period starts, examples "8:30", "21:30"
T1 = " "
T2 = " "
T3 = " "
T4 = " "

schedule.every().day.at(T1).do(webbrowser.open_new_tab(P1))
schedule.every().day.at(T2).do(webbrowser.open_new_tab(P2))
schedule.every().day.at(T3).do(webbrowser.open_new_tab(P3))
schedule.every().day.at(T4).do(webbrowser.open_new_tab(P4))

while True:
    schedule.run_pending()
    time.sleep(1)
