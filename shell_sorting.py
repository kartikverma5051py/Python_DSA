def shellsort(alist):
    gap = len(alist)//2
    while gap>0:
        for index in range(gap,len(alist)):


            current_element = alist[index]


            postion_of_current_element = index


            while postion_of_current_element>=gap and current_element<=alist[postion_of_current_element-gap]:


                alist[postion_of_current_element]=alist[postion_of_current_element-gap]
 



            alist[postion_of_current_element] = current_element
        gap = gap//2
    return  alist
num = [99,101,12,15553,14,17,18,332]
result = shellsort(num)
print(result)
