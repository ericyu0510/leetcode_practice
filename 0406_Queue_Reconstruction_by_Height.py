class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        vacancy = [i for i in range(len(people))]
        ans = [[0,0] for i in range(len(people))]
        people.sort()
        tmp = []
        for i in range(len(people)): # peo = [hi, ki]
            count = 0
            if i and people[i][0] > people[i-1][0]:
                for index in tmp:
                    del vacancy[index-count]
                    count += 1
                tmp = []
            ans[vacancy[people[i][1]]] = people[i]
            tmp.append(people[i][1])
        return ans
