def main():
    import numpy as np
    size = 12

    select = input("multiplication table size > ")
    try:
        size = int(select)
    except ValueError:
        print("Invalid Selection, Defaulting to 12")
        size = 12

    final = np.zeros((size, size))
    for i in range(size):
        for k in range(size):
            final[i, k] = ((i+1) * (k+1))
    return final.astype(int)


if __name__ == "__main__":
    main()
