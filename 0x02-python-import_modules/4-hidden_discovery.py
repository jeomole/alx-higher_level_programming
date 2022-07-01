#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hiddenlist = dir(hidden_4)

    for i in hiddenlist:
        if i[:2] != "__":
            print(f"{i}")
