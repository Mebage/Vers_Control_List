def biggest_power_of_two(A):
    try:
        A = int(A)
    except:
        print("Error: Please enter a valid number.")
        return
    if A < 1:
        print("There is no power of 2 for numbers smaller than 1.")
        return
    power = 1
    while power * 2 <= A:
        power *= 2
    return power
print(biggest_power_of_two(17))
