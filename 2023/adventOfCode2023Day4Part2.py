#start at 9:30 pm
# 9:58 end
# change make map of card # to winning in that card. So less reptetive loops
# Instead of queue, have a map for the rest for number (card number to amount to play)
import re
import queue

def scratch_off_winnings(file_name):
    card_queue = queue.Queue()
    card_count = 0

    with open(file_name, "r") as file:
        card_number = 0
        # Seems like readlines() is attached to the iterator, so I have to do this early
        for line in file:
            card_count += 1
            card_number += 1

            new_card_from_this_line = 0

            pipe_location = line.find("|")
            card_prefix = re.search(r'Card\s+\d+:\s', line)
            winning_numbers = line[card_prefix.end():pipe_location].split()
            my_numbers = line[pipe_location + 1:].split()
            for numString in winning_numbers:
                if numString in my_numbers:
                    new_card_from_this_line += 1
                    card_queue.put(int(card_number) + new_card_from_this_line)

            card_count += new_card_from_this_line

    with open(file_name, "r") as file:
        file_lines = file.readlines()
        while not card_queue.empty():
            card_number_to_scratch = card_queue.get()
            line_to_scratch = file_lines[card_number_to_scratch - 1]
            new_card_from_this_line = 0

            pipe_location = line_to_scratch.find("|")
            card_prefix = re.search(r'Card\s+\d+:\s', line_to_scratch)
            winning_numbers = line_to_scratch[card_prefix.end():pipe_location].split()
            my_numbers = line_to_scratch[pipe_location + 1:].split()
            for numString in winning_numbers:
                if numString in my_numbers:
                    new_card_from_this_line += 1
                    card_queue.put(int(card_number_to_scratch) + new_card_from_this_line)

            card_count += new_card_from_this_line
    
    return card_count

if __name__ == "__main__":
    print(scratch_off_winnings("adventOfCode2023Day4Input.txt"))