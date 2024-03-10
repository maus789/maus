class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            current_element = self.data[self.index]
            self.index += 1
            return current_element
        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
iterator = ListIterator(my_list)

for item in iterator:
    print(item)



class FilterIterator:
    def __init__(self, data, condition):
        self.data = data
        self.condition = condition
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            current_element = self.data[self.index]
            self.index += 1
            if self.condition(current_element):
                return current_element
        raise StopIteration

def is_even(num):
    return num % 2 == 0

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_filter = FilterIterator(my_list, is_even)

for item in even_filter:
    print(item)



class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]
        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_list)

for item in reverse_iterator:
    print(item)