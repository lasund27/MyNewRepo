a = [5, 12, 28, 29, 40, 41, 53, 54, 68, 69, 79, 80, 83, 89, 90, 100]
x = input('Input a number: ')
left = 0
right = len(a) - 1


while left <= right:
    middle = (left + right) // 2
  
    if a[middle] == int(x):  
        print('{:3}는 리스트에서[{:2}]번째에 있습니다.'.format(x, middle))
        break   
    elif a[middle] < int(x):
        left = middle + 1    
    else:
        right = middle - 1

if left > right:
    print('There is not {:3} in this list.'.format(x))
