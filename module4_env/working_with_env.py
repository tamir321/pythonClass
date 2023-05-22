import sys

#
print("version - ",sys.version)
print("platform - ",sys.platform)


def main(args):
    # Check the number of arguments
    if len(args) < 3:
        print(f"Usage: python expect  3 args got {len(args)}")
        return

    # Extract the arguments
    arg1 = args[1]
    arg2 = args[2]

    # Process the arguments
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv[:]):
        if i == 0:
            print(f"Script name: {sys.argv[0]}")
        else:
            print(f"{i}. argument is: { sys.argv[i]}")

    # Pass the command-line arguments (excluding the script name) to the main function
    main(sys.argv[:])