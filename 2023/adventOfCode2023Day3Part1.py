# 7:19 PM start
# Read prompt 40-60 minutes ago before dinner
# Completed 8:43. Read Python regex module, manga, and MVs during
import re

with open("adventOfCode2023Day3Input.txt", "r") as file:
    file_lines = list(file)
    sum = 0
    for i in range(len(file_lines)):
        line = file_lines[i]
        results = re.finditer(r'\d+', line)
        if results:
            for match in results:
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
                special_char = re.match(r'[^0-9.\n]', file_lines[i][left_start])

                if special_char:
#                    print(match.group(0))
                    sum += int(match.group(0))
                    continue

                # right_end is for the end of the range. Last number is range - 1
                special_char = re.match(r'[^0-9.\n]', file_lines[i][right_end - 1])

                if special_char:
#                    print(match.group(0))
                    sum += int(match.group(0))
                    continue

                for number_index in range(left_start, right_end):
                    if i > 0:
                        special_char = re.match(r'[^0-9.\n]', file_lines[i - 1][number_index])
                        if special_char:
                            break
                    if i < len(file_lines) - 1:
                        special_char = re.match(r'[^0-9.\n]', file_lines[i + 1][number_index])
                        if special_char:
                            break

                if special_char:
#                    print(match.group(0))
                    sum += int(match.group(0))
                    continue
    print(sum)