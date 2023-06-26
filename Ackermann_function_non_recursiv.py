def ack(m: int, n: int) -> int:
    stack = []

    while True:
        if m == 0:
            if stack:
                m = stack.pop()
                n += 1
            else:
                return n + 1
        elif n == 0:
            m -= 1
            n = 1
        else:
            stack.append(m - 1)
            n -= 1


if __name__ == '__main__':
    print(ack(3, 6))
