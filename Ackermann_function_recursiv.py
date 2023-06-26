def ack(n: int, m: int):
    if n == 0:
        return m + 1
    if m == 0:
        return ack(n - 1, 1)

    return ack(n - 1, ack(n, m - 1))


if __name__ == '__main__':
    print(ack(3, 6))

