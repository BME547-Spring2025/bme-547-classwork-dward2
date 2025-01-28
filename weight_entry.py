def input_weight_entry():
    print("Enter patient weight in form of ## units (e.g., 105 lb)")
    weight_input = input("Enter weight: ")
    weight_in_kg = parse_weight_input(weight_input)
    print("The patient weight of {} kg will be stored "
          "in database.".format(weight_in_kg))


def parse_weight_input(weight_input):
    if weight_input.strip(" ").find(" ") < 0:
        weight, units = parse_when_no_space(weight_input)
    else:
        weight, units = weight_input.split()
    weight = float(weight)
    if units.lower() in ["lb", "lbs", "pound", "pounds"]:
        weight_kg = convert_lb_to_kg(weight)
    elif units.lower() in ["kg", "kgs", "kilos", "kilograms"]:
        weight_kg = weight
    else:
        weight_kg = 0
    weight_kg = round(weight_kg)
    return weight_kg


def convert_lb_to_kg(weight_lb):
    weight_kg = weight_lb / 2.20462
    return weight_kg
    

def parse_when_no_space(weight_input):
    weight_in = weight_input.strip(" ")
    for i, char in enumerate(weight_in):
        if char.isnumeric() or char in ".-":
            pass
        else:
            break
    weight = weight_input[:i]
    units = weight_input[i:]
    return weight, units


if __name__ == "__main__":
    input_weight_entry()
