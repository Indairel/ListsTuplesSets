
courses = ['History', 'Geography', 'Physics', 'Math']

courses_2 = ['Chemistry', 'Biology']
# courses.append('Art')

# courses.insert(0, 'Art')

# courses.extend(courses_2)
#
# courses.remove('Math')
#
# popped = courses.pop()
#
# print(popped)
# print(courses[-1])
#
# print(courses[0:2])

# courses.sort(reverse=True)
#
# print(courses.index('History'))
# print(courses)
#
# for index, course in enumerate(courses, start=1):
#     print(index, course)

course_str = ' - '.join(courses)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)

