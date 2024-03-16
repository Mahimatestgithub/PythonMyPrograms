#Sets are unordered and have no duplicates 

courses = {'coa','os','dsa','dbms'}   #Order changes each time
print(courses)
print('coa' in courses)

cs_courses = {'coa','os','dsa','dbms'}
ec_courses = {'coa','adc','dsa','signals'}
print(cs_courses.intersection(ec_courses))
print(cs_courses.difference(ec_courses))

print(ec_courses.difference(cs_courses))

print(cs_courses.union(ec_courses))


