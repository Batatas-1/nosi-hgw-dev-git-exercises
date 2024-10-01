import sys

def greet(name) -> None:
    print(f'Hello {name}!')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <name>")
    else:
        name = sys.argv[1]
        greet(name)
