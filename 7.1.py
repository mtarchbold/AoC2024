with open('7.txt') as file:
    lines =  file.readlines()

def solvable(test_value, numbers):
    def helper(index, current_value):
        if index == len(numbers) - 1:
            return current_value == test_value
        for operator in ('+', '*'): 
            if helper(index + 1, eval(f"{current_value}{operator}{numbers[index + 1]}")):
                return True
        return False

    return helper(0, numbers[0])

total_calibration = 0
for line in lines:
    test_value, *numbers = map(int, line.replace(':','').strip().split())
    if solvable(test_value, numbers):
        total_calibration += test_value
print(total_calibration)
