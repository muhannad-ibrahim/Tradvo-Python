import base64
from appium import webdriver
from time import sleep
import os

# Configure paths
apk_path = "C:/Users/user/AndroidStudioProjects/apk/app/build/outputs/apk/debug/app-debug.apk"
screenshot_dir = "D:/Assessment/django_app_manager/apk_manager/screenshots"
video_dir = "D:/Assessment/django_app_manager/apk_manager/videos"
db_path = "/path/to/your/database.db"

if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

if not os.path.exists(video_dir):
    os.makedirs(video_dir)

desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",            
    "deviceName": "sdk_gphone_x86",       
    "app": apk_path,                      # Path to your APK file
    "automationName": "UiAutomator2",     # Automation framework to use
    "appWaitActivity": "*",               # Activity to wait for
    "noReset": True,                      # Don't reset app state between sessions
    "fullReset": False                    # Don't uninstall the app between sessions
}

# Initialize the Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

sleep(5)

driver.start_recording_screen()

# Capture the initial UI elements hierarchy and take a screenshot
initial_ui_hierarchy = driver.page_source
initial_screenshot_path = os.path.join(screenshot_dir, "initial_screen.png")
driver.save_screenshot(initial_screenshot_path)

# Simulate a click on the first button (customize the locator as needed)
try:
    first_button = driver.find_element_by_id("com.example.apk:id/button_id")
    first_button.click()
    screen_changed = True
except:
    screen_changed = False

# Capture the final UI elements hierarchy and take another screenshot
final_screenshot_path = os.path.join(screenshot_dir, "final_screen.png")
driver.save_screenshot(final_screenshot_path)

sleep(10)
# Stop the video recording and save it
video_data = driver.stop_recording_screen()
video_data = base64.b64decode(video_data)
video_path = os.path.join(video_dir, "app_evaluation.mp4")
with open(video_path, "wb") as video_file:
    video_file.write(video_data)

print(f"Initial screenshot saved at: {initial_screenshot_path}")
print(f"Final screenshot saved at: {final_screenshot_path}")
print(f"Video recording saved at: {video_path}")
print(f"Screen changed after button click: {'Yes' if screen_changed else 'No'}")

driver.quit()