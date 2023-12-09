# start 4:12 pm, dec 9, 2023
# 20-30 minute break
import re


# from https://stackoverflow.com/a/22808285
def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

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
                nodes = re.finditer(r'[0-9A-Z]{3}', line)
                node_string = []
                for node in nodes:
                    node_string.append(node.group(0))
                node_map[node_string[0]] = [node_string[1], node_string[2]]
    
    current_nodes = [node for node in node_map.keys() if node[2] == 'A']
    step_per_node = []

    # Go through all nodes and find steps for each to get to end individually
    for n in range(len(current_nodes)):
        current = current_nodes[n]
        steps_taken = 0
        print(n, len(current_nodes), current)
        while current[2] != 'Z':
            print(current)
    #        print(current_nodes)
    #        print("bro", current_node, left_right_sequence[steps_taken % len(left_right_sequence)], steps_taken % len(left_right_sequence))
            step_instruction = left_right_sequence[steps_taken % len(left_right_sequence)]
            if step_instruction == 'L':
                    current = node_map[current][0]
            else:
                    current = node_map[current][1]
            steps_taken +=1
        step_per_node.append(steps_taken)
    
    all_factors = []
    total = 1
    for step in step_per_node:
        prime_factorization = prime_factors(step)
        for factor in prime_factorization:
            if factor not in all_factors:
                all_factors.append(factor)
                total *= factor
    print(total) 
day8()