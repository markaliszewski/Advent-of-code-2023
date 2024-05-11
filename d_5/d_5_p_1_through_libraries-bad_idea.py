"""Solution of d_5_p_1_task.txt."""
from os.path import dirname, join

def add_dependency_to_dict(dependency_dict: dict, part_of_file: str) -> None:
    for line in part_of_file:
        x, y, z = map(int, line.split(" "))
        dependency_dict.update(dict((y+i,x+i) for i in range(z)))

def track_number(dependency_dict: dict, my_number: int) -> int:
    try:
        return dependency_dict[my_number]
    except KeyError:
        return my_number



def main() -> None:
    """
        Does really work for too large numbers, e.g. provided input.txt
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        input_file = file1.read()

    seed_to_soil_dict = {}
    soil_to_fertilizer_dict = {}
    fertilizer_to_water_dict = {}
    water_to_light_dict = {}
    light_to_temperature_dict = {}
    temperature_to_humidity_dict = {}
    humidity_to_location_dict = {}

    for part_of_file in input_file.split("\n\n"):
        part_of_file = part_of_file.split("\n")
        if part_of_file[0].find("seeds:")>-1:
            seeds = [int(s) for s in part_of_file[0].split() if s.isdigit()]
        match part_of_file[0].strip():
            case "seed-to-soil map:":
                dict_to_update = seed_to_soil_dict
            case "soil-to-fertilizer map:":
                dict_to_update = soil_to_fertilizer_dict
            case "fertilizer-to-water map:":
                dict_to_update = fertilizer_to_water_dict
            case "water-to-light map:":
                dict_to_update = water_to_light_dict
            case "light-to-temperature map:":
                dict_to_update = light_to_temperature_dict
            case "temperature-to-humidity map:":
                dict_to_update = temperature_to_humidity_dict
            case "humidity-to-location map:":
                dict_to_update = humidity_to_location_dict
            case _:
                continue
        add_dependency_to_dict(dict_to_update,part_of_file[1:])
    locations = [track_number(humidity_to_location_dict,track_number(temperature_to_humidity_dict,\
            track_number(light_to_temperature_dict,track_number(water_to_light_dict,\
            track_number(fertilizer_to_water_dict,track_number(soil_to_fertilizer_dict,\
            track_number(seed_to_soil_dict,seed))))))) for seed in seeds]
    print(min(locations))


if __name__ == "__main__":
    main()
