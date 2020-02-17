# 學生表基礎製作
def input_student():
    L = []
    while True:
        name = input("請輸入學生姓名: ")
        if not name:
            break
        age = int(input("請輸入學生年齡: "))
        score = int(input("請輸入學生成績: "))
        d = {} 
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L

def output_student(L):
    print('+------------+------+-------+')
    print('|   name     | age  | score |')
    print('+------------+------+-------+')
    for d in L:  
        t = (d['name'].center(12),
             str(d['age']).center(6),
             str(d['score']).center(7))
        line = "|%s|%s|%s|" % t  
        print(line)
    print('+------------+------+-------+')

def show_menu():
    print('+-----------------------------+')
    print('|  1) 添加學生資訊            |')
    print('|  2) 查看學生內容            |')
    print('|  3) 修改學生的成績          |')
    print('|  4) 刪除學生訊息            |')
    print('|  5) 年齡由高到低排名        |')
    print('|  6) 年齡由低到高排名        |')
    print('|  7) 分數由高到低排名        |')
    print('|  8) 分數由低到高排名        |')
    print('|  q) 退出                    |')
    print('+-----------------------------+')


def modify_student_info(lst):
    name = input("請輸入要修改學生的姓名: ")
    for d in lst:
        if d['name'] == name:
            score = int(input("請輸入新的成績: "))
            d['score'] = score
            print("修改", name, '的成績為', score)
            return
    else:
        print("沒有找到名為:", name, '的學生訊息')

def delete_student_info(lst):
    name = input("請輸入要刪除學生的姓名: ")
    for i in range(len(lst)): 
        if lst[i]['name'] == name:
            del lst[i]
            print("已成功删除: ", name)
            return True
    else:
        print("沒有找到名為:", name, "的學生")


def get_age(d):   
    return d['age']

def get_score(d):   
    return d['score']

def sort_agehigh(docs):
    L = sorted(docs, key=get_age, reverse=True)
    output_student(L)   

def sort_agelow(docs):
    L = sorted(docs, key=get_age)
    output_student(L) 

def sort_scorehigh(docs):
    L = sorted(docs,key=get_score, reverse=True)
    output_student(L)

def sort_scorelow(docs):
    L = sorted(docs,key=get_score)
    output_student(L)

def main():
    docs = []  
    while True:
        show_menu()
        s = input("請輸入選項: ")
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':  
            modify_student_info(docs)
        elif s == '4':  
            delete_student_info(docs)
        elif s == '5':  
            sort_agehigh(docs)
        elif s == '6':  
            sort_agelow(docs)
        elif s == '7':  
            sort_scorehigh(docs)
        elif s == '8':  
            sort_scorelow(docs)
        elif s == 'q':
            print("謝謝使用")
            return 
                
main()