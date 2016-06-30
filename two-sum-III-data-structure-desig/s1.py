class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.numbers = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.numbers:
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        
        for n  in self.numbers:
            if value - n == n:
                if self.numbers[n] >= 2:
                    return True
                
            elif value - n in self.numbers:
                return True
                
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
