'''
상하좌우 이동
왼손: 1,4,7
오른손: 3,6,9
가까운: 2,5,8,0
거리가 같다면 왼손잡이 , 오른손 잡이
'''
def solution(numbers, hand):
    answer = ''
    left_now = [3,0]
    right_now = [3,2]
    keypad ={1:[0,0], 2:[0,1], 3:[0,2],
             4:[1,0], 5:[1,1], 6:[1,2],
             7:[2,0], 8:[2,1], 9:[2,2],
             '*':[3,0], 0:[3,1], '#':[3,2]}
    for i in numbers:
        if i in [1,4,7]:
            answer = answer + 'L'
            left_now = keypad[i]
        if i in [3,6,9]:
            answer = answer + 'R'
            right_now = keypad[i]
        if i in [2,5,8,0]:    
            left = abs(keypad[i][0] - left_now[0]) + abs(keypad[i][1] - left_now[1])
            right = abs(keypad[i][0] - right_now[0]) + abs(keypad[i][1] - right_now[1])
            if left < right:
                left_now = keypad[i]
                answer = answer + 'L'
            elif left > right:
                right_now = keypad[i]
                answer = answer + 'R'
            elif left == right:
                if hand == 'right':
                    right_now = keypad[i]
                    answer = answer + 'R'
                else:
                    left_now = keypad[i]
                    answer = answer + 'L'
    
    return answer