# -*- coding: utf-8 -*-
"""
Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку
повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента.
Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.
"""


def binary_search(arr, value):
    arr = arr[:]
    left = 0
    right = len(arr) - 1
    iterations = 0
    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1
        if arr[mid] < value:
            left = mid + 1
        elif arr[mid] > value:
            right = mid - 1
        else:
            return iterations, arr[mid]
    # If not found element, return upper_bound:
    upper_bound = arr[left] if left < len(arr) else None
    return iterations, upper_bound


def make_search(arr, value):
    iterations, upper_bound = binary_search(arr, value)
    print(f"Count of iterations: {iterations}")
    print(f"upper bound: {upper_bound}")


# Приклад використання:
sorted_array = [1.0, 2.5, 3.8, 5.2, 7.1, 9.0]
target_value = 7
make_search(sorted_array, target_value)
target_value = 10
make_search(sorted_array, target_value)
