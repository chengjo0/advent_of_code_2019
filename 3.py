import requests

if __name__ == "__main__":
    request = requests.get("https://adventofcode.com/2019/day/2/input", headers={
        "Cookie": "session=53616c7465645f5f7cd4ecfc55bfaac66acf9112979339a2061e7f0111d741c96bc8bb08fc3ae91d3c9b44a48f9945a6"})
