# 8:45 pm start, 9:00 pause 10:00 restart
# Assumption, max 2 numbers near a *
import re
import unittest

def day_3_part_2(file_name):
    with open(file_name, "r") as file:
        file_lines = list(file)
        sum = 0
        for i in range(len(file_lines)):
            print("+++++++++++++++++++++++++++++i", i)
            line = file_lines[i]
            results = re.finditer(r'[*]', line)
            if results:
                for match in results:
                    print("Match", match)
                    gears = []
                    # Look around each match
                    try:
                        left_start = match.start() - 1
                        file_lines[i][left_start]
                    except:
                        left_start = match.start()
                    try:
                        right_end = match.end() + 1
                        file_lines[i][right_end]
                    except:
                        right_end = match.end()

                    # Find Number to left or right of gear
                    gear_number_in_line = re.finditer(r'\d+', file_lines[i])
                    for gear_number_candidate in gear_number_in_line:
                        if gear_number_candidate.end() == match.start() or gear_number_candidate.start() == match.end():
                            print("same line", int(gear_number_candidate.group(0)), end=" ")
                            gears.append(int(gear_number_candidate.group(0)))

                    # Find number in row above
                    if i > 0:
                        line_index = i - 1
                        gear_number_in_line = re.finditer(r'\d+', file_lines[line_index])
                        for gear_number_candidate in gear_number_in_line:
                            if gear_number_candidate.end() >= match.start() and gear_number_candidate.start() <= match.end():
                                print("above line", int(gear_number_candidate.group(0)), end=" ")
                                gears.append(int(gear_number_candidate.group(0)))
                    
                    # Find number in row below
                    if i < len(file_lines) - 1:
                        line_index = i + 1
                        gear_number_in_line = re.finditer(r'\d+', file_lines[line_index])
                        for gear_number_candidate in gear_number_in_line:
                            if gear_number_candidate.end() >= match.start() and gear_number_candidate.start() <= match.end():
                                print("below line", int(gear_number_candidate.group(0)), end=" ")
                                gears.append(int(gear_number_candidate.group(0)))
                    print()
                    for b in gears:
                        print(b, end=" ")
                    print()
                    if len(gears) >= 2:
                        sum = sum + (gears[0] * gears[1])
                        print(sum)
        return sum

if __name__ == '__main__':
    print(day_3_part_2("adventOfCode2023Day3Input.txt"))