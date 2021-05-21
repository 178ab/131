import os #导入文件

filename = 's.txt'
def main():
    while(1):
        menu()
        option = input("请选择")
        if option == '1':
            insert()
        elif option == '7':
            show()
        elif option == '2':
            search()
        elif option == '5':
            sort()
        elif option == '4':
            modify()
        elif option == '3':
            delete()
        elif option == '6':
            total()
        else:
            print("您已经退出学生管理系统")
            break
#统计
def total():
    if os.path.exists(filename):
            #打开文件，读取数据
            with open(filename,'r') as file:
                studentList = file.readlines()#字符串
                if studentList:
                    print("一共%d学生"% len(studentList))
                else:
                    print("没有学生信息")          
    else:
        print("未找到文件数据")
        

#排序
def sort():
   student_new = []
   if os.path.exists(filename):
        #打开文件，读取数据
        with open(filename,'r') as file:
            studentList = file.readlines()#字符串
        #将字符串转为dicionay存在列表中
        for list in studentList:
            student_new.append(eval(list))

        #排序
        asc = input("请选择（0升序，1降序）")
        if asc == '0':
            asc = False
        else:
            asc = True
        mode = input("请选择排序方式（1（语文），2（数学），3（英语），4（总成绩））")
        if mode == '1':
            student_new.sort(key=lambda x:float(x['chinese']),reverse = asc)
        elif mode == '2':
            student_new.sort(key=lambda x:float(x['math']),reverse = asc)
        elif mode == '3':
            student_new.sort(key=lambda x:float(x['english']),reverse = asc)
        elif mode == '4':
            student_new.sort(key=lambda x:float(x['chinese'])+float(x['math'])+float(x['english']),reverse = asc)
                
        if student_new:
            printDate(student_new) 
    

#修改学生信息
def modify():
    show()
    studentId = input("输入要修改学生的ID：")
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old = rfile.readlines();
    else:
        return
    with open(filename,'w') as wfile:
        d = {}
        for s in student_old:
            d = dict(eval(s))
            if d['id'] == studentId:#符合修改条件
                #修改信息
                while True:
                     try:   
                        d['name'] = input("pleas input name：")
                        d['chinese'] = float(input('pleas input chinese grade：'))
                        d['math'] = float(input('please input math grade：'))
                        d['english'] = float(input('pleas input english grade：'))
                     except:
                        print("输入无效")       
                     else:
                        break
                wfile.write(str(d) + '\n')
                print("修改成功")
            

            else:      
                #直接修改文件
                wfile.write(str(d) + '\n')
                
    ismore = input("是否继续修改：")     
    if ismore == 'y':
        modify()#嵌套，递归
           
        
#菜单
def menu():
    print("学生信息管理系统")
    print('''
=============菜单=============

   1 录入学生信息
   2 查寻学生信息
   3 删除学生信息
   4 修改学生信息
   5 排序学生信息
   6 统计学生总人数
   7 显示所有学生信息
   8 退出系统

=============菜单=============
    ''')

#录入学生信息 
def insert():
    #用于保存多个学生信息
    studentList = []
    isflag = True
    while isflag:
        id = input("pleas input id:")
        name = input("pleas input name：")
        try:
            chinese = float(input('pleas input chinese grade：'))
            math = float(input('please input math grade：'))
            english = float(input('pleas input english grade：'))
        except:
            print("输入无效")
            continue
        student = {'id':id,'name':name,'chinese':chinese,'math':math,'english':english}
        studentList.append(student)
        ismore = input("是否需要继续添加：")
        if ismore == 'y':
            isflag = True
        else:
            isflag = False


    #保存文件
    student_txt = open(filename,'a')
    #将本次添加的学生信息全部添加到文件中

    for s in studentList:
       #写入一行数据
       student_txt.write(str(s) + '\n')
    #关闭文件对象
    student_txt.close()

    
#删除学生信息
def delete():
    isflag = 'Ture'
    while isflag == 'Ture':
        studentId = input("请输入要删除学生的信息")
        if studentId != '':
            #读取所有学生信息
            if os.path.exists(filename):
                with open(filename) as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            isDel = 'False'
            if student_old:
                with open(filename,'w') as wfile:
                    d = {}
                    for s in student_old:
                        d = dict(eval(s))#得到列表中的学生字典
                        if d['id'] != studentId:#只有Id不相等的Id才会写入
                            wfile.write(str(d) + '\n')
                        else:
                            isDel = 'Ture'
                    if isDel:
                        print("该学生已被删除")
                    else:
                        print("该学生没被删除")
            else:
                print("无该学生信息")
                continue
            show()#显示学生是否被删除
            ismore = input("是否继续删除：")
            if ismore == 'y':
                isflag = 'Ture'
            else:
                isflag = 'Flase'


#查询学生信息
def show():
    student_new = []
    if os.path.exists(filename):
        #打开文件，读取数据
        with open(filename,'r') as file:
            studentList = file.readlines()#字符串
        #将字符串转为dicionay存在列表中
        for list in studentList:
            student_new.append(eval(list))
        if student_new:
            printDate(student_new)


            
#提取相同的代码
#显示数据
def printDate(student_new):
    print("ID\tname\tchinese\tmath\tenglish\tall")
            #遍历改列表
    for info in student_new:
        print(info.get("id")+'\t'+
                      info.get("name")+'\t'+
                      str(info.get("chinese"))+'\t'+
                      str(info.get("math"))+'\t'+
                      str(info.get("english"))+'\t'+
                      str(float(info.get("chinese"))+float(info.get("math"))+float(info.get("english"))))
   
                
#查找学生信息
def search():
    isFlag = True
    student_new = []
    while isFlag:
        id = ''
        name = ''
        #请用户输入
        mode = input("按id查询请输1；按姓名查询请输2；")
        if mode == '1':
            id = input("请输入学生id:")
           
        elif mode == '2':
            name = input("请输入学生姓名：")
            
        else:
            print("您的输入有误，请重新输入")
            continue
        
        #读取文件
        if os.path.exists(filename):
            with open(filename,'r') as file:
                studentList = file.readlines()
                
            for list in studentList:
                d = dict(eval(list))
                
                if id != '':
                    if d['id'] == id:
                        student_new.append(d)
                if name != '':
                    if d['name'] == name:
                        student_new.append(d)
            #开始打印
            printDate(student_new)
            student_new.clear()
            ismore = input("是否需要继续查询：")
            if ismore == 'y':
                isFlag = True
            else:
                isFlag = False
        else:
            print("没有读取到文件")
                        
main()

