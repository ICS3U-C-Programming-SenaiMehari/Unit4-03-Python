def calculate_squares(num):
    for i in range(num + 1):
        square = i**2
        print(f"{i}^2 = {square}")


while True:
    try:
        user_input = int(input("Enter a whole number: "))
        if user_input < 0:
            print("Please enter a non-negative number.")
            continue
        calculate_squares(user_input)
        break  # Exit the loop if the input is valid and calculation is done
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
