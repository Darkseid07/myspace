#Hello
#Hello jb
class item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def kanpsack(w, arr):
    print(arr)
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    print(arr)
    finalvalue = 0.0
    for item in arr:
        if item.weight <= w:
            w -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * w / item.weight
            break
    return finalvalue


if __name__ == "__main__":
    w = 50
    arr = [item(60, 5), item(100, 20), item(120, 30)]
    print(arr)
    max_val = kanpsack(w, arr)

    print(max_val)
