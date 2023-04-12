import itertools

def find_operations(target, numbers):
    for i in range(2, 7):
        for subset in itertools.combinations(numbers, i):
            for ops in itertools.product("+-*/", repeat=i-1):
                temp = list(subset)
                result = temp.pop(0)
                for j, op in enumerate(ops):
                    b = temp[j]
                    if op == "+":
                        result += b
                    elif op == "-":
                        result -= b
                        if result < 1:
                            break
                    elif op == "*":
                        result *= b
                    elif op == "/":
                        if b == 0 or result % b != 0:
                            break
                        result //= b
                else:
                    print(" ".join(str(x) for x in subset), " ".join(ops), "=", result)
                if result == target:
                    print("Winner.")
                    exit()

target = 476
numbers = [5,7,11,19,20,23]
find_operations(target, numbers)