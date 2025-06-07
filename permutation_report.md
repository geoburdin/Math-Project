# Date-Sorting Algorithms & Complexity

We assume every input list is a **permutation** of n different dates. This document summarises the classical sorting
algorithms implemented in `permutation_sorting.py`, gives their complexity bounds, and leaves placeholders for your empirical
measurements.

---

## 1 How many permutations?

A permutation of length \(n\) is any ordering of the \(n\) distinct
dates. The total number of such orderings is

\[
n! \;=\; 1\times2\times3\times\dots\times n .
\]

// ...rest of sections 2.1-2.5 stay the same as they describe the algorithms which work the same way for dates...

## 3 Permutation generation with Dates

The SJT algorithm has been modified to work with dates instead of numbers. It generates all possible orderings of a given set of dates.

### 3.2 Step-by-step example for \(n=3\)

Below each date carries its arrow; the largest (latest) mobile date is **bold**.

| Step | State | Swap performed |
|------|-----------------|------------------|
| 0 | 2024-01-01← 2024-02-01← **2024-03-01←** | start |
| 1 | 2024-01-01← **2024-03-01←** 2024-02-01→ | swap Mar ↔ Feb |
// ...rest of the document stays the same...
