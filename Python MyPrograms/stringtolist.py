courses=['coa','os','dsa','dbms']
#course_string =', '.join(courses)
#print(course_string) #join converts string to list
course_string ='-'.join(courses)
new_list =course_string.split(' - ')  # SPLIT we use to convert it again to original string   
print(new_list)