#11:05pm start
#12:39 am end
# Input Format: result source range
# Assumption: no caps in range
# map source result
import re

def calculate_map(start_value, map_used):
    for map in map_used:
        if start_value >= map[0] and start_value < map[0] + map[2]:
            #print("start", start_value, map[0], map[0] + map[2])
            return start_value + (map[1] - map[0])
    return start_value

def somethine(file_name):
    seed_soil_map = []
    soil_fert_map = []
    fert_water_map = []
    water_light_map = []
    light_temp_map = []
    temp_humid_map = []
    humid_loc_map = []
    seed_to_soil = False
    soil_to_fertilizer = False
    fertilizer_to_water = False
    water_to_light  = False
    light_to_temperature = False
    temperature_to_humidity = False
    humidity_to_location = False
    with open(file_name, "r") as file:
        for line in file:
            result = re.search(r'[a-z]+-to-[a-z]+', line)
            if result:
                if result.group(0) == "seed-to-soil":
                    seed_to_soil = True
                    soil_to_fertilizer = False
                    fertilizer_to_water = False
                    water_to_light  = False
                    light_to_temperature = False
                    temperature_to_humidity = False
                    humidity_to_location = False
                elif result.group(0) == "soil-to-fertilizer":
                    seed_to_soil = False
                    soil_to_fertilizer = True
                    fertilizer_to_water = False
                    water_to_light  = False
                    light_to_temperature = False
                    temperature_to_humidity = False
                    humidity_to_location = False
                elif result.group(0) == "fertilizer-to-water":
                    seed_to_soil = False
                    soil_to_fertilizer = False
                    fertilizer_to_water = True
                    water_to_light  = False
                    light_to_temperature = False
                    temperature_to_humidity = False
                    humidity_to_location = False
                elif result.group(0) == "water-to-light":
                    seed_to_soil = False
                    soil_to_fertilizer = False
                    fertilizer_to_water = False
                    water_to_light  = True
                    light_to_temperature = False
                    temperature_to_humidity = False
                    humidity_to_location = False
                elif result.group(0) == "light-to-temperature":
                    seed_to_soil = False
                    soil_to_fertilizer = False
                    fertilizer_to_water = False
                    water_to_light  = False
                    light_to_temperature = True
                    temperature_to_humidity = False
                    humidity_to_location = False
                elif result.group(0) == "temperature-to-humidity":  
                    seed_to_soil = False
                    soil_to_fertilizer = False
                    fertilizer_to_water = False
                    water_to_light  = False
                    light_to_temperature = False
                    temperature_to_humidity = True
                    humidity_to_location = False
                elif result.group(0) == "humidity-to-location":
                    seed_to_soil = False
                    soil_to_fertilizer = False
                    fertilizer_to_water = False
                    water_to_light  = False
                    light_to_temperature = False
                    temperature_to_humidity = False
                    humidity_to_location = True
            else:
                mapping = re.search(r'\d+\s\d+\s\d+', line)
                if mapping:
                    split_mapping = mapping.group(0).split()
                    if seed_to_soil:
                        seed_soil_map.append([int(split_mapping[1]), int(split_mapping[0]), int(split_mapping[2])])
                    elif soil_to_fertilizer:
                        soil_fert_map.append([int(split_mapping[1]), int(split_mapping[0]), int(split_mapping[2])])
                    elif fertilizer_to_water:
                        fert_water_map.append([int(split_mapping[1]), int(split_mapping[0]), int(split_mapping[2])])
                    elif water_to_light:
                        water_light_map.append([int(split_mapping[1]), int(split_mapping[0]), int(split_mapping[2])])
                    elif light_to_temperature:
                        light_temp_map.append([int(split_mapping[1]), int(split_mapping[0]), int(split_mapping[2])])
                    elif temperature_to_humidity:
                        temp_humid_map.append([int(split_mapping[1]), int(split_mapping[0]), int(split_mapping[2])])
                    elif humidity_to_location:
                        humid_loc_map.append([int(split_mapping[1]), int(split_mapping[0]), int(split_mapping[2])])

    lowest = -1
    with open(file_name, "r") as file:
        for line in file:
            split_line = line.split()
            seeds = split_line[1:]
            for seedStr in seeds:
                seed = int(seedStr)
                soil = calculate_map(seed, seed_soil_map)
                fert = calculate_map(soil, soil_fert_map)
                water = calculate_map(fert, fert_water_map)
                light = calculate_map(water, water_light_map)
                temp = calculate_map(light, light_temp_map)
                humid = calculate_map(temp, temp_humid_map)
                loc = calculate_map(humid, humid_loc_map)
                #print(seed, soil, fert, water, light, temp,humid, loc)
                if lowest == -1:
                    lowest = loc
                elif loc < lowest:
                    lowest = loc
            break
    print(lowest)
somethine('input.txt')
        
