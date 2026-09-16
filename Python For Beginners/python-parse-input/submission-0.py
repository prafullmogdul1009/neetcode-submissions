from typing import List

def read_integers() -> List[int]:
    a= input()
    b = (a.split(","))
    b = [int(x) for x in a.split(",")]

    return b

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
