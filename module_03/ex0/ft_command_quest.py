from sys import argv

if __name__ == "__main__":
    print("=== Command Quest ===")
    argc = len(argv)
    print(f"Program name: {argv[0][2:]}")
    if argc < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1
    print(f"Total arguments: {argc}")
