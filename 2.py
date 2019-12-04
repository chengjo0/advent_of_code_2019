import requests


def add(a: int, b: int):
    return a + b


def multiply(a: int, b: int):
    return a * b


def run(input: list, noun: int, verb: int):
    input[1] = noun
    input[2] = verb
    # print(input)

    for i in range(0, len(input) - 1, 4):
        # print(input[i:i+4])
        opCode = input[i]

        if opCode == 99:
            break

        pos1, pos2, insertPos = input[i+1:i+4]
        val1 = input[pos1]
        val2 = input[pos2]
        operation = operations[opCode]
        res = operation(val1, val2)
        input[insertPos] = res

    program_res = input[0]
    if program_res == 19690720:
        print("STOOOOOP... noun: {} and verb: {} --> {}".format(noun, verb, program_res))
        return True
    else:
        print("Nope... noun: {} and verb: {} --> {}".format(noun, verb, program_res))
        return False


operations = {
    1: add,
    2: multiply
}

if __name__ == "__main__":
    request = requests.get("https://adventofcode.com/2019/day/2/input", headers={
        "Cookie": "session=53616c7465645f5f7cd4ecfc55bfaac66acf9112979339a2061e7f0111d741c96bc8bb08fc3ae91d3c9b44a48f9945a6"})

    input = [int(x) for x in request.text.split(',')]

    flag = False
    for x in range(0, 100):
        for y in range(0, 100):
            flag = run(input.copy(), x, y)
            if flag:
                break
        if flag:
            break
