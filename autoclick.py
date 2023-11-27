import time
import mouse

def auto_click_at_current_location():
    try:

        while True:
            # Get the current mouse position
            # x, y = mouse.get_position()
            time.sleep(10)
            clickme = 0
            # Perform the click action at the current mouse position
            mouse.click('left')
            print(f"clicked{clickme}")
            clickme += 1
            # Wait for the specified interval
            time.sleep(40)

    except KeyboardInterrupt:
        print("\nScript terminated by user.")


# Start the auto-clicking script
auto_click_at_current_location()
