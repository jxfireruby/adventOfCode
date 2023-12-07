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
                    # Match is faster with regex starting. Search if faster if search value is string literal
                    digit = re.match(r'\d', file_lines[i][left_start])

                    # find whole number after finding digit
                    if digit:
    #                    print(match.group(0))
                        gear_number_in_line = re.finditer(r'\d+', file_lines[i][0:match.start()])
                        for gear_number_candidate in gear_number_in_line:
                            if gear_number_candidate.start() < right_end and gear_number_candidate.end() > left_start:
                                print("left right", left_start, right_end)
                                print("gear left, right", gear_number_candidate.start(), gear_number_candidate.end())
                                print("gear", gear_number_candidate.group(0))
                                gears.append(int(gear_number_candidate.group(0)))
                    
                    # right_end is for the end of the range. Last digit is range - 1
                    digit = re.match(r'\d', file_lines[i][right_end - 1])

                    if digit:
    #                    print(match.group(0))
                        gear_number_in_line = re.finditer(r'\d+', file_lines[i][match.end():])
                        for gear_number_candidate in gear_number_in_line:
                            if gear_number_candidate.start() < right_end and gear_number_candidate.end() > left_start:
                                print("left right", left_start, right_end)
                                print("gear left, right", gear_number_candidate.start(), gear_number_candidate.end())
                                print("gear", gear_number_candidate.group(0))
                                gears.append(int(gear_number_candidate.group(0)))

                    for number_index in range(left_start, right_end):
                        if i > 0:
                            line_index = i - 1
                            digit = re.match(r'\d', file_lines[line_index][number_index])
                            if digit:
                                gear_number_in_line = re.finditer(r'\d+', file_lines[line_index])
                                for gear_number_candidate in gear_number_in_line:
                                    if gear_number_candidate.start() < right_end and gear_number_candidate.end() > left_start:
                                        print("left right", left_start, right_end)
                                        print("gear left, right", gear_number_candidate.start(), gear_number_candidate.end())
                                        print("gear", gear_number_candidate.group(0))
                                        gears.append(int(gear_number_candidate.group(0)))
                        if i < len(file_lines) - 1:
                            line_index = i + 1
                            digit = re.match(r'\d', file_lines[line_index][number_index])
                            if digit:
                                gear_number_in_line = re.finditer(r'\d+', file_lines[line_index])
                                for gear_number_candidate in gear_number_in_line:
                                    if gear_number_candidate.start() < right_end and gear_number_candidate.end() > left_start:
                                        print("left right", left_start, right_end)
                                        print("gear left, right", gear_number_candidate.start(), gear_number_candidate.end())
                                        print("gear", gear_number_candidate.group(0))
                                        gears.append(int(gear_number_candidate.group(0)))
                    # Only part that has to change if assumption is wrong
                    if len(gears) >= 2:
                        print(gears[0], gears[1])
                        sum = sum + (gears[0] * gears[1])
        return sum

if __name__ == '__main__':
    print(day_3_part_2("adventOfCode2023Day3Input.txt"))