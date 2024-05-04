import pyttsx3
from win10toast import ToastNotifier
import time

toster=ToastNotifier()
abhi=pyttsx3.init()

abhi.say('checkout ur computer man. There are some alert')
abhi.runAndWait()

toster.show_toast('Alert','Checkout ur computer', threaded=True, icon_path=None, duration=3)

while toster.notification_active():
    time.sleep(0.1)

