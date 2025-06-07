# Permutation-Sorting Algorithms & Complexity

We assume every input list is a **permutation** of the integers  
\(\{1,2,\dots,n\}\).  This document summarises the classical sorting
algorithms implemented in `permutation_sorting.py`, gives their
complexity bounds, and leaves placeholders for your empirical
measurements.

---

## 1 How many permutations?

A permutation of length \(n\) is any ordering of the \(n\) distinct
items.  The total number of such orderings is

\[
n! \;=\; 1\times2\times3\times\dots\times n .
\]

---

## 2 Sorting algorithms

| Short name | Section |
|------------|---------|
| Bubble sort | § 2.1 |
| Insertion sort | § 2.2 |
| Merge sort | § 2.3 |
| Quick sort | § 2.4 |
| Heap sort | § 2.5 |

Each subsection contains a **formal** definition and a **plain-language**
intuition.

### 2.1 Bubble sort
**Formal.**  Repeatedly scan adjacent pairs \((a_j,a_{j+1})\).  
If \(a_j>a_{j+1}\) swap them.  After the \(i\)-th full pass the last
\(i\) elements are in final position.  Worst-case comparisons:
\(\tfrac{n(n-1)}{2}\Rightarrow\Theta(n^{2})\) time; extra space
\(O(1)\).

**Plain words.**  Keep “bubbling” the biggest item to the end of the
list by swapping neighbours that are out of order.  Simple but slow.

---

### 2.2 Insertion sort
**Formal.**  For each index \(i\) insert \(a_i\) into the already
sorted prefix \(a_0\dots a_{i-1}\) by shifting larger elements right.  
Worst-case (reverse order) does \(\Theta(n^{2})\) shifts; extra space
\(O(1)\).

**Plain words.**  Like sorting playing cards: take the next card and
slide it left until it fits.

---

### 2.3 Merge sort
**Formal.**  Recurrence  
\(T(n)=2\,T(\tfrac{n}{2})+n\Rightarrow T(n)=\Theta(n\log n)\).  
Merging halves needs a buffer of length \(n\Rightarrow O(n)\) extra
space.

**Plain words.**  Keep splitting the list in half, sort each half, then
*merge* them back together like a zipper.

---

### 2.4 Quick sort
**Formal.**  Pick a pivot, partition into “\< pivot”, “pivot”, “\> pivot”,
then recurse.  With a random pivot the expected height of the recursion
tree is \(\Theta(\log n)\); total work
\(\Theta(n\log n)\).  Recursion stack uses \(O(\log n)\) space on
average, \(O(n)\) in the worst case.

**Plain words.**  Choose a pivot value, shove smaller items left and
bigger items right, then sort each side.  Usually very fast, but can
slow drastically if the pivot choice is unlucky.

---

### 2.5 Heap sort
**Formal.**  (1) Build a max-heap in \(O(n)\).  (2) Repeat \(n-1\)
times: swap the root with the last element and heapify the reduced
heap.  Total \(\Theta(n\log n)\) time, \(O(1)\) extra memory.

**Plain words.**  Treat the array like a binary tree where parents are
bigger than children.  Keep removing the top (largest) item and fixing
the heap.

---

## 3 Permutation generation — Steinhaus–Johnson–Trotter (SJT)

SJT is **not** a sorter; it is an efficient way to *enumerate* all
\(n!\) permutations with a single adjacent swap between successive
outputs.

### 3.1 Formal description

1. Give every element a direction (← or →).  
2. A number is **mobile** if its arrow points to a neighbour that is
   smaller than itself.  
3. Find the **largest mobile** element \(m\).  
4. Swap \(m\) with the neighbour it points to.  
5. Reverse the direction of **every** element larger than \(m\).  
6. Repeat until no element is mobile (all arrows blocked).

Cost: one adjacent swap per permutation ⇒  
\(O(n)\) time and \(O(n)\) space *per permutation*,
\(O(n!\,n)\) overall.

### 3.2 Step-by-step example for \(n=3\)

Below each element carries its arrow; the largest mobile is **bold**.

| Step | State | Swap performed |
|------|-----------------|------------------|
| 0 | 1← 2← **3←** | start |
| 1 | 1← **3←** 2→ | swap 3 ↔ 2 |
| 2 | **3→** 1← 2→ | swap 3 ↔ 1 |
| 3 | 3→ 1← **2←** | swap 2 ↔ 1 |
| 4 | 3← **2←** 1→ | swap 2 ↔ 3 |
| 5 | **2→** 3← 1→ | swap 2 ↔ 3 |
| 6 | 2→ 3← 1→ | (no mobile ⇒ done) |

Numbers only:

\[
(1\,2\,3),\ (1\,3\,2),\ (3\,1\,2),\ (3\,2\,1),\ (2\,3\,1),\ (2\,1\,3).
\]

**Plain words.**  Every number marches left or right until it hits a
larger one.  Always move the biggest number that can move, then make
all bigger numbers turn around.  Continue until nobody can move—you’ve
visited every ordering exactly once.

---

## 4 Complexity cheat-sheets

### 4.1 Theoretical bounds for *sorting* algorithms

| Algorithm | Time (best) | Time (avg) | Time (worst) | Extra space |
|-----------|-------------|-----------|--------------|-------------|
| Bubble    | \(Θ(n^{2})\) | \(Θ(n^{2})\) | \(Θ(n^{2})\) | \(O(1)\) |
| Insertion | \(Θ(n)\) | \(Θ(n^{2})\) | \(Θ(n^{2})\) | \(O(1)\) |
| Merge     | \(Θ(n\log n)\) | \(Θ(n\log n)\) | \(Θ(n\log n)\) | \(O(n)\) |
| Quick     | \(Θ(n\log n)\) | \(Θ(n\log n)\) | \(Θ(n^{2})\) | \(O(\log n)\)\* |
| Heap      | \(Θ(n\log n)\) | \(Θ(n\log n)\) | \(Θ(n\log n)\) | \(O(1)\) |

\*Recursion stack; worst-case pivoting uses \(O(n)\).

### 4.2 Placeholders for empirical results

(Time in **ms**, memory in **kB**.)

| Algorithm | Runtime (ms) | Memory (kB) | Notes |
|-----------|--------------|-------------|-------|
| Bubble    | — | — | |
| Insertion | — | — | |
| Merge     | — | — | |
| Quick     | — | — | |
| Heap      | — | — | |

*SJT is excluded because it is a generator, not a sorter.*

---

## 5 Corner cases & caveats

* **Quick sort:** using the last element as pivot on an already-sorted
  permutation triggers the \(\Theta(n^{2})\) path and can exceed
  Python’s default recursion limit (≈ 1000).  
* **SJT:** for \(n=0\) the generator emits a single empty permutation,
  which is correct.

---

## 6 Measurement methodology

The following cells conduct a more detailed performance analysis. We will:
1. Run each sorting algorithm on 1000 different random permutations to estimate its average-case time complexity.
2. Run each sorting algorithm on a known worst-case input permutation to observe its worst-case time complexity.

This allows for a practical comparison of how the algorithms perform on average versus how they perform under stress conditions.