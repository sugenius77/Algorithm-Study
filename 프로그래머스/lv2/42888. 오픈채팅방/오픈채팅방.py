def solution(record):
    answer = []
    array = []
    dict = {}
    for i in record:
        user = i.split()        
        if user[0] == "Enter":
            array.append([user[0],user[1]])
            dict[user[1]] = user[2]
        elif user[0] == "Leave":
            array.append([user[0],user[1]])
        elif user[0] == "Change":
            dict[user[1]] = user[2]
    
    for i in array:
        if i[0] == "Enter":
            answer.append(dict[i[1]] + "님이 들어왔습니다.")
        if i[0] == "Leave":
            answer.append(dict[i[1]] + "님이 나갔습니다.")
    
    return answer