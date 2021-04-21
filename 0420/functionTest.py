import random

def getNum():
    lottoSet = set()  #중복을 제거하기 위해서 set 생성
    while True:
        num = random.randrange(1,45)   #1-45까지 랜덤 숫자
        lottoSet.add(num)
        if len(lottoSet)==6:            #중복이 제외 6개라면, 반복문 종료
            break
    return lottoSet


lottoList = list(getNum())         #set를 list로 변환
lottoList.sort()                   #정렬
print(lottoList)

