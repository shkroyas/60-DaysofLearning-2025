from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Reminder",
            message="This is a reminder to take a break!",
            app_icon="C:\\Users\\LOQ\\Downloads\\app_draw_14085.ico",  
            app_name="Reminder App",
            timeout=5  # Notification will be visible for 5 seconds
        )
        time.sleep(3600)