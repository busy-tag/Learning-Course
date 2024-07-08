import json

class PatternUnit:
    def __init__(self, led_bits=127, color="0000FF", speed=5, delay=50):
        """
        Initialize the PatternUnit object with optional default values.
        
        :param led_bits: Integer value for the LED bits (default: 127)
        :param color: String representing the color in hexadecimal format (default: "0000FF")
        :param speed: Integer value representing the speed (default: 5)
        :param delay: Integer value representing the delay in milliseconds (default: 50)
        """
        self.led_bits = led_bits
        self.color = color
        self.speed = speed
        self.delay = delay

    def __repr__(self):
        return f"PatternUnit(led_bits={self.led_bits}, color='{self.color}', speed={self.speed}, delay={self.delay})"

    def display_info(self):
        """
        Display the details of the PatternUnit.
        """
        print(f"LED Bits: {self.led_bits}")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed}")
        print(f"Delay: {self.delay}")

def read_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def write_config(filename, config):
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

def save_pattern_units(config, pattern_units):
    """
    Save a list of PatternUnit objects to the custom_pattern_arr in the config.
    """
    config["custom_pattern_arr"] = [unit.__dict__ for unit in pattern_units]

def prompt_for_pattern_unit():
    """
    Prompt the user for each field to create a new PatternUnit.
    """
    default_values = {
        "led_bits": 127,
        "color": "0000FF",
        "speed": 5,
        "delay": 50
    }

    try:
        led_bits_input = input("Enter LED bits (integer, or press Enter for default): ").strip()
        led_bits = int(led_bits_input) if led_bits_input else default_values["led_bits"]

        color_input = input("Enter color (hex code, e.g., 00FF00, or press Enter for default): ").strip()
        color = color_input if color_input else default_values["color"]

        speed_input = input("Enter speed (integer 1-100, or press Enter for default): ").strip()
        speed = int(speed_input) if speed_input else default_values["speed"]

        delay_input = input("Enter delay (integer in milliseconds, 1000 milliseconds = 1 second, or press Enter for default): ").strip()
        delay = int(delay_input) if delay_input else default_values["delay"]

        return PatternUnit(led_bits=led_bits, color=color, speed=speed, delay=delay)

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        return prompt_for_pattern_unit()  # Retry until valid input is provided

def main():
    config_file = r'D:\config.json'

    # Step 1: Read the config file
    print("Reading existing config file...")
    config = read_config(config_file)

    # Step 2: Clear existing patterns
    print("Clearing existing patterns...")
    config["custom_pattern_arr"] = []

    # Step 3: Add new pattern units interactively
    new_pattern_units = []

    while True:
        print("\nAdding a new pattern unit...")
        new_unit = prompt_for_pattern_unit()
        new_pattern_units.append(new_unit)

        # Ask if the user wants to add another pattern unit
        add_another = input("Do you want to add another pattern unit? (y/n): ").strip().lower()
        if add_another != 'y':
            break

    # Step 4: Prompt user for repeat times
    while True:
        try:
            repeat_times = int(input("Enter how many times to repeat this pattern (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Step 5: Save the new patterns and repeat times to the config
    save_pattern_units(config, new_pattern_units)
    config["pattern_repeat"] = repeat_times
    write_config(config_file, config)
    print("\nConfig file updated successfully with the new patterns and repeat times.")

    # Step 6: Confirm the updated config
    updated_config = read_config(config_file)
    print("\nUpdated Patterns in Config:")
    for unit in updated_config.get("custom_pattern_arr", []):
        print(unit)
    print(f"\nPattern repeat times: {updated_config.get('pattern_repeat', 'Not set')}")

if __name__ == "__main__":
    main()