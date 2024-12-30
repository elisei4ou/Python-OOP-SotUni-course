def solution():

    def integers():
        idx = 0
        while True:
            idx += 1
            yield idx

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            result.append(next(seq))
        return result


    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

