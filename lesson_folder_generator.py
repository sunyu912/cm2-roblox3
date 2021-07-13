import os
import sys

'''
    usage: lesson_folder_generator.py [lesson_number] [lesson_name] [section_number]
'''

assert len(sys.argv) == 4

lesson_number = int(sys.argv[1])
assert 100 > lesson_number > 0, 'lesson number invalid, expected: 1-99'

lesson_name = sys.argv[2]
assert len(sys.argv[2]) < 20, f'lesson name too long: {len(sys.argv[2])}, expected: 20'

section_number = int(sys.argv[3])

lesson_number_str = str(lesson_number) if lesson_number > 10 else '0'+str(lesson_number)

path = f'./Lesson {lesson_number_str} {lesson_name}'

try:
    os.makedirs(path)
except OSError:
    print("Creation of the directory %s filed" % path)
else:
    print ("Successfully created the directory %s " % path)

##
for s in range(section_number):
    print (s+1)
    fp1 = open(f'{path}/L{lesson_number}-{s+1}.md','w+')
    fp1.close()
    fp2 = open(f'{path}/L{lesson_number}-{s + 1} Exercise.md', 'w+')
    fp2.close()


##
for cat in ['Project','Summary','Overview']:
    fp = open(f'{path}/L{lesson_number} {cat}.md','w+')
    fp.close()