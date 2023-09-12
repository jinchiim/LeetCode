class Solution(object):
    def minimumSum(self, n, k):
        numList = [i for i in range(1, k//2+1)] # 짝수, 홀수 일 경우의 반 
        if len(numList) == n:
            return(sum(numList)) # 길이가 같을 경우 그대로 return
        else:
            last = abs(len(numList) - n) # 부족한 길이의 절댓값
            if len(numList) > n: # 길이가 더 길 경우
                return(sum(numList[:len(numList)-last]))
            else: # 길이가 부족한 경우
                plusNum = sum([i for i in range(k, k+last)]) # 부족한 만큼 붙인 값 더하기
                return(sum(numList) + plusNum)