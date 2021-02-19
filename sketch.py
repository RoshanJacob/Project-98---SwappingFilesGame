def swapFiles():
    swapFileNameFirst = input("Write the 1st file to swap! : ")
    swapFileNameSecond = input("Write the 2nd file to swap! : ")

    file = open(swapFileNameFirst, 'r')
    readFile1 = file.read()

    file2 = open(swapFileNameSecond, 'r')
    readFile2 = file2.read()

    file = open(swapFileNameFirst, 'w')
    file2 = open(swapFileNameSecond, 'w')

    file.write(readFile2)
    file2.write(readFile1)

    # print(readFile1)
    # print(readFile2)
    print("The files have successfully been swapped!")


swapFiles()