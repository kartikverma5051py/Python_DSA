class Sorting:
    def selection_sort(self,array:list[int]):
        length = len(array)
        for i in range(length-1):
            minIndex = i
            for j in range(i+1 , length):
                if array[j]<array[minIndex]:
                    minIndex = j
            if array[i] != array[minIndex]:
                array[i],array[minIndex] = array[minIndex],array[i]
                print(f" Iteration number {i}")
                print(array,"\n")
        return array
if __name__ == '__main__':
    obj = Sorting()
    arr = [0,0,0,0,0,2,1,5,2,4,72,5]
    # arr.sort()
    # print(arr)
    result = obj.selection_sort(arr)
    print(result)

