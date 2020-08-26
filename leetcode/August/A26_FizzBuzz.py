class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            Three = False
            Five = False
            if i%3 == 0:
                Three = True
            if i%5 == 0:
                Five = True
            if Three and Five:
                res.append("FizzBuzz")
            elif Three:
                res.append("Fizz")
            elif Five:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res 

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            word = ""
            if i%3 == 0:
                word += "Fizz"
            if i%5 == 0:
                word += "Buzz"
            if word == "":
                word = str(i)
            res.append(word)
        return res        