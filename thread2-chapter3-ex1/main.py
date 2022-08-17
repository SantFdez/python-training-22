import array


def main():
    arrayEmpty = [None]
    if (arrayEmpty):
        print("Truthy")
    else:
        print("Falsy")
    print(my_sum(1, 2, 3))
    my_list = [1, 2, 3, 4, 5, 6]

    *a, b, c = my_list

    print(a)
    print(b)
    print(c)
    
    with File('demo.txt', 'w') as opened_file:
        print("demito")
        opened_file.undefined_function()
   

class File(object):
    def __init__(self, file_name, method):
        print("Constructing object")
        self.file_obj = open(file_name, method)
    def __enter__(self):
        print("Created object")
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

def reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return(reversed_sentence)

def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

if __name__ == "__main__":
    main()