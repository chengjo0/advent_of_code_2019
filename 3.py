import requests


class Wire:
    def __init__(self, steps):
        self.steps = steps
        self.current_position = (0, 0)

    def inc_x_axis(self, inc: int):
        (x, y) = self.current_position
        self.current_position = (x + inc, y)

    def inc_y_axis(self, inc: int):
        (x, y) = self.current_position
        self.current_position = (x, y + inc)

    def dec_x_axis(self, inc: int):
        (x, y) = self.current_position
        self.current_position = (x - inc, y)

    def dec_y_axis(self, inc: int):
        (x, y) = self.current_position
        self.current_position = (x, y - inc)

    operations = {
        "U": inc_y_axis,
        "D": dec_y_axis,
        "L": inc_x_axis,
        "R": dec_x_axis
    }

    def get_position(self, step: str):
        positions = []
        direction = step[0]
        steps = int(step[1:])
        operation = self.operations[direction]
        while steps > 0:
            operation(self, 1)
            positions.append(self.current_position)
            steps -= 1
        return positions

    def get_positions(self):
        positions: list((int, int)) = []
        for x in self.steps:
            positions += self.get_position(x)
        # print(positions)
        return positions


if __name__ == "__main__":
    request = requests.get("https://adventofcode.com/2019/day/3/input", headers={
        "Cookie": "session=53616c7465645f5f7cd4ecfc55bfaac66acf9112979339a2061e7f0111d741c96bc8bb08fc3ae91d3c9b44a48f9945a6"})

    input = request.text.splitlines()
    # wire_1 = Wire("R8,U5,L5,D3".split(','))
    # wire_2 = Wire("U7,R6,D4,L4".split(','))
    wire_1 = Wire(input[0].split(','))
    wire_2 = Wire(input[1].split(','))

    wire_1_positions = wire_1.get_positions()
    wire_2_positions = wire_2.get_positions()

    common_positions = []
    print(len(wire_1_positions))
    print(len(wire_2_positions))
    index = 0
    lists = (wire_1_positions, wire_2_positions) if len(wire_1_positions) <= len(
        wire_2_positions) else (wire_2_positions, wire_1_positions)
    for p1 in lists[0]:
        print(index)
        for p2 in lists[1]:
            if p1 == p2:
                common_positions.append(p2)
        index += 1

    if len(common_positions) > 0:
        closest_position = abs(
            common_positions[0][0]) + abs(common_positions[0][1])
        for common_position in range(1, len(common_positions)):
            closest_position = min(closest_position, abs(
                common_positions[common_position][0]) + abs(common_positions[common_position][1]))

        print(closest_position)
    else:
        print("No common position...")
