z = float(input("Enter the length of the zander in centimeters: "))

size = 42

if z >= size:
    print("Congratulations! You can keep the zander.")
else:
    below_limit = size
    print(f"The zander is too small. Release it back into the lake. It's {below_limit:.f} centimeters below the size limit.")