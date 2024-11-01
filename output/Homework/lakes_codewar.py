def likes(names):
    # Считаем количество людей, которые лайкнули
    count = len(names)

    if count == 0:
        return "no one likes this"
    elif count == 1:
        return f"{names[0]} likes this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {count - 2} others like this"


# Примеры использования
print(likes([]))  # no one likes this
print(likes(["Alice"]))  # Alice likes this
print(likes(["Alice", "Bob"]))  # Alice and Bob like this
print(likes(["Alice", "Bob", "Charlie"]))  # Alice, Bob and Charlie like this
print(likes(["Alice", "Bob", "Charlie", "David"]))  # Alice, Bob and 2 others like this
