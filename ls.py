first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
all = first_strings + second_strings
first_result = [len(i)  for i in first_strings if len(i) >=5]
second_result = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x:len(x) for x in all if len(x)%2==0}
print(first_result)
print(second_result)
print(third_result)