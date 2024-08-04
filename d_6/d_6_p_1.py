"""Solution of d_3_p_1_task.txt."""
from os.path import dirname, join

def find_win_product(times: list, dist: list) -> int:
    """
    Returns the multiplication of wins number according to d_6_p_1_task.txt
    :param times: times read from file
    :param times: distances to beat read from file
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
    Prints the multiplication of wins number according to d_6_p_1_task.txt
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()

    times = [int(s) for s in lines[0].split() if s.isdigit()]
    distances = [int(s) for s in lines[1].split() if s.isdigit()]

    print(find_win_product(times,distances))

if __name__ == "__main__":
    main()
