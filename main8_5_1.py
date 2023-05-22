emp = []

def add_emp(emp_num: int ,**kwargs):
    _emp = {}
    _emp["emp_num"]=emp_num
    print(kwargs)
    f_name=kwargs.get("first_name")
    l_name= kwargs.get("first_name")

    emp.append(_emp)

add_emp(1,first_name="tamir",last_name="reiss",age=89)
add_emp(2,first_name="tamr",last_name="rei3s",age=89)
add_emp(3,stam="tami3r",Last_name="reis4s",age=89)
add_emp(4,First_name="tamir1",last_name="reis23s",age=89)

for i in emp:
    print(i)
