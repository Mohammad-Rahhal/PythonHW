def sort_list(myList):
     n = len(myList)
     for i in range(n):
             for j in range(n-i-1):
                     if myList[j] > myList[j+1]:
                             temp = myList[j]
                             myList[j] = myList[j+1]
                             myList[j+1] = temp
     print(myList)

