class Password:
    def __init__(self, range_start: int, range_stop: int):
        self.range_start = range_start
        self.range_stop = range_stop

    def following_digits_are_increasing(self, digit_one: int, digit_two: int):
        # print("1: {} , 2: {}".format(digit_one, digit_two))
        return digit_one > digit_two

    def following_digits_are_equals(self, digit_one: int, digit_two: int):
        return digit_one == digit_two

    def get_amount_of_possible_passwords(self):
        cpt = 0
        for combination in range(self.range_start, self.range_stop):
            combination_as_string = str(combination)
            # print("Checking password {}".format(combination_as_string))
            is_possible_code = True
            has_two_equals_adjacent_digits = False
            for i in range(5, 0, -1):
                if self.following_digits_are_increasing(combination_as_string[i], combination_as_string[i-1]):
                    pass
                elif self.following_digits_are_equals(combination_as_string[i], combination_as_string[i-1]):
                    has_two_equals_adjacent_digits = True
                    pass
                else:
                    is_possible_code = False
                    break

            if is_possible_code and has_two_equals_adjacent_digits:
                cpt += 1
        return cpt


if __name__ == "__main__":
    password = Password(136760, 595730)
    # password = Password(111111, 111112)
    possible_password = password.get_amount_of_possible_passwords()
    print("There {} {} combination{} possible".format(
        "is" if possible_password == 1 else "are", possible_password, "s" if possible_password > 1 else ""))
