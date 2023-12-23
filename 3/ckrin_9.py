def count_happy_numbers(length):
    if length % 2 != 0:
        return 0

    half_length = length // 2
    count = 0

    for i in range(10 ** (half_length - 1), 10 ** half_length):
        Olesa = list(map(int, str(i)))
        Vika = list(map(int, str(i)))

        if sum(Olesa) == sum(Vika):
            count += 1

    return count


