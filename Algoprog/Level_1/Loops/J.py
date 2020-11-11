try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input()))
except:
    counter = 0
    for i in my_list:
        if i == 0:
            print(counter)
        if i%2 == 0:
            counter += 1
