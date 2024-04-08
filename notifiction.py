from win10toast import ToastNotifier
toster=ToastNotifier()

toster.show_toast('SECURITY ALERT ', 'due to the infomation transfer', threaded=True, icon_path=None, duration=3)

import time

while toster.notification_active():
    time.sleep(0.1)