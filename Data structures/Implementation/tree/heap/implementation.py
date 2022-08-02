class minheap:
    def __init__(self):
        self.heap_list = []
        self.heap_curr_size = 0

    def bubbleup(self,i):
        while (i-1) // 2 >= 0:
            if self.heap_list[i] < self.heap_list[(i-1)//2]:
                #swap
                (self.heap_list[i] , self.heap_list[(i-1)//2]) = (self.heap_list[(i-1)//2], self.heap_list[i])
            i = (i-1) // 2

    def insert(self,val):

        #add
        self.heap_list.append(val)

        self.heap_curr_size += 1

        #bubbleup the last element
        self.bubbleup(self.heap_curr_size-1)


    def bubbledown(self,i):
        while (i*2 + 1) <= self.heap_curr_size-1:
            mc = self.min_child_idx(i)

            if self.heap_list[i] > self.heap_list[mc]:
                (self.heap_list[i], self.heap_list[mc]) = (self.heap_list[mc], self.heap_list[i])
            i = mc

    def min_child_idx(self,i):
        if (i*2 + 2) > self.heap_curr_size-1:
            return i*2 + 1
        else:
            if self.heap_list[i*2+1] > self.heap_list[i*2+2]:
                return i*2+2
            elif self.heap_list[i*2+1] < self.heap_list[i*2+2]:
                return i*2+1

    def deletemin(self):
        if self.heap_curr_size == 0:
            return "empty heap"
        
        root = self.heap_list[0]

        self.heap_list[0] = self.heap_list[self.heap_curr_size-1]

        self.heap_list.pop()

        self.heap_curr_size -= 1

        self.bubbledown(0)

        return root

    def peek(self):
        if self.heap_curr_size == 0:
            return "empty heap"
        
        return self.heap_list[0]


my_minheap = minheap()
arr = [7,10,4,3,20,15]

for i in arr:
    my_minheap.insert(i)

#print(my_minheap.peek())
print(my_minheap.heap_list)
#print(my_minheap.heap_curr_size)
print(my_minheap.deletemin())
print(my_minheap.heap_list)


    



