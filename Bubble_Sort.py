class Bubble_Sort:
    def bubbleSort(self,array:list[int]):
        length = len(array)
        for i in range(0,length-1):
            for j in range(length-i-1):
                if array[j] >array[j+1]:
                    array[j] , array[j+1] = array[j+1],array[j]
        return array
if __name__ == '__main__':
    obj = Bubble_Sort()
    arr = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19, 2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    result = obj.bubbleSort(arr)
    print(result)