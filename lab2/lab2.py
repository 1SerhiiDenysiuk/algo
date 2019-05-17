class Calendar:
    def __init__(self, array):
        self.array = array
    def insertion_sort(self, array):
        for index in range(1, len(array)):
            value = array[index]
            i = index - 1
            while i >= 0:
                if value < array[i]:
                    array[i + 1] = array[i]
                    array[i] = value
                    i = i - 1
                else:
                    break
        return array

    def change_calendar(self):
        self.result = []
        i = 0
        while i < len(self.array):
            start = self.array[i][0]
            end = self.array[i][1]
            k = i + 1
            flag = True
            while k < len(self.array) and flag == True:
                if (self.array[i][1] < self.array[k][0]):
                    i = k - 1
                    flag = False
                else:
                    if (end < self.array[k][1]):
                        end = self.array[k][1]
                    if (k == len(self.array) - 1):
                        i = k
                        flag = False
                    else:
                        k += 1
            self.result.append((start, end))
            i += 1

if __name__ == '__main__':
    array = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    test = Calendar(array)
    test.array = test.insertion_sort(test.array)
    test.change_calendar()
    print(test.result)