def solution(numbers, hand):
    #왼손인지 오른손인지 저장하기
    #거리가 눌린 번호 저장하기
    if(hand.startswith('r')):
        hand = "R"
    else:
        hand = "L"
    
    total=[]
    num = ["" for i in range(10)]
    for i in numbers:
        if(i in [1,4,7]):
            if("L" in num): num[num.index("L")] = ""
            num[i] = "L"
            total.append(num[i])
        elif(i in [3,6,9]):
            if("R" in num): num[num.index("R")] = ""
            num[i] = "R"
            total.append(num[i])
        else:
            if(num[i-1] == "L" or num[i+1] == "R"):
                if(hand in num): num[num.index(hand)] = ""
                num[i] = hand
                total.append(num[i])
            else:
                a = num.index("L")
                b = num.index("R")
                if(abs(a-i) < abs(b-i)):
                    if("R" in num): num[num.index("R")] = ""
                    num[i] = "R"
                    total.append(num[i])
                else:
                    if("L" in num): num[num.index("L")] = ""
                    num[i] = "L"
                    total.append(num[i])
                
        print(num)