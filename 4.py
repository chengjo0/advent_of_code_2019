import re


class Password:
    def __init__(self, range_start: int, range_stop: int):
        self.range_start = range_start
        self.range_stop = range_stop

    def following_digits_are_increasing(self, digit_one: chr, digit_two: chr):
        return digit_one > digit_two

    def following_digits_are_equals(self, digit_one: chr, digit_two: chr):
        return digit_one == digit_two

    def following_digits_are_part_of_larger_group(self, pos: int, digit: chr, combination_as_string: str):
        nb_of_similar_digits = 2
        for i in range(pos-2, -1, -1):
            if combination_as_string[i] == digit:
                nb_of_similar_digits += 1
            else:
                break

        if pos + 1 < len(combination_as_string):
            for j in range(pos+1, len(combination_as_string)):
                if combination_as_string[j] == digit:
                    nb_of_similar_digits += 1
                else:
                    break

        # print("Nb of similar digits: {}".format(nb_of_similar_digits))
        return False if nb_of_similar_digits % 2 == 0 else True

    def check_larger_group(self, combination_as_string):
        matches = re.findall(
            '22+|33+|44+|55+|66+|77+|88+|99+', combination_as_string)
        # print(matches)
        if matches and min([len(match) for match in matches]) == 2:
            return True
        else:
            return False

    def get_amount_of_possible_passwords(self):
        cpt = 0
        for combination in range(self.range_start, self.range_stop):
            combination_as_string = str(combination)
            # print("Checking password {}".format(combination_as_string))
            is_possible_code = True
            has_two_equals_adjacent_digits = False
            for i in range(5, 0, -1):
                # print("1: {} , 2: {}".format(
                #     combination_as_string[i], combination_as_string[i-1]))
                if self.following_digits_are_increasing(combination_as_string[i], combination_as_string[i-1]):
                    pass
                elif self.following_digits_are_equals(combination_as_string[i], combination_as_string[i-1]):
                    has_two_equals_adjacent_digits = True
                    if self.following_digits_are_part_of_larger_group(i, combination_as_string[i], combination_as_string):
                        is_possible_code = False
                        break
                    pass
                else:
                    is_possible_code = False
                    break

            # if not self.check_larger_group(combination_as_string):
            #     is_possible_code = False

            if is_possible_code and has_two_equals_adjacent_digits:
                cpt += 1
        return cpt


if __name__ == "__main__":
    password = Password(136760, 595730)
    # password = Password(123444, 123444+1)
    possible_password = password.get_amount_of_possible_passwords()
    print("There {} {} combination{} possible".format(
        "is" if possible_password <= 1 else "are", possible_password, "s" if possible_password > 1 else ""))
    assert possible_password == 1264, "Should be equal to 1264"
