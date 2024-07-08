import json
from PIL import Image
import time

def read_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def write_config(filename, config):
    with open(filename, 'w') as file:
        json.dump(config, file)

def get_led_id_from_user():
    while True:
        try:
            print("\n HERE ARE THE LED IDs:")
            print("""
LT = 132  M = 136  RT = 144
LM = 130           RM = 160
LB = 129           RB = 192

""")
            print("""
        ____________
       |LT   M    RT|
       |            |
       |LM        RM|
       |            |
       |LB        RB|
       |____________|
             ||
""")
            
            led_id = int(input("Enter the LED ID (number not the letters): "))
            return led_id
        except ValueError:
            print("Please enter an ID for the LED.")

def main(led_id):
    config_file = r'D:\config.json'

    config = read_config(config_file)
    config['solid_color']['led_bits'] = led_id
    write_config(config_file, config)
    print(f"You selected {led_id} and it is now written to the config file.")

    # Read the config file again to confirm the change
    updated_config = read_config(config_file)
    print(f"Config file values for 'solid_color.led_bits' are now set to: {updated_config['solid_color']['led_bits']}")
      
    

if __name__ == "__main__":
    while True:
        led_id = get_led_id_from_user()
        main(led_id)
        
        user_choice = input("To select a different LED press 1 or press Enter to exit: ")

        if user_choice.strip() != '1':  # Exits if input is anything other than '1'
            print("Exiting the program.")
            break