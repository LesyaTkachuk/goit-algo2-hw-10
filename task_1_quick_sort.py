from collections import defaultdict
from colorama import Fore, init, Style
import matplotlib.pyplot as plt
from timeit import timeit
import random

init()


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.randint(0, len(arr) - 1)

    middle = [arr[pivot]]
    left = [x for x in arr if x < arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr, pivot=0):
    if len(arr) <= 1:
        return arr

    middle = [arr[pivot]]
    left = [x for x in arr if x < arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


if __name__ == "__main__":
    # test of algorithms
    test_array = [45, 8, 34, 25, 89, 90, 15, 21, 78, 4]

    print(randomized_quick_sort(test_array))
    print(deterministic_quick_sort(test_array))
    print("\n")

    numbers_list_10000 = [random.randint(0, 10000) for _ in range(10000)]
    numbers_list_50000 = [random.randint(0, 50000) for _ in range(50000)]
    numbers_list_100000 = [random.randint(0, 100000) for _ in range(100000)]
    numbers_list_500000 = [random.randint(0, 500000) for _ in range(500000)]

    array = [
        numbers_list_10000,
        numbers_list_50000,
        numbers_list_100000,
        numbers_list_500000,
    ]
    titles = [
        "10_000",
        "50_000",
        "100_000",
        "500_000",
    ]

    # defining a dictionary to store the execution times
    results = defaultdict(list)

    for i, arr in enumerate(array):
        results[titles[i]].append(timeit(lambda: randomized_quick_sort(arr), number=5))
        results[titles[i]].append(
            timeit(lambda: deterministic_quick_sort(arr), number=5)
        )
        results[titles[i]].append(
            timeit(lambda: deterministic_quick_sort(arr, pivot=len(arr) - 1), number=5)
        )
        results[titles[i]].append(
            timeit(lambda: deterministic_quick_sort(arr, pivot=len(arr) // 2), number=5)
        )

    print(
        Fore.LIGHTBLUE_EX
        + "\n---------------------------------------------------------------------------------------------------------------------------------------------"
        + Style.RESET_ALL
    )
    print(
        Fore.GREEN
        + f"{'Number of elements':<20} | {'Randomized QS':<20} | {'Det. QS - pivot[0]':<20} | {'Det. QS - pivot[len(arr)-1]':<20} | {'Det. QS - pivot[len(arr)//2]':<20}"
        + Style.RESET_ALL
    )
    print(
        Fore.LIGHTBLUE_EX
        + "\n---------------------------------------------------------------------------------------------------------------------------------------------"
        + Style.RESET_ALL
    )
    for key, value in results.items():
        print(
            f"{key:<20} | {value[0]:<20.6f} | {value[1]:<20.6f} | {value[2]:<20.6f} | {value[3]:<20.6f}"
        )

    print(
        Fore.LIGHTBLUE_EX
        + "\n---------------------------------------------------------------------------------------------------------------------------------------------"
        + Style.RESET_ALL
    )

    # plotting the results
    # Extract number of elements and execution times
    num_elements = [int(k.replace('_', '')) for k in results.keys()]
    times = list(zip(*results.values()))

    # Labels for the sorting methods
    methods = ["Randomized QS", "Det. Pivot First", " Det. Pivot Last", " Det. Pivot Middle"]

    # Plot
    plt.figure(figsize=(10, 6))
    for time, method in zip(times, methods):
        plt.plot(num_elements, time, marker='o', label=method)

    # Labels and title
    plt.xlabel("Number of Elements")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time of Quick Sort Variants")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")  # Optional: Log scale for better visualization

    # Show plot
    plt.show()
