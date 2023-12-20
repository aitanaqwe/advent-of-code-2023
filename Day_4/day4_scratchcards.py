puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_4\day4_test_puzzle_input.txt', 'r').read().splitlines()

lines = [line.strip().split('|') for line in puzzle_input]

# Convert the string representations of numbers to integers
numbers_before_bar = [[int(num) for num in card.split()] for card in lines]

# Print the result
print("Numbers before the bar:")
for card_numbers in numbers_before_bar:
    print(card_numbers)

# If needed, you can also obtain numbers after the bar in a similar way
numbers_after_bar = [[int(num) for num in card.split()] for card in lines]
print("\nNumbers after the bar:")
for card_numbers in numbers_after_bar:
    print(card_numbers)