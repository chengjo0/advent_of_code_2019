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

    # wire_1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(','))
    # wire_2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83".split(','))

    # wire_1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(','))
    # wire_2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(','))

    wire_1 = Wire(input[0].split(','))
    wire_2 = Wire(input[1].split(','))

    wire_1_positions = wire_1.get_positions()
    wire_2_positions = wire_2.get_positions()

    common_positions = []
    least_steps_taken = 10000000000000000000
    flag = False
    # print(len(wire_1_positions))
    # print(len(wire_2_positions))
    lists = (wire_1_positions, wire_2_positions) if len(wire_1_positions) <= len(
        wire_2_positions) else (wire_2_positions, wire_1_positions)
    for j, p1 in enumerate(lists[0], 1):
        for k, p2 in enumerate(lists[1], 1):
            if p1 == p2:
                common_positions.append(p2)
                least_steps_taken = min(least_steps_taken, j + k)
                flag = True
                print("Steps taken to reach intersection: {}".format(j + k))

        #     if flag:
        #         break
        # if flag:
        #     break

    if len(common_positions) > 0:
        closest_position = abs(
            common_positions[0][0]) + abs(common_positions[0][1])
        for common_position in range(1, len(common_positions)):
            closest_position = min(closest_position, abs(
                common_positions[common_position][0]) + abs(common_positions[common_position][1]))

        print("""
Result:
--> Closest position: {}
--> Least steps taken to reach intersetion: {} steps
        """.format(closest_position, least_steps_taken))
        # print("Closest position: {}".format(closest_position))
        # print("Least steps taken to reach intersetion: {} steps".format(
        # least_steps_taken))
    else:
        print("No common position...")
