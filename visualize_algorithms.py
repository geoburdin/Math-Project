# Visualization for sorting algorithms
import random
from typing import List, Iterable, Generator
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# -------- Sorting algorithm generators --------

def bubble_sort_steps(arr: List[int]) -> Generator[List[int], None, None]:
    a = arr.copy()
    yield a.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            yield a.copy()
    yield a.copy()


def insertion_sort_steps(arr: List[int]) -> Generator[List[int], None, None]:
    a = arr.copy()
    yield a.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            yield a.copy()
        a[j + 1] = key
        yield a.copy()
    yield a.copy()


def merge_sort_steps(arr: List[int]) -> Generator[List[int], None, None]:
    a = arr.copy()
    yield a.copy()

    def _merge_sort(left: int, right: int) -> Generator[List[int], None, None]:
        if left >= right:
            return
        mid = (left + right) // 2
        yield from _merge_sort(left, mid)
        yield from _merge_sort(mid + 1, right)
        merged = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if a[i] <= a[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(a[j])
                j += 1
        while i <= mid:
            merged.append(a[i])
            i += 1
        while j <= right:
            merged.append(a[j])
            j += 1
        for idx, val in enumerate(merged):
            a[left + idx] = val
            yield a.copy()

    yield from _merge_sort(0, len(a) - 1)
    yield a.copy()


def quick_sort_steps(arr: List[int]) -> Generator[List[int], None, None]:
    a = arr.copy()
    yield a.copy()

    def _quick_sort(lo: int, hi: int) -> Generator[List[int], None, None]:
        if lo >= hi:
            return
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
                yield a.copy()
        a[i], a[hi] = a[hi], a[i]
        yield a.copy()
        yield from _quick_sort(lo, i - 1)
        yield from _quick_sort(i + 1, hi)

    yield from _quick_sort(0, len(a) - 1)
    yield a.copy()


def heap_sort_steps(arr: List[int]) -> Generator[List[int], None, None]:
    a = arr.copy()
    yield a.copy()
    n = len(a)

    def heapify(size: int, i: int) -> Generator[List[int], None, None]:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < size and a[left] > a[largest]:
            largest = left
        if right < size and a[right] > a[largest]:
            largest = right
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            yield a.copy()
            yield from heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        yield a.copy()
        yield from heapify(i, 0)
    yield a.copy()


# -------- Visualization helpers --------

def _animate(arr: List[int], steps: Iterable[List[int]], title: str, interval: int = 200):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update(step):
        for rect, val in zip(bar_rects, step):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"{title}\nstep {iteration[0]}")
        return bar_rects

    ani = animation.FuncAnimation(fig, update, frames=steps, interval=interval, repeat=False, blit=False)
    plt.close(fig)
    return ani


# Public API

def animate_bubble_sort(arr: List[int], interval: int = 200):
    steps = bubble_sort_steps(arr)
    ani = _animate(arr, steps, "Bubble Sort", interval)
    plt.show()
    return ani


def animate_insertion_sort(arr: List[int], interval: int = 200):
    steps = insertion_sort_steps(arr)
    ani = _animate(arr, steps, "Insertion Sort", interval)
    plt.show()
    return ani


def animate_merge_sort(arr: List[int], interval: int = 200):
    steps = merge_sort_steps(arr)
    ani = _animate(arr, steps, "Merge Sort", interval)
    plt.show()
    return ani


def animate_quick_sort(arr: List[int], interval: int = 200):
    steps = quick_sort_steps(arr)
    ani = _animate(arr, steps, "Quick Sort", interval)
    plt.show()
    return ani


def animate_heap_sort(arr: List[int], interval: int = 200):
    steps = heap_sort_steps(arr)
    ani = _animate(arr, steps, "Heap Sort", interval)
    plt.show()
    return ani


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Visualize sorting algorithms")
    parser.add_argument("algorithm", choices=["bubble", "insertion", "merge", "quick", "heap"], help="Algorithm to visualize")
    parser.add_argument("--size", type=int, default=10, help="Size of the list")
    parser.add_argument("--interval", type=int, default=200, help="Interval between frames in ms")
    args = parser.parse_args()

    random_list = [random.randint(1, args.size * 3) for _ in range(args.size)]

    if args.algorithm == "bubble":
        animate_bubble_sort(random_list, args.interval)
    elif args.algorithm == "insertion":
        animate_insertion_sort(random_list, args.interval)
    elif args.algorithm == "merge":
        animate_merge_sort(random_list, args.interval)
    elif args.algorithm == "quick":
        animate_quick_sort(random_list, args.interval)
    elif args.algorithm == "heap":
        animate_heap_sort(random_list, args.interval)
