import math


# PART 1
def cone_surface_area(r, h):
    surface_area = math.pi * r ** 2 + (math.pi * r) * math.sqrt(r ** 2 + h ** 2)
    return surface_area


def cone_volume(r, h):
    volume = (1 / 3) * math.pi * r ** 2 * h
    return volume


def get_inputs():
    # No validation
    # radius = float(input("Enter the radius (in feet): "))
    # height = float(input("Enter the height (in feet): "))

    # With Validation
    radius = get_nneg_float("Enter the radius (a non-negative float in feet): ")
    height = get_nneg_float("Enter the height (a non-negative float in feet): ")

    return radius, height


# PART 2
def is_nneg_float(s):
    try:
        value = float(s)
        return value >= 0 and not "e" in s.lower()
    except ValueError:
        return False


def get_nneg_float(p):
    while True:
        user_input = input(p)
        if is_nneg_float(user_input):
            return float(user_input)
        else:
            print("Must be a float value; please try again.")


def main():
    print("The program calculates the surface area and volume of a cone.")
    radius, height = get_inputs()
    print("--------------------------------")
    print(f"Radius: {round(radius, 2)} feet\nHeight: {round(height, 2)} feet")

    surface_area = cone_surface_area(radius, height)
    volume = cone_volume(radius, height)

    print(f"Surface Area: {round(surface_area, 2)}\nVolume: {round(volume, 2)}")
    print("--------------------------------")

# print(get_nneg_float("Enter a non-negative float (NN.NN): "))

main()
