import cmath as c

def handle_value_error(a):
    while True:
        try:
            if int(a):
                int_a = int(a)
                return int_a
            elif float(a):
                float_a = float(a)
                return float_a
        except ValueError:
            print("Please enter a valid value!")
            break


def handle_yes_or_no():
    while True:
        a = input("Enter your choice (Y/N): ")
        if a.lower() == "y" or a.lower() == "n":
            return a.lower()
        else:
            print("Please enter y or n!")

#Regex pattern for getting x and y from x+yi(complex number)
complex_pattern = r"([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?j"
