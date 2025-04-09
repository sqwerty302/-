def find_min_max(arr):
    if not arr:
        raise ValueError("Массив пуст.")

    min_val = max_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val


try:
    user_input = input("Введите элементы массива через пробел: ")
    arr = list(map(int, user_input.strip().split()))
    min_val, max_val = find_min_max(arr)
    print(f"Минимальное значение: {min_val}")
    print(f"Максимальное значение: {max_val}")
except ValueError as e:
    print("Ошибка:", e)
