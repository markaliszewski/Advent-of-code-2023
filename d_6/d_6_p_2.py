"""Solution of d_3_p_1_task.txt."""
from os.path import dirname, join

def find_win_product(times: list, dist: list) -> int:
    """
    Returns the wins number according to d_6_p_2_task.txt
    :param times: time read from file
    :param times: distance to beat read from file
    """
    win_product = 1
    for i, time in enumerate(times):
        win_sum = 0
        for boat_hold in range(1,time):
            if boat_hold*(time-boat_hold) > dist[i]:
                win_sum += 1
        win_product *= win_sum

    return win_product

def main() -> None:
    """
    Prints the wins number according to d_6_p_2_task.txt
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()

    times = [s for s in lines[0].split() if s.isdigit()]
    distances = [s for s in lines[1].split() if s.isdigit()]

    time = [int(''.join(times))]
    distance = [int(''.join(distances))]
    print(find_win_product(time, distance))

if __name__ == "__main__":
    main()
