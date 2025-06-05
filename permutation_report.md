# Permutation Sorting Algorithms and Complexity

This report summarizes the sorting algorithms implemented in `permutation_sorting.py`.  We treat each input list as a permutation of the integers $\{1,\ldots,n\}$.

## Counting Permutations

A permutation of length $n$ is an ordered arrangement of the elements $\{1,\ldots,n\}$.  The total number of permutations is
\[
 n! \,=\, 1 \times 2 \times 3 \times \cdots \times n.
\]

Many algorithms in this project exploit the fact that each element appears exactly once.

## Sorting Algorithms

Below are the algorithms provided along with their time complexities.

### Bubble Sort

Bubble sort repeatedly swaps adjacent elements that are out of order.  For a permutation of length $n$ it makes at most
\[
 \sum_{i=1}^{n-1} i \;=\; \frac{n(n-1)}{2}
\]
comparisons, leading to $\mathcal{O}(n^2)$ time.

### Insertion Sort

Insertion sort builds the sorted permutation by inserting each element into its proper place among the previous ones.  The worst case occurs for a reversed permutation and also requires $\mathcal{O}(n^2)$ comparisons and swaps.

### Merge Sort

Merge sort divides the permutation into halves, recursively sorts each half, and then merges the results.  The recurrence
\[
 T(n) = 2\,T\Bigl(\frac{n}{2}\Bigr) + n
\]
solves to $\mathcal{O}(n\log n)$ time.  The algorithm uses additional space for merging, so its space complexity is $\mathcal{O}(n)$.

### Quick Sort

Quick sort chooses a pivot element and partitions the permutation into values less than or greater than the pivot.  The expected running time satisfies the recurrence
\[
 T(n) \approx n + \frac{1}{n}\sum_{k=0}^{n-1} \bigl(T(k) + T(n-1-k)\bigr) 
\]
and is $\mathcal{O}(n\log n)$ on average.  The sort is in-place, so the extra space is $\mathcal{O}(\log n)$ for the recursion stack.

### Heap Sort

Heap sort first converts the permutation into a binary heap and repeatedly extracts the maximum element.  Both heap construction and extraction phases take $\mathcal{O}(n\log n)$ time, and the algorithm runs in-place.

### Steinhaus--Johnson--Trotter Algorithm

This algorithm generates all $n!$ permutations by repeatedly swapping adjacent elements according to their directions.  Each swap changes the parity of the number of inversions, systematically visiting every permutation exactly once.  The generation cost is $\mathcal{O}(n!\,n)$ in total, or $\mathcal{O}(n)$ per permutation.
## Corner Cases

Some algorithms behave poorly on specific inputs. Using the last element as the pivot in quick sort causes worst-case recursion when the permutation is already sorted. If the length exceeds Python's recursion limit (roughly 1000), the implementation raises a `RecursionError`. The Steinhaus--Johnson--Trotter generator simply yields a single empty permutation when called with $n=0$.


## Empirical Testing

The script's `test_sorting_algorithm` function measures the time to sort a random permutation.  Because all inputs are permutations, we can assume there are no repeated values, simplifying comparisons.

## Conclusions

By examining permutations, we see that algorithms like merge sort, quick sort, and heap sort run in $\mathcal{O}(n\log n)$ time, while bubble sort and insertion sort are $\mathcal{O}(n^2)$.  The Steinhaus--Johnson--Trotter method provides an efficient means to enumerate all permutations.  Understanding these complexities helps in choosing the appropriate algorithm depending on the permutation size and required performance.
