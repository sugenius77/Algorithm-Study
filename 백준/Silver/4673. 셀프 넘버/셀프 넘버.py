array = []
  
for i in range(1,10000):
  i = str(i)
  if len(i) == 1:
    array.append(eval(f'0+{i}+{i}'))
  if len(i) == 2:
    array.append(eval(f'{i[0]}+{i[1]}+{i}'))
  if len(i) == 3:
    array.append(eval(f'{i[0]}+{i[1]}+{i[2]}+{i}'))
  if len(i) == 4:
    array.append(eval(f'{i[0]}+{i[1]}+{i[2]}++{i[3]}+{i}'))

for i in range(1,10000):
  if i not in array:
    print(i)