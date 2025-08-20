# PROJECT 1--TEMPERATURE CONVERTER

import os
from datetime import datetime


class InvalidUnitError(Exception):
    pass


class TemperatureConverter:
    units = {
        'Celsius': '*C',
        'Fahrenheit': '*F',
        'Kelvin': '*K'
    }

    abbreviations = {
        'C': 'Celsius',
        'F': 'Fahrenheit',
        'K': 'Kelvin'
    }

    log_file = "temperature_log.txt"

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    @classmethod
    def from_input(cls):
        while True:
            try:
                unit_input = input("Enter temperature unit (C, F, K or full name): ").strip().title()

                if len(unit_input) == 1:
                    unit_input = unit_input.upper()
                    if unit_input in cls.abbreviations:
                        full_unit = cls.abbreviations[unit_input]
                    else:
                        raise InvalidUnitError("Unknown unit abbreviation. Try again.")


                elif unit_input in cls.units:
                    full_unit = unit_input
                else:
                    raise InvalidUnitError("Unknown unit name. Try again.")

                break

            except InvalidUnitError as e:
                print(e)

        while True:
            try:
                value_input = float(input("Enter the temperature value: "))
                break
            except ValueError:
                print("Invalid number. Please enter a numeric value.")

        return cls(value_input, full_unit)

    def convert(self):
        try:
            if self.unit == "Celsius":
                f = (self.value * 9 / 5) + 32
                k = self.value + 273.15
                return {"Fahrenheit": f, "Kelvin": k}

            elif self.unit == "Fahrenheit":
                c = (self.value - 32) * 5 / 9
                k = c + 273.15
                return {"Celsius": c, "Kelvin": k}

            elif self.unit == "Kelvin":
                c = self.value - 273.15
                f = (c * 9 / 5) + 32
                return {"Celsius": c, "Fahrenheit": f}
        except Exception as e:
            print(f"Error during conversion: {e}")
            return {}

    def log_conversion(self, conversions):
        """Write conversion details to a log file."""
        try:
            with open(self.log_file, "a") as file:
                file.write(f"{datetime.now()} | Original: {self.value}{self.units[self.unit]} | ")
                for u, v in conversions.items():
                    file.write(f"{u}: {round(v, 2)}{self.units[u]} | ")
                file.write("\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")

    def __str__(self):
        return f"{self.value}{self.units[self.unit]}"


#  Main Loop
try:
    while True:
        temp = TemperatureConverter.from_input()
        conversions = temp.convert()

        print(f"\nOriginal: {temp}")
        for u, v in conversions.items():
            print(f"{u}: {round(v, 2)}{TemperatureConverter.units[u]}")

        # Write to file
        temp.log_conversion(conversions)
        print(f" Conversion saved to {TemperatureConverter.log_file}")

        again = input("\nDo you want to convert another temperature? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
