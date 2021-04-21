foods = {"떡볶이":"오뎅", 
            "짜장면":"단무지",
            "라면":"김치",
            "피자":"피클",
            "맥주":"땅콩",
            "치킨":"치킨무",
            "삼겹살":"상추" }


while True :
    myFood = input("음식을 입력하시오:")
    if myFood in foods:
        print("%s : %s"% (myFood, foods.get(myFood)))
    elif myFood == "끝":
        break
    else :
        print("없음") 
