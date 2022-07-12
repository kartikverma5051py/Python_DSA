class Merge_Sort:
    def merge_Sort(self,arr:list[int]):
        length = len(arr)
        if length>1:
            mid =  length//2
            leftList = arr[:mid]
            rightList = arr[mid:]
            self.merge_Sort(leftList)
            self.merge_Sort(rightList)
            i=j=k=0
            while i<len(leftList) and j<len(rightList):
                if leftList[i]<rightList[j]:
                    arr[k] = leftList[i]
                    i+=1
                    k+=1
                else:
                    arr[k] = rightList[j]
                    j+=1
                    k+=1
            while i<len(leftList):
                arr[k]=leftList[i]
                i+=1
                k+=1
            while j<len(rightList):
                arr[k]=rightList[j]
                j+=1
                k+=1
        return arr
if __name__ == '__main__':
    obj = Merge_Sort()
    arr = [9,8,3,45,2,234]

    result = obj.merge_Sort(arr)
    print(result)
