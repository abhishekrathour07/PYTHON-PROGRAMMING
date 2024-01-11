def filter_even_numbers(numbers):
    # Use a list comprehension to filter even numbers
    if numbers %2==0:
        return numbers

# Example usage
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(filter_even_numbers,input_numbers))

print("Original Numbers:", input_numbers)
print("Even Numbers:", result)
