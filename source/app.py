import sys

def main(argv) -> None:
    if len(argv) > 1:
        print(f"Hello {argv[1]}")
    else:
        print("Usage: python hello.py [arg0]")


if __name__ == "__main__":
    main(sys.argv[1:])

