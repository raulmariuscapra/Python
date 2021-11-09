a_list = [1,2,3,4,5,6,7,7,8,9]
for i in range(0,len(a_list)):
    for j in range(i+1,len(a_list)):
        if(a_list[i]==a_list[j]):
            print("Duplicate is " ,j)
            break
        