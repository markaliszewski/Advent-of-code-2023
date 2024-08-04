"""
    Solution of d_5_p_2_task.txt
    Unfortunatelly, it does not work well for final input.txt,
    but works for final input. I had already learned a lot from
    this task and I suppose further debugging will bring me no more
    than just 10-th star. Therefor, I decide to keep the solution as it is
    - at least for now.
"""
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

    def step_right(self, left_range: list, mapping: list) -> list:
        """
            devides given range due to mapping demands and transform it into right ranges
            :param left_range: given left range
            :return: mapping from divided left range into right range
        """
        left_range_start_point = left_range[0]
        left_range_end_point = left_range[1]

        # start_points = sorted(list(set(x for row in start_points for x in row)))
        map_for_range = []
        if mapping[0][0] > left_range_start_point:
            if mapping[0][0] <= left_range_end_point:
                left_range = [left_range_start_point, mapping[0][0] - 1]
                right_range = [left_range_start_point, mapping[0][0] - 1]
                map_for_range.append(left_range + right_range)
                left_range_start_point = left_range[1] + 1
            else:
                left_range = [left_range_start_point, left_range_end_point]
                right_range = [left_range_start_point, left_range_end_point]
                map_for_range.append(left_range + right_range)
                return map_for_range

        for dependency_range in mapping:
            shift = dependency_range[2] - dependency_range[0]
            if  dependency_range[0] <= left_range_start_point < dependency_range[1]:
                start_index_map = left_range_start_point
                if left_range_end_point < dependency_range[1]:
                    end_index_map = left_range_end_point
                else:
                    end_index_map = dependency_range[1]
                left_range = [start_index_map, end_index_map]
                right_range = [start_index_map + shift, end_index_map + shift]
                map_for_range.append(left_range + right_range)
                left_range_start_point = left_range[1] + 1

        if mapping[-1][1] < left_range_end_point:
            left_range = [left_range_start_point, left_range_end_point]
            right_range = [left_range_start_point, left_range_end_point]
            map_for_range.append(left_range + right_range)

        return map_for_range

    def steps_right(self, left_ranges: list, mapping: list) -> list:
        """
            Preforms range_backward for multiple ranges
            :param left_ranges: multiple destination ranges
            :return: mapping from divided ranges into source ranges
        """
        left_ranges = sorted(left_ranges, key=lambda x: x[0])
        map_for_ranges = []
        for left_range in left_ranges:
            map_for_ranges.extend(self.step_right(left_range,mapping))
        return map_for_ranges


    def ranges_forward(self, source_range: list) -> list:
        """
            transform source_range into destination range  
            :param source_range: source range that can be transform through mapping
            :return: destination range
        """
        if any(isinstance(i, list) for i in source_range):
            destination_ranges = self.steps_right(source_range, self.partial_map_reversed)
        else:
            destination_ranges = self.step_right(source_range, self.partial_map_reversed)

        return [range[2:] for range in destination_ranges]

    def ranges_backward(self, dest_range: list) -> list:
        """
            transform destination range into source range  
            :param dest_range: destiantion range that can be transform through mapping
            :return: source range
        """
        if any(isinstance(i, list) for i in dest_range):
            source_ranges = self.steps_right(dest_range, self.partial_map)
        else:
            source_ranges = self.step_right(dest_range, self.partial_map)

        return [range[2:] for range in source_ranges]

class Almanac:
    """
    Contains AlmanacStepmap objects related to mappings in the given file.
    Include only one method which returns minimum location for provided seed ranges.
    """
    def __init__(self, maps: str):
        """
            :param maps: file containing maps
        """
        for part_of_file in maps.split("\n\n"):
            part_of_file = part_of_file.split("\n")
            match part_of_file[0].strip():
                case "seed-to-soil map:":
                    self.s2s = AlmanacStepmap(part_of_file[1:])
                case "soil-to-fertilizer map:":
                    self.s2f = AlmanacStepmap(part_of_file[1:])
                case "fertilizer-to-water map:":
                    self.f2w = AlmanacStepmap(part_of_file[1:])
                case "water-to-light map:":
                    self.w2l = AlmanacStepmap(part_of_file[1:])
                case "light-to-temperature map:":
                    self.l2t = AlmanacStepmap(part_of_file[1:])
                case "temperature-to-humidity map:":
                    self.t2h = AlmanacStepmap(part_of_file[1:])
                case "humidity-to-location map:":
                    self.h2l = AlmanacStepmap(part_of_file[1:])
                case _:
                    continue
    def track_seed_location(self,seeds: list):
        """
            track seeds locations through all mappings
            :param seeds: seeds numbers
            :return: locations correponding to seeds
        """
        # print(seeds)
        soils = self.s2s.ranges_forward(seeds)
        # print(soils)
        ferts = self.s2f.ranges_forward(soils)
        # print(ferts)
        waters = self.f2w.ranges_forward(ferts)
        # print(waters)
        lights = self.w2l.ranges_forward(waters)
        # print(lights)
        temps = self.l2t.ranges_forward(lights)
        # print(temps)
        humids = self.t2h.ranges_forward(temps)
        # print(humids)
        locs = self.h2l.ranges_forward(humids)
        # print(locs)
        return locs

def main() -> None:
    """
    Finds minimum location for all given seeds
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./sample_input.txt")
    # file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        input_file = file1.read()

    for part_of_file in input_file.split("\n\n"):
        part_of_file = part_of_file.split("\n")
        if part_of_file[0].find("seeds:")>-1:
            seeds_packed = [int(s) for s in part_of_file[0].split() if s.isdigit()]

    seeds = []
    for seed, range_length in zip(seeds_packed[0::2], seeds_packed[1::2]):
        seeds.append([seed,seed + range_length-1])

    input_almanac = Almanac(input_file)
    seeds_locations = input_almanac.track_seed_location(seeds)
    min_location = min([min(locs) for locs in seeds_locations])
    print(min_location)


if __name__ == "__main__":
    main()
