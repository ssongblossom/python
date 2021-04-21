while True:
    inputStr = input("문자열을 입력하시오: ")
    if inputStr == "end" :
        break

    strLen = len(inputStr)
    for index in range(0,strLen):
        print(inputStr[strLen-index-1], end = "")
    
    print(" ")