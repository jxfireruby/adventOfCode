# start 8:00 pm
# end 8:08 pm
import re

def fix_kerning(finditer_result):
    squashed_string = ""
    for result in finditer_result:
        squashed_string += result.group(0)
    return squashed_string

def day_6(file_name):
    with open(file_name, "r") as file:
        file_list = file.readlines()
        time_results = re.finditer(r'\d+', file_list[0])
        actual_time = int(fix_kerning(time_results))
        distance_results = re.finditer(r'\d+', file_list[1])
        actual_distance = int(fix_kerning(distance_results))
        
        amount_of_ways_to_beat_record = 0

        # if you have 7 seconds, there are 8 (0-7) ways to wind the boat
        for time_winding in range(actual_time + 1):
            speed = 1 * time_winding
            distance = speed * (actual_time - time_winding)
            if distance > actual_distance:
                amount_of_ways_to_beat_record += 1
        
        return amount_of_ways_to_beat_record

if __name__ == "__main__":
    print(day_6('input.txt'))