"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
s={"studenrt_name":"kalyan","age":23,"roll_no":27,"class":10,"section":'D',"percentage":83,"college_name":"alibaba"}
print(s["percentage"])


"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""

L={"names":["pavan","kalyan","kalki"],
   "ages":[22,23,24],
   "roll_nos":[1,2,3],
   "classes":[10,11,12],
   "sections":('a','b','c'),
   "percentages":[56,65,76],
   "university_name":["ABC","BCA","CBA"]
   }
print(L["classes"][-1])


"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
L={"employees":{"emp1":{"name":"pavan","salary":28000,"Designation":"developer"},
                "emp2":{"name":"kalyan","salary":32000,"Designation":"ui/ux designer"},
                "emp3":{"name":"sai","salary":25000,"Designation":"tester"},
                "emp4":{"name":"vasu","salary":33000,"Designation":"qa analyast"}}}
print(L["employees"]["emp3"]["Designation"])
