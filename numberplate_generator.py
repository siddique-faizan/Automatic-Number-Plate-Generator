import datetime
import json
import os

current_year = datetime.datetime.now().year

print("Welcome to the Irish Number Plate Generator!")

while True:
    try:
        car_year = int(input("Enter your car year: "))
        car_month = int(input("Enter your month (1-12): "))

        if car_year < 1987:
            raise ValueError("Year too early for modern Irish plates")
        
        if car_year > current_year:
            raise ValueError("Year has not been released yet")
        
        if car_month < 1 or car_month > 12:
            raise ValueError("Month must be between 1 and 12")
        break

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")


# Year identifier
year_identifier = car_year % 100


# Half year
if car_month <= 6:
    half = 1
else:
    half = 2


# Registration period
if half == 1:
    registration_period = "January-June"
else:
    registration_period = "July-December"


# Format year with leading zero if needed
year_str = str(year_identifier).zfill(2)


# County codes
county_codes = {
    "Dublin": "D", "Cork": "C", "Galway": "G", "Limerick": "L",
    "Meath": "MH", "Wicklow": "W", "Kildare": "KE", "Westmeath": "WH",
    "Tipperary": "T", "Wexford": "WX", "Carlow": "CW", "Donegal": "DL",
    "Monaghan": "MN", "Cavan": "CN", "Sligo": "SO", "Roscommon": "RN",
    "Louth": "LH", "Offaly": "OY", "Laois": "LS", "Kerry": "KY",
    "Clare": "CE", "Waterford": "WD", "Leitrim": "LM", "Longford": "LD",
    "Mayo": "MO", "Kilkenny": "KK"
}


while True:

    county = input("Enter your county: ").strip().title()

    if county in county_codes:
        f_county = county_codes[county]
        break
    else:
        print(f"{county} not recognised. Valid counties: {', '.join(county_codes.keys())}")


# Sequence number stored in JSON
file_name = "plates.json"

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        plates = json.load(file)
else:
    plates = {}


# Create unique key for each registration series
if car_year >= 2013:
    plate_key = f"{year_str}{half}-{f_county}"
else:
    plate_key = f"{year_str}-{f_county}"


if plate_key not in plates:
    plates[plate_key] = 1


sequence = plates[plate_key]


# Increase number for next plate
plates[plate_key] += 1


# Save updated JSON
with open(file_name, "w") as file:
    json.dump(plates, file, indent=4)


# Final plate
if car_year >= 2013:

    plate = f"{year_str}{half}-{f_county}-{sequence}"

else:

    plate = f"{year_str}-{f_county}-{sequence}"


print(f"\nYour Irish number plate: {plate}")
print(f"Registered: {registration_period} {car_year}")
print(f"County: {county}")