import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(title = "**Please drink water now**",
                            message = "Human body is almost 75% water. Please drink enough water to stay healthy",
                            app_icon = "icon.ico",
                            timeout = 10)
        time.sleep(60*60)
