class Solution(object):
    def letterCombinations(self, digits):
        numDict = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        resultList = []

        for i in range(len(digits)):
            outputList = []
            if resultList == []: # i가 1일 경우
               resultList = numDict[digits[0]]
               continue # 1일 경우 List 추가 후 continue
            for k in resultList:
                    for p in numDict[digits[i]]:
                        outputList.append(k+p) 
            resultList = outputList
        return resultList