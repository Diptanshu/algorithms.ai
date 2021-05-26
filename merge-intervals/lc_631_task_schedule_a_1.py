class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import heapq
        from collections import defaultdict
        proc = []
        freq_map = defaultdict()
        for task in tasks:
            freq_map[task] = freq_map.get(task,0)+1
        
        for task, freq in freq_map.items():
            proc.append((-freq, task))
        heapq.heapify(proc)
        task_list = []
        while proc:
            temp = n
            temp_list = []
            while(n >= 0):
                if proc:
                    freq, task  = heapq.heappop(proc)
                    freq_map[task] = freq_map.get(task)-1 
                    if freq_map.get(task) == 0:
                        freq_map.pop(task)
                    temp_list.append(task)
                else:
                    if freq_map:
                        temp_list.append("idle")          
                n -= 1
            for task in temp_list:
                if task in freq_map:
                    heapq.heappush(proc, (-(freq_map[task]),task))
            task_list += temp_list
            n = temp
        return len(task_list)