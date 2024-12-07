import sys
import test

# area.py
def abbreviate(unit):
    result = ""
    unit0 = unit.lower()
    match unit1:
        case "square yard":
            result = "yd2"
        case "square foot":
            result = "ft2"
        case "square inch":
            result = "in2"
        case "square mile":
            result = "mi2"
        case "square kilometer":
            result = "km2"
        case "square meter":
            result = "m2"
        case _:
            result = unit2
    return result


def normalize(num, unit):
    result = 0
    match unit:
        case "yd2":
            result = num * 9
        case "ft2":
            result = num
        case "in2":
            result = num / 144
        case "mi2":
            result = num * 27880000
        case "km2":
            result = num * 10760000
        case "m2":
            result = num * 10.764
    return result


def convert_area(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "yd2":
            result = num / 9
        case "ft2":
            result = num
        case "in2":
            result = num * 144
        case "mi2":
            result = num / 27880000
        case "km2":
            result = num / 10760000
        case "m2":
            result = num / 10.764
        case _:
            print(f"Unknown unit: '{to}'")
    result = round(result, 2)
    return result

# conversion.py
def display_valid_units():
    temps = ["Temperatures:", "f", "c", "k"]
    dists = ["Distances:", "mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
    masses = ["Masses:", "mg", "g", "kg", "oz", "lb", "t"]
    times = ["Times:", "s", "min", "h", "day", "week", "month", "year"]
    volumes = ["Volumes:", "mL", "L", "m3", "qt", "gal", "ft3"]
    areas = ["Areas:", "in2", "ft2", "yd2", "mi2", "m2", "km2"]
    speeds = ["Speeds:", "m/s", "km/h", "mph"]
    units = [temps, dists, masses, times, volumes, areas, speeds]
    for unit in units:
        for item in unit:
            print(item, end=" ")
        print("")


def check_cl_args():
    args = sys.argv
    if len(args) > 1:
        if "-h" in args or "--help" in args:
            display_valid_units()
            return None, False
        elif "-t" in args or "--test" in args:
            test.run_tests()
            return None, False
        return sys.argv, True
    else:
        return None, False


def select_conversion(arg):
    temps = ["f", "c", "k"]
    dists = ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
    masses = ["mg", "g", "kg", "oz", "lb", "t"]
    times = ["s", "min", "h", "day", "week", "month", "year"]
    volumes = ["mL", "L", "m3", "qt", "gal", "ft3"]
    areas = ["in2", "ft2", "yd2", "mi2", "m2", "km2"]
    speeds = ["m/s", "km/h", "mph"]
    result = ""
    if arg in temps:
        result = "temperature"
    elif arg in dists:
        result = "distance"
    elif arg in masses:
        result = "mass"
    elif arg in times:
        result = "time"
    elif arg in volumes:
        result = "volume"
    elif arg in areas:
        result = "area"
    elif arg in speeds:
        result = "speed"
    else:
        print("Unknown conversion.")
    return result


def convert(args):
    conversion = select_conversion(args[2])
    num = float(args[1])
    unit1 = args[2]
    unit2 = args[3]
    result = ""
    match conversion:
        case "temperature":
            result = convert_temperature(num, unit1, unit2)
        case "distance":
            result = convert_distance(num, unit1, unit2)
        case "mass":
            result = convert_mass(num, unit1, unit2)
        case "time":
            result = convert_time(num, unit1, unit2)
        case "volume":
            result = convert_volume(num, unit1, unit2)
        case "area":
            result = convert_area(num, unit1, unit2)
        case "speed":
            result = convert_speed(num, unit1, unit2)
    print(f"{args[1]}{unit1} = {result}{unit2}")

# distance.py
def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "meter":
            result = "m"
        case "kilometer":
            result = "km"
        case "centimeter":
            result = "cm"
        case "millimeter":
            result = "mm"
        case "inch":
            result = "in"
        case "foot":
            result = "ft"
        case "yard":
            result = "yd"
        case "mile":
            result = "mi"
        case _:
            result = unit
    return result


def check_unit_type(unit):
    metric = ["m", "km", "cm", "mm"]
    imperial = ["in", "ft", "yd", "mi"]
    result = ""
    if unit in metric:
        result = "metric"
    elif unit in imperial:
        result = "imperial"
    return result


def normalize(num, unit):
    unit = unit.lower()
    unit = abbreviate(unit)
    result = 0
    unit_type = check_unit_type(unit)
    if unit_type == "metric":
        temp = 0
        match unit:
            case "m":
                temp = num
            case "km":
                temp = num * 1000
            case "cm":
                temp = num / 100
            case "mm":
                temp = num / 1000
        result = temp
    elif unit_type == "imperial":
        temp = 0
        match unit:
            case "in":
                temp = num / 36
            case "ft":
                temp = num / 3
            case "yd":
                temp = num
            case "mi":
                temp = num * 1760
        result = temp
    else:
        print(f"Unrecognized unit: '{unit}'")
    return result


def convert_from_imperial(num, to):
    result = 0
    match to:
        case "m":
            result = num / 1.094
        case "km":
            result = num / 1094
        case "cm":
            result = num * 91.44
        case "mm":
            result = num * 914.4
        case "in":
            result = num * 36
        case "ft":
            result = num * 3
        case "yd":
            result = num
        case "mi":
            result = num / 1760
    result = round(result, 2)
    return result


def convert_from_metric(num, to):
    result = 0
    match to:
        case "m":
            result = num
        case "km":
            result = num / 1000
        case "cm":
            result = num * 100
        case "mm":
            result = num * 1000
        case "in":
            result = num * 39.37
        case "ft":
            result = num * 3.281
        case "yd":
            result = num * 1.094
        case "mi":
            result = num / 1609
    result = round(result, 2)
    return result


def convert_distance(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    unit_type = check_unit_type(frm)
    match unit_type:
        case "imperial":
            return convert_from_imperial(num, to)
        case "metric":
            return convert_from_metric(num, to)

# mass.py
def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "gram":
            result = "g"
        case "kilogram":
            result = "kg"
        case "milligram":
            result = "mg"
        case "ton":
            result = "t"
        case "pound":
            result = "lb"
        case "ounce":
            result = "oz"
        case _:
            result = unit
    return result


def check_unit_type(unit):
    metric = ["g", "kg", "mg"]
    imperial = ["t", "lb", "oz"]
    result = ""
    if unit in metric:
        result = "metric"
    elif unit in imperial:
        result = "imperial"
    return result


def normalize(num, unit):
    unit = abbreviate(unit)
    result = 0
    unit_type = check_unit_type(unit)
    if unit_type == "metric":
        match unit:
            case "mg":
                result = num / 1000
            case "g":
                result = num
            case "kg":
                result = num * 1000
    elif unit_type == "imperial":
        match unit:
            case "oz":
                result = num / 16
            case "lb":
                result = num
            case "t":
                result = num * 2000
    else:
        print(f"Unrecognized unit: '{unit}'")
    result = round(result, 2)
    return result


def convert_from_imperial(num, to):
    result = 0
    match to:
        case "mg":
            result = num * 453600
        case "g":
            result = num * 453.6
        case "kg":
            result = num / 2.205
        case "oz":
            result = num * 16
        case "lb":
            result = num
        case "t":
            result = num / 2000
    result = round(result, 2)
    return result


def convert_from_metric(num, to):
    result = 0
    match to:
        case "mg":
            result = num * 1000
        case "g":
            result = num
        case "kg":
            result = num / 1000
        case "oz":
            result = num / 28.35
        case "lb":
            result = num / 453.6
        case "t":
            result = num / 907200
    result = round(result, 2)
    return result


def convert_mass(num, frm, to):
    num = normalize(num, frm)
    unit_type = check_unit_type(frm)
    match unit_type:
        case "imperial":
            return convert_from_imperial(num, to)
        case "metric":
            return convert_from_metric(num, to)

# my_time.py
def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "second":
            result = "s"
        case "minute":
            result = "min"
        case "hour":
            result = "h"
        case _:
            result = unit
    return result


def normalize(num, unit):
    result = 0
    unit = abbreviate(unit)
    match unit:
        case "s":
            result = num / 3600
        case "min":
            result = num / 60
        case "h":
            result = num
        case "day":
            result = num * 24
        case "week":
            result = num * 168
        case "month":
            result = num * 730
        case "year":
            result = num * 8760
        case _:
            print(f"Unrecognized unit: '{unit}'")
    return result


def convert_time(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "s":
            result = num * 3600
        case "min":
            result = num * 60
        case "h":
            result = num
        case "day":
            result = num / 24
        case "week":
            result = num / 168
        case "month":
            result = num / 730
        case "year":
            result = num / 8760
    result = round(result, 2)
    return result

# script.py
def main():
    args, cl_call = check_cl_args()
    if cl_call:
        convert(args)


if __name__ == "__main__":
    main()

# speed.py
def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "meters per second":
            result = "m/s"
        case "m per second":
            result = "m/s"
        case "kilometers per hour":
            result = "km/h"
        case "km per hour":
            result = "km/h"
        case "miles per hour":
            result = "mph"
        case "mi per hour":
            result = "mph"
        case _:
            result = unit
    return result


def normalize(num, unit):
    result = 0
    match unit:
        case "m/s":
            result = num
        case "km/h":
            result = num / 3.6
        case "mph":
            result = num / 2.237
    return result


def convert_speed(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "m/s":
            result = num
        case "km/h":
            result = num * 3.6
        case "mph":
            result = num * 2.237
    result = round(result, 2)
    return result

# temperature.py
def abbreviate(unit):
    result = ""
    unit = unit.lower()
    match unit:
        case "fahrenheit":
            result = "f"
        case "celsius":
            result = "c"
        case "kelvin":
            result = "k"
        case _:
            result = unit
    return result


def convert_temperature(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    result = 0
    if frm == "f":
        match to:
            case "c":
                result = (num - 32) * 5 / 9
            case "k":
                result = ((num - 32) * 5 / 9) + 273.15
            case "f":
                result = num
    elif frm == "c":
        match to:
            case "f":
                result = (num * 9 / 5) + 32
            case "k":
                result = num + 273.15
            case "c":
                result = num
    elif frm == "k":
        match to:
            case "f":
                result = (num - 273.15) * 9 / 5 + 32
            case "c":
                result = num - 273.15
            case "k":
                result = num
    result = round(result, 2)
    return result


def test_speed():
    print("\nTesting speeds:")
    s1 = 60
    s2 = 100
    s3 = 25
    res1 = convert_speed(s1, "mph", "km/h")
    res2 = convert_speed(s2, "m/s", "mph")
    res3 = convert_speed(s3, "km/h", "m/s")
    print(f"{s1}mph = {res1}km/h")
    print(f"{s2}m/s = {res2}mph")
    print(f"{s3}km/h = {res3}m/s")


def test_area():
    print("\nTesting areas:")
    a1 = 10
    a2 = 537
    a3 = 45
    res1 = convert_area(a1, "square foot", "square yard")
    res2 = convert_area(a2, "in2", "ft2")
    res3 = convert_area(a3, "mi2", "km2")
    print(f"{a1}ft^2 = {res1}yd^2")
    print(f"{a2}in^2 = {res2}ft^2")
    print(f"{a3}mi^2 = {res3}km^2")


def test_volume():
    print("\nTesting volumes:")
    vol1 = 2
    vol2 = 10000
    vol3 = 10
    res1 = convert_volume(vol1, "cubic foot", "gal")
    res2 = convert_volume(vol2, "gal", "L")
    res3 = convert_volume(vol3, "gal", "qt")
    print(f"{vol1}ft^3 = {res1}gal")
    print(f"{vol2}gal = {res2}L")
    print(f"{vol3}gal = {res3}qt")


def test_my_time():
    print("\nTesting times:")
    time1 = 50
    time2 = 6
    time3 = 36709
    res1 = convert_time(time1, "day", "second")
    res2 = convert_time(time2, "h", "month")
    res3 = convert_time(time3, "s", "day")
    print(f"{time1}day = {res1}s")
    print(f"{time2}h = {res2}month")
    print(f"{time3}s = {res3}day")


def test_mass():
    print("\nTesting masses:")
    mass1 = 8
    mass2 = 150
    mass3 = 2
    res1 = convert_mass(mass1, "g", "mg")
    res2 = convert_mass(mass2, "oz", "g")
    res3 = convert_mass(mass3, "t", "lb")
    print(f"{mass1}g = {res1}mg")
    print(f"{mass2}oz = {res2}g")
    print(f"{mass3}t = {res3}lb")


def test_temperature():
    print("\nTesting temperatures:")
    temp1 = 61
    temp2 = 11
    res1 = convert_temperature(temp1, "f", "c")
    res2 = convert_temperature(temp2, "c", "f")
    print(f"{temp1}f = {res1}c")
    print(f"{temp2}c = {res2}f")


def test_distance():
    print("\nTesting distances:")
    dist1 = 2735
    dist2 = 47
    dist3 = 1241
    dist4 = 1
    res1 = convert_distance(dist1, "ft", "km")
    res2 = convert_distance(dist2, "yard", "in")
    res3 = convert_distance(dist3, "mm", "yd")
    res4 = convert_distance(dist3, "mi", "mm")
    print(f"{dist1}ft = {res1}km")
    print(f"{dist2}yd = {res2}in")
    print(f"{dist3}mm = {res3}yd")
    print(f"{dist4}mi = {res4}mm")


def run_tests():
    test_temperature()
    test_distance()
    test_mass()
    test_my_time()
    test_volume()
    test_area()
    test_speed()
    print()

# volume.py
def check_unit_type(unit):
    metric = ["L", "mL", "m3"]
    imperial = ["gal", "qt", "ft3"]
    result = ""
    if unit in metric:
        result = "metric"
    elif unit in imperial:
        result = "imperial"
    return result


def abbreviate(unit):
    if len(unit) > 3:
        unit = unit.lower()
    result = ""
    match unit:
        case "liter":
            result = "L"
        case "milliliter":
            result = "mL"
        case "cubic meter":
            result = "m3"
        case "gallon":
            result = "gal"
        case "quart":
            result = "qt"
        case "cubic foot":
            result = "ft3"
        case _:
            result = unit
    return result


def normalize(num, unit):
    unit = abbreviate(unit)
    result = 0
    match unit:
        case "L":
            result = num * 1000
        case "mL":
            result = num
        case "m3":
            result = num * 1000000
        case "gal":
            result = num * 3785
        case "qt":
            result = num * 946.4
        case "ft3":
            result = num * 28320
        case _:
            print(f"Unrecognized unit: '{unit}'")
    return result


def convert_volume(num, frm, to):
    frm = abbreviate(frm)
    to = abbreviate(to)
    num = normalize(num, frm)
    result = 0
    match to:
        case "L":
            result = num / 1000
        case "mL":
            result = num
        case "m3":
            result = num / 1000000
        case "gal":
            result = num / 3785
        case "qt":
            result = num / 946.4
        case "ft3":
            result = num / 28320
    result = round(result, 3)
    return result
