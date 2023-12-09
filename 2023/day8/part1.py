# start 2:54 pm, dec 9, 2023
# 30-40 minute break
# end 4:12 pm
import re

def day8():
    # Make map
    left_right_sequence = ""
    node_map = {}
    with open("input.txt", "r") as file:
        for line in file:
            # First line is left/right sequence
            left_right_sequence = (re.match(r'[LR]+', line)).group(0)
            break

        for line in file:
            #lines with = means this is a line with mapping
            if re.search(r'=', line):
                nodes = re.finditer(r'[A-Z]{3}', line)
                node_string = []
                for node in nodes:
                    node_string.append(node.group(0))
                node_map[node_string[0]] = [node_string[1], node_string[2]]

    # Follow map through nodes
    current_node = 'AAA'
    steps_taken = 0
    while current_node != 'ZZZ':
        print("bro", current_node, left_right_sequence[steps_taken % len(left_right_sequence)], steps_taken % len(left_right_sequence))
        step_instruction = left_right_sequence[steps_taken % len(left_right_sequence)]
        if step_instruction == 'L':
            current_node = node_map[current_node][0]
        else:
            current_node = node_map[current_node][1]
        steps_taken += 1
    print("last current:", current_node)
    print("LR lenght:", len(left_right_sequence))
    print("steps taken:", steps_taken)
        
day8()