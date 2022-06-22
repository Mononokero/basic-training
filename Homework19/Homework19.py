def len_nested(l):

    count = 0

    for i in l:
        if isinstance(i, list):
            count += len_nested(i)
        else:
            count += 1
    return count

if __name__ == "__main__":
    ll = [1, 2, 3, [1, 2, [1, 2], [4, [5, [6, [4]]], [3, 1]]]]
    r = len_nested(ll)
    print("Nested lists length:", r)

