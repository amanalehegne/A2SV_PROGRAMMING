class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = []
        idx = 0
        # Becuase we need the index incase we have two process with same finishing time
        for enqueue, process in tasks:
            arr.append([enqueue, process, idx])
            idx += 1
        
        # Then we sort them by their start (enqueue) time as it is the first to arrive that will be executed initally
        arr.sort()
        heap = []
        
        # We need to keep track of how many unit of time have passed and also the taks to be added to the priority queue (if their enqueue time is smaller than the current time | they have been successfuly enqueued)
        idx = 0
        time = arr[0][0]
        size = len(arr)
        res = []
        
        # We need to check both the heap (the priority queue) and the array(tasks) becuase:
        # If our heap is empty but not the tasks array it means, there are tasks remaining that are idely by
        # If our tasks finished but the heap still has elements, it means there are no taks waiting to get enqueued but there are tasks in our processor waiting for their time
        while heap or idx < size:
            # There is a possiblity in a given time multiple taks have to be added to the processor, thus we use a while loop, and since the tasks array is sorted we get the tasks inorder of their enquque time
            while idx < size and time >= arr[idx][0]:
                # Here we only need the process time and the index
                task = [arr[idx][1], arr[idx][-1]]
                heapq.heappush(heap, task)
                idx += 1
            
            # If we have no element in our priority queue, it means it is idel, thus we have to move the time
            # We can increment it by one - which is infficent
            # We can make it to the time of the last process
            if not heap:
                time = arr[idx][0]
            else:
                finished = heapq.heappop(heap)
                time += finished[0]
                res.append(finished[-1])
        
        return res