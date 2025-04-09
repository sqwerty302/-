def convert_to_12_hour_format(hours, minutes):
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        print("Некорректное время.")
        return

    period = "AM" if hours < 12 else "PM"
    hour_12 = hours % 12
    if hour_12 == 0:
        hour_12 = 12

    print(f"{hour_12}:{minutes:02d} {period}")


try:
    hours = int(input("Введите часы (0-23): "))
    minutes = int(input("Введите минуты (0-59): "))
    convert_to_12_hour_format(hours, minutes)
except ValueError:
    print("Пожалуйста, введите целые числа.")
