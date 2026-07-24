class Solution:
   
        def isonechange(self,word,target):
            change = 0
            for i in range(len(word)):
                if word[i] != target[i]:
                    change += 1
                if change > 1:
                    return False
            return True
        def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            graph = defaultdict(list)
            start = beginWord
            end = endWord
            graph[start] = []
            graph[end] = []
            i = 0
            visited = set()
            visited.add(start)
        
            # if endWord not in wordList:
            #     return 0
            for w in wordList:

                if w not in visited and self.isonechange(start,w):
                    graph[start].append(w)
                visited.add(w)
            visited = set()
            visited.add(start)
            while i < len(wordList):
                j = 0

                if wordList[i] == end or wordList[i] in visited:
                    i+=1                
                    continue

                if wordList[i] == start:
                    i+=1
                    continue
                while j < len(wordList):
                    if i == j:
                        
                        j += 1
                        continue
                
                    if self.isonechange(wordList[i],wordList[j]) :
                        graph[wordList[i]].append(wordList[j])
        
                    j += 1
                visited.add(wordList[i])
                i += 1
    
            visited = set()
            res = float("inf")
            q = collections.deque([(start,1)])
            visited.add(start)
            while q:
    
                node,length = q.popleft()

            
                
                    
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        
                        if neighbor == end:
                
                            res = min(res,length+1)
                            break
                        visited.add(neighbor)
                    
                        q.append((neighbor,length+1))
            
                        
                        
                        
        
            return 0 if res == float("inf") else res