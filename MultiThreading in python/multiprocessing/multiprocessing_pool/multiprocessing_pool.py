def f(n):
    return n*n

if __name__ == "__main__":
    array = [1,2,3,4,5,6]

    result = []
    for i in array:
        result.append(f(array))

    print(result)