"""Solution of d_4_p_1_task.txt."""
from os.path import dirname, join


def main() -> None:
    """
        xxx
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        input_file = file1.read()


    for part_of_file in input_file.split("\n\n"):
        part_of_file = part_of_file.split("\n")
        match part_of_file[0]:
            case "seed-to-soil map:":
                print(part_of_file[1:])
            case "soil-to-fertilizer map":
                print(part_of_file[1:])
            case "fertilizer-to-water map:":
                print(part_of_file[1:])
            case "water-to-light map:":
                print(part_of_file[1:])
            case "light-to-temperature map:":
                print(part_of_file[1:])
            case "temperature-to-humidity map:":
                print(part_of_file[1:])
            case "humidity-to-location map:":
                print(part_of_file[1:])


if __name__ == "__main__":
    main()
