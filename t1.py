# Task: Read the contents of 'data.txt' and print each line with line numbers

with open('data.txt', 'r') as file:
    line_number = 1
    # Use Copilot to complete the code to read and print each line with line numbers
    for line in file:
        # TODO: Complete the code here
         print(f"Line {line_number}: {line.strip()}")
         line_number += 1
