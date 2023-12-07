# start 7:40 pm
# end 8:00 pm
import re

def day_6(file_name):
    with open(file_name, "r") as file:
        file_list = file.readlines()
        time_results = re.finditer(r'\d+', file_list[0])
        time_list = [int(time.group(0)) for time in time_results]
        distance_results = re.finditer(r'\d+', file_list[1])
        record_distance_list = [int(distance.group(0)) for distance in distance_results]

        output_product = 1
        
        for race_number in range(len(time_list)):
            amount_of_ways_to_beat_record = 0
            time_limit = time_list[race_number]

            # if you have 7 seconds, there are 8 (0-7) ways to wind the boat
            for time_winding in range(time_limit + 1):
                speed = 1 * time_winding
                distance = speed * (time_limit - time_winding)
                if distance > record_distance_list[race_number]:
                    amount_of_ways_to_beat_record += 1
            
            output_product = output_product * amount_of_ways_to_beat_record
        
        return output_product

if __name__ == "__main__":
    print(day_6('input.txt'))