#start time 9:14 pm
#finish at 9:30 pm
import re

def scratch_off_winnings(file_name):
    with open(file_name, "r") as file:
        sum = 0
        for line in file:
            line_score = 0

            pipe_location = line.find("|")
            card_prefix = re.search(r'Card\s+\d+:\s', line)
            winning_numbers = line[card_prefix.end():pipe_location].split()
            my_numbers = line[pipe_location + 1:].split()
            for num in winning_numbers:
                if num in my_numbers:
                    if line_score == 0:
                        line_score = 1
                    else:
                        line_score *= 2
            sum += line_score

        return sum


if __name__ == "__main__":
    print(scratch_off_winnings("adventOfCode2023Day4Input.txt"))