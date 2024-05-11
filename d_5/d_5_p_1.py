"""Solution of d_5_p_1_task.txt."""
from os.path import dirname, join

def convert_dependency_data(part_of_file: str) -> list:
    """
        Converts string of data to problem specific list of data
        :param part_of_file: string containg data specific to a dependency
        :result: list of lists containing the same data but in more elegant form
    """
    converted_data = []

    for line in part_of_file:
        converted_data.append(list(map(int, line.split(" "))))

    return converted_data

def track_number(dependency_data: list, my_number: int) -> int:
    """
        Tracks down my_number's destiny due to dependency_data
        :param dependency_data: the rules about tracking destiny of my_numbers
        :result: destiny
    """
    for dependency in dependency_data:
        if  dependency[1] <= my_number <= dependency[1]+dependency[2]-1:
            return (my_number-dependency[1]) + dependency[0]

    return my_number



def main() -> None:
    """
        Prints minimum location number corresponding to seed number
        and dependency data included in input.txt file.
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        input_file = file1.read()

    seed_to_soil_data = []
    soil_to_fertilizer_data = []
    fertilizer_to_water_data = []
    water_to_light_data = []
    light_to_temperature_data = []
    temperature_to_humidity_data = []
    humidity_to_location_data = []

    for part_of_file in input_file.split("\n\n"):
        part_of_file = part_of_file.split("\n")
        if part_of_file[0].find("seeds:")>-1:
            seeds = [int(s) for s in part_of_file[0].split() if s.isdigit()]
        dependency_data = convert_dependency_data(part_of_file[1:])
        match part_of_file[0].strip():
            case "seed-to-soil map:":
                seed_to_soil_data = dependency_data
            case "soil-to-fertilizer map:":
                soil_to_fertilizer_data = dependency_data
            case "fertilizer-to-water map:":
                fertilizer_to_water_data = dependency_data
            case "water-to-light map:":
                water_to_light_data = dependency_data
            case "light-to-temperature map:":
                light_to_temperature_data = dependency_data
            case "temperature-to-humidity map:":
                temperature_to_humidity_data = dependency_data
            case "humidity-to-location map:":
                humidity_to_location_data = dependency_data
            case _:
                continue

    seeds = [track_number(seed_to_soil_data,seed) for seed in seeds]
    seeds = [track_number(soil_to_fertilizer_data,seed) for seed in seeds]
    seeds = [track_number(fertilizer_to_water_data,seed) for seed in seeds]
    seeds = [track_number(water_to_light_data,seed) for seed in seeds]
    seeds = [track_number(light_to_temperature_data,seed) for seed in seeds]
    seeds = [track_number(temperature_to_humidity_data,seed) for seed in seeds]
    seeds = [track_number(humidity_to_location_data,seed) for seed in seeds]

    print(min(seeds))

if __name__ == "__main__":
    main()
