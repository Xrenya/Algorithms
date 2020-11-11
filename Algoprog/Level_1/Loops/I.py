try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input()))
except:
    res = 0
    for i in my_list:
        if i == 0:
            print(res)
        res += i
