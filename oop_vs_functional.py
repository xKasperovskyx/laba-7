#процедурний стиль
import random


def bubble_sort_optimized(array_: list) -> tuple[list, int]:
    array = array_.copy()
    n = len(array)
    comparisons = 0
    for j in range(n - 1):
        swapped = False
        for i in range(n - j - 1):
            comparisons += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
    return array, comparisons


def quicksort(array, comparisons=0):
    if len(array) < 2:
        return array, comparisons

    pivot = array[0]
    less = []
    greater = []

    for i in array[1:]:
        comparisons += 1
        if i <= pivot:
            less.append(i)
        else:
            greater.append(i)

    sorted_less, left_comparisons = quicksort(less)
    sorted_greater, right_comparisons = quicksort(greater)

    total_comparisons = comparisons + left_comparisons + right_comparisons

    return sorted_less + [pivot] + sorted_greater, total_comparisons


def main(array_length=100, num_trials=100):
    arr1 = [64, 34, 25, 12, 22, 11, 90, 100, 1, 3, 4, 7, 8, 9, 11, 12, 16]
    sorted_arr1, comp_count1 = bubble_sort_optimized(arr1)
    print(f"Bubble Sort -> Відсортований масив: {sorted_arr1}, Кількість порівнянь: {comp_count1}")

    arr2 = [64, 34, 25, 12, 22, 11, 90, 100, 1, 3, 4, 7, 8, 9, 11, 12, 16]
    sorted_arr2, comp_count2 = quicksort(arr2)
    print(f"Quick Sort -> Відсортований масив: {sorted_arr2}, Кількість порівнянь: {comp_count2}")

    bubble_comparisons_total = 0
    quick_comparisons_total = 0
    for i in range(num_trials):
        test_array = [random.randint(0, 1000) for _ in range(array_length)]

        _, bubble_comparisons = bubble_sort_optimized(test_array)
        _, quick_comparisons = quicksort(test_array)

        bubble_comparisons_total += bubble_comparisons
        quick_comparisons_total += quick_comparisons

    print(f"Середня кількість порівнянь у Bubble Sort: {bubble_comparisons_total / num_trials}")
    print(f"Середня кількість порівнянь у QuickSort: {quick_comparisons_total / num_trials}")


if __name__ == "__main__":
    main()

#ооп
class Triangle:
    def __init__(self, a, b=None, c=None):
        if isinstance(a, Triangle):
            self.__a = a.__a
            self.__b = a.__b
            self.__c = a.__c
            if hasattr(a, "info"):
                self.info = a.info
        else:
            assert self.is_exists(a, b, c)
            self.__a = a
            self.__b = b
            self.__c = c

    @staticmethod
    def is_exists(a, b, c):
        return a + b > c and a + c > b and c + b > a


t = Triangle(3, 4, 5)
print(id(t))

t.info = "Description of triangle"
print(vars(t))

t2 = Triangle(t)
print(id(t2))

print(vars(t2))