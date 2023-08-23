numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
total_odd_numbers = 0
total_even_numbers = 0
for x in numbers:
    if not x % 2:
        total_even_numbers += 1
    else:
        total_odd_numbers += 1
print("Number of even numbers :", total_even_numbers)
print("Number of odd numbers :", total_odd_numbers)
