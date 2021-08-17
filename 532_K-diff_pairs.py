import random
def pair(keys: list, k: int) ->int:
    counter: int = 0
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
                if abs(keys[i] - keys[j]) == k:
                    counter+=1
    return counter

def main():
    values = [random.randint(0, 10) for _ in range(5)]
    print(values)
    print(pair(values, 3))

if __name__ == '__main__':
    main()