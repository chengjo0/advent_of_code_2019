import requests


def getFuel(mass: int):
    print("mass: {}".format(mass))
    result: int = mass // 3

    print("divided by 3: {}".format(result))
    if result <= 0:
        return 0

    fuelQtty: int = result - 2
    if fuelQtty <= 0:
        return 0

    print("Qtty needed: {}".format(fuelQtty))
    return fuelQtty + getFuel(fuelQtty)


if __name__ == "__main__":
    request = requests.get("https://adventofcode.com/2019/day/1/input", headers={
                           "Cookie": "session=53616c7465645f5f7cd4ecfc55bfaac66acf9112979339a2061e7f0111d741c96bc8bb08fc3ae91d3c9b44a48f9945a6"})

    massList = request.text.splitlines()
    totalFuelNeeded = 0
    for mass in massList:
        print("====================================")
        massAsInt: int = int(mass)
        print(massAsInt)
        fuelForMass: int = getFuel(massAsInt)
        print("total mass: {}".format(fuelForMass))
        totalFuelNeeded = totalFuelNeeded + fuelForMass

    print("Quantity of fuel needed: {}".format(totalFuelNeeded))
