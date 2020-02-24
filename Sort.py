class SmartSort:

#not perfectly written, quick mockup

    def __init__(self):
        self.maxV = -float('inf')
        self.minV = float('inf')
        self.size = 0
        self.array = [] #this would theoretically represent a map of (IntegerKey -> AnyType)

    def insert(self, x): #to insert into the array
        self.array.append(x)
        self.size += 1
        self.array.sort()


        #a good searching function for large data maps with distinct keys
        """
        This works well on maps with distinct keys
        performs well (better than binary search)
        unless the distribution is heavily left skewed
        """
    def smartSearch(self, val):
        endIndex = len(self.array)
        startIndex = 0
        if self.size == 0 or (endIndex - startIndex) == 0:
            print "Error: start index: ", startIndex, " end index: ", endIndex
            return -1, -1, -1#basic error handling
        pivotPercent = float(val)/(self.array[endIndex - 1] - self.array[startIndex]) #calculate the percentile in the range
        print "pivot percent, ",pivotPercent
        #(endIndex - startIndex) is # of elements in our working range
        pivotIndex = int(pivotPercent*((endIndex) - startIndex))
        pivotVal = self.array[pivotIndex]
        if pivotVal > val:
            #new range becomes start index to pivot index as the pivot is greater than our val
            return self.smartSearchRec(val, startIndex, pivotIndex, 1)
        if pivotVal < val:
            #val in right subsection of array
            return self.smartSearchRec(val, pivotIndex, endIndex, 1)
        return pivotVal, pivotIndex, 1

    def smartSearchRec(self, val, startIndex, endIndex, iterations):
        if self.size == 1: #even if the val isnt in the array we need to return
            return startIndex, endIndex, self.array[startIndex]
        if self.size == 0 or (endIndex - startIndex) == 0:
            return #basic error handling
        pivotPercent = val/(self.array[endIndex - 1] - self.array[startIndex]) #calculate the percentile in the range
        #(endIndex - startIndex) is # of elements in our working range
        pivotIndex = int(pivotPercent*((endIndex) - startIndex))
        pivotVal = self.array[pivotIndex]
        print "iteration: ", iterations, ", pivot index: ", pivotIndex
        if pivotVal > val:
            #new range becomes start index to pivot index as the pivot is greater than our val
            return self.smartSearchRec(val, startIndex, pivotIndex, iterations + 1)
        if pivotVal < val:
            #val in right subsection of array
            return self.smartSearchRec(val, pivotIndex, endIndex, iterations + 1)
        return pivotVal, pivotIndex, iterations


if __name__ == '__main__':
    sort = SmartSort()
    for v in range(1, 50):
        if v%2 is 0 or v % 3 is 0:
            sort.insert(v)

    print "array ", sort.array
    value, index, iterations = sort.smartSearch(3)
    print "val: ", value, ", index: ", index,", iterations: ", iterations
