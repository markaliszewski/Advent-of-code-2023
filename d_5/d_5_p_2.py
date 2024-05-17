"""Solution of d_5_p_2_task.txt."""
from os.path import dirname, join

class AlmanacStepmap:
    """
    Defines all mapping quantities and methods for given relation 
    """
    def __init__(self, part_maps: str):
        """
            :param part_maps: part of file containing maps
        """
        unpacked_partial_maps = []
        for part_map in part_maps:
            unpacked_partial_maps.append([int(number) for number\
                                     in part_map.split() if number.isdigit()])

        self.partial_map = []
        self.partial_map_reversed = []

        for unpacked_partial_map in unpacked_partial_maps:
            self.partial_map.append([\
                unpacked_partial_map[0], unpacked_partial_map[0] + unpacked_partial_map[2] - 1,\
                    unpacked_partial_map[1], unpacked_partial_map[1] + unpacked_partial_map[2] - 1])
            self.partial_map_reversed.append([\
                unpacked_partial_map[1], unpacked_partial_map[1] + unpacked_partial_map[2] - 1,\
                unpacked_partial_map[0], unpacked_partial_map[0] + unpacked_partial_map[2] - 1])

        self.partial_map = sorted(self.partial_map, key=lambda x: x[0])
        self.partial_map_reversed = sorted(self.partial_map_reversed, key=lambda x: x[0])

    def range_backward(self, dest_range: list) -> list:
        """
            devides given range due to mapping demands and transform it into source ranges  
            :param dest_range: given range
            :return: mapping from divided range into destination
        """
        dest_range_start_point = dest_range[0]
        dest_range_end_point = dest_range[1]

        # start_points = sorted(list(set(x for row in start_points for x in row)))
        map_for_range = []
        if self.partial_map[0][0] > dest_range_start_point:
            if self.partial_map[0][0] <= dest_range_end_point:
                dest_range = [dest_range_start_point, self.partial_map[0][0] - 1]
                source_range = [dest_range_start_point, self.partial_map[0][0] - 1]
                map_for_range.append(dest_range + source_range)
                dest_range_start_point = dest_range[1] + 1
            else:
                dest_range = [dest_range_start_point, dest_range_end_point]
                source_range = [dest_range_start_point, dest_range_end_point]
                map_for_range.append(dest_range + source_range)
                return map_for_range

        for dependency_range in self.partial_map:
            shift = dependency_range[2] - dependency_range[0]
            if  dependency_range[0] <= dest_range_start_point < dependency_range[1]:
                start_index_map = dest_range_start_point
                if dest_range_end_point < dependency_range[1]:
                    end_index_map = dest_range_end_point
                else:
                    end_index_map = dependency_range[1]
                dest_range = [start_index_map, end_index_map]
                source_range = [start_index_map + shift, end_index_map + shift]
                map_for_range.append(dest_range + source_range)
                dest_range_start_point = dest_range[1] + 1

        if self.partial_map[-1][1] < dest_range_end_point:
            dest_range = [dest_range_start_point, dest_range_end_point]
            source_range = [dest_range_start_point, dest_range_end_point]
            map_for_range.append(dest_range + source_range)

        return map_for_range

    def ranges_backward(self, dest_ranges: list) -> list:
        """
            Preforms range_backward for multiple ranges
            :param dest_ranges: multiple destination ranges
            :return: mapping from divided ranges into source ranges
        """
        dest_ranges = sorted(dest_ranges, key=lambda x: x[0])
        map_for_ranges = []
        for dest_range in dest_ranges:
            map_for_ranges.extend(self.range_backward(dest_range))
        return map_for_ranges




    def unit_range_forward(self, unit_source_range: list) -> list:
        """
            transform unit source range into destination range  
            :param unit_source_range: source range that can be transform through mapping
                                    with no need for addictional divisions
            :return: destination range
        """
        source_range_start_point = unit_source_range[0]
        source_range_end_point = unit_source_range[1]

        # POZAMIENIAĆ FUNCKJĘ BACKWARD NA FORWARD

def main() -> None:
    """
    Finds minimum location for all given seeds
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        input_file = file1.read()

    for part_of_file in input_file.split("\n\n"):
        part_of_file = part_of_file.split("\n")
        if part_of_file[0].find("seeds:")>-1:
            seeds_packed = [int(s) for s in part_of_file[0].split() if s.isdigit()]
        match part_of_file[0].strip():
            case "seed-to-soil map:":
                s2s = AlmanacStepmap(part_of_file[1:])
            case "soil-to-fertilizer map:":
                s2f = AlmanacStepmap(part_of_file[1:])
            case "fertilizer-to-water map:":
                f2w = AlmanacStepmap(part_of_file[1:])
            case "water-to-light map:":
                w2l = AlmanacStepmap(part_of_file[1:])
            case "light-to-temperature map:":
                l2t = AlmanacStepmap(part_of_file[1:])
            case "temperature-to-humidity map:":
                t2h = AlmanacStepmap(part_of_file[1:])
            case "humidity-to-location map:":
                h2l = AlmanacStepmap(part_of_file[1:])
            case _:
                continue

    seeds = []
    for seed, range_length in zip(seeds_packed[0::2], seeds_packed[1::2]):
        seeds.append([seed,seed + range_length-1])

    print(h2l.ranges_backward([[0,68],[69,100]]))
if __name__ == "__main__":
    main()
