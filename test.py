def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"File missing: {e}")

readFile("files.py")