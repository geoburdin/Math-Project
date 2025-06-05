import random
import time
from typing import List, Callable, Generator


def bubble_sort(arr: List[int]) -> List[int]:
    """Sort a list using bubble sort."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr: List[int]) -> List[int]:
    """Sort a list using insertion sort."""
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr: List[int]) -> List[int]:
    """Sort a list using merge sort."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """Sort a list using quick sort."""
    a = arr.copy()

    def _quick_sort(lo: int, hi: int) -> None:
        if lo < hi:
            p = partition(lo, hi)
            _quick_sort(lo, p - 1)
            _quick_sort(p + 1, hi)

    def partition(lo: int, hi: int) -> int:
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    _quick_sort(0, len(a) - 1)
    return a


def heap_sort(arr: List[int]) -> List[int]:
    """Sort a list using heap sort."""
    a = arr.copy()
    n = len(a)

    def heapify(size: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and a[left] > a[largest]:
            largest = left
        if right < size and a[right] > a[largest]:
            largest = right
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(i, 0)

    return a


def steinhaus_johnson_trotter(n: int) -> Generator[List[int], None, None]:
    """Generate permutations using the Steinhaus-Johnson-Trotter algorithm."""
    perm = list(range(1, n + 1))
    dirs = [-1] * n  # -1 for left, 1 for right
    yield perm.copy()

    while True:
        # Find the largest mobile element
        mobile_idx = -1
        mobile = -1
        for i in range(n):
            if dirs[i] == -1 and i != 0 and perm[i] > perm[i - 1] and perm[i] > mobile:
                mobile = perm[i]
                mobile_idx = i
            if dirs[i] == 1 and i != n - 1 and perm[i] > perm[i + 1] and perm[i] > mobile:
                mobile = perm[i]
                mobile_idx = i
        if mobile_idx == -1:
            return

        swap_with = mobile_idx + dirs[mobile_idx]
        perm[mobile_idx], perm[swap_with] = perm[swap_with], perm[mobile_idx]
        dirs[mobile_idx], dirs[swap_with] = dirs[swap_with], dirs[mobile_idx]
        mobile_idx = swap_with

        for i in range(n):
            if perm[i] > mobile:
                dirs[i] *= -1
        yield perm.copy()


def generate_permutation(n: int) -> List[int]:
    perm = list(range(1, n + 1))
    random.shuffle(perm)
    return perm


def test_sorting_algorithm(alg: Callable[[List[int]], List[int]], n: int) -> None:
    perm = generate_permutation(n)
    start = time.perf_counter()
    result = alg(perm)
    elapsed = time.perf_counter() - start
    print(f"{alg.__name__} sorted permutation: {result}")
    print(f"Time taken: {elapsed:.6f} seconds\n")


def demonstrate_corner_cases() -> None:
    """Show examples where an algorithm exhibits undesired behavior."""
    print("\nCorner case: quick_sort on an already sorted list of length 1500")
    try:
        quick_sort(list(range(1500)))
    except RecursionError as err:
        print("quick_sort failed with RecursionError:", err)

    print("\nCorner case: Steinhaus-Johnson-Trotter with n=0")
    print(list(steinhaus_johnson_trotter(0)))

    print("\nCorner case: sorting an empty list with bubble_sort")
    print(bubble_sort([]))


if __name__ == "__main__":
    N = 10
    algorithms = [bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort]
    for alg in algorithms:
        test_sorting_algorithm(alg, N)

    print("\nFirst 5 permutations from Steinhaus-Johnson-Trotter:")
    sjt_gen = steinhaus_johnson_trotter(3)
    for _ in range(5):
        try:
            print(next(sjt_gen))
        except StopIteration:
            break

    demonstrate_corner_cases()
