# def get_digit(number, n):
#     return number // 10**n % 10

# # 0th index
# get_digit(987654321, 0)
# # 1


# numbers = [4, 8, 9, 0]
# print(sorted(numbers))

# numbers_tuple = (6, 9, 3, 1)
# print(sorted(numbers_tuple))

# string_value = 'I like to sort'
# print(sorted(string_value))

# string_value = 'I like to sort'
# print( ' '.join(sorted(string_value.split(' ') )) )

# names = ['harry', 'Suzz', 'al', 'Mark']
# print(sorted(names, key = lambda x: x[-1]))

# names = ['harry', 'Suzz', 'al', 'Mark']
# print(sorted(names, key = lambda x: x[-1], reverse=True))

# # case-insensitive sorting 
# print(sorted("This is a test string from Andrew".split(), key=str.lower)) 
        
# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# print(sorted(student_tuples, key=lambda student: student[2]))

# class Student:
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#     def __repr__(self):
#         return repr((self.name, self.grade, self.age))

# student_objects = [
#     Student('tunde', 'Z', 10),
#     Student('john',  'A', 15),
#     Student('jane',  'B', 12),
#     Student('dave',  'B', 10),   
# ]
# print(sorted(student_objects, key=lambda student: student.age))


# from operator import itemgetter, attrgetter

# print(sorted(student_tuples, key=itemgetter(2)))
# print(sorted(student_objects, key=attrgetter('grade', 'age'))) #sort by grade, then age i.e if grade is equal, then sort by age
# print(sorted(student_tuples, key=itemgetter(1,2)))


# def sortSentence(s: str) -> str:
#     count_array = [0]  * len(s.split(' '))
#     print(len(s.split(' ')))
#     for word in s.split(' '):
#         print(word, int(word[-1])-1)
#         count_array[int(word[-1])-1] = word[:-1]
#     print(count_array)

# sortSentence("lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1")

# aResult = [[0 for j in range(0, 4)] for i in range(0, 4)]
# print(aResult)

print(bin(157))
# print(bin(157 >> 1))
print(bin(157 << 1))