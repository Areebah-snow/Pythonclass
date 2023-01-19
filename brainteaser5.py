x = 500
print(type(x))
<class 'int'>
y = "apple"
print(type(y))
<class 'str'>
z = 3.142
print(type(z))
<class 'float'>
isTrue = True
print(type(isTrue))
<class 'bool'>
x = 100
print(isinstance(x,int))
True
print(isinstance(y,float))
False
y = 100.9
print(isinstance(y,float))
True
z = 1.002
print(isinstance(z,float))
True
z = 1.003
print(isinstance(z,float))
True
print(isinstance(y,int))
False


studentID = 12344
print(isinstance(studentID,int))
True
classID = "cake"
print(isinstance(classID,str))
True
school_id = 1.004
print(isinstance(school_id,float))
True
work_id = True
print(isinstance(work_id,bool))
True
couontry_id = 3.4
print(isinstance(couontry_id,int))
False
food_id = "ice-cream"
print(isinstance(food_id,str))
True
