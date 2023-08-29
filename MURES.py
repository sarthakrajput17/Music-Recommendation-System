
import pymysql
import sys

db = pymysql.connect(host='localhost',user='root',password='sp230303')
c = db.cursor()
c.execute('USE MRS')

def ra():
    n = input("\t\t\t\t\t\t\t\t\t\t    Enter the name of artist : ")
    print("\t\t\t\t\t\t\t\t\t\t    Recommending songs of %s ..."%n)
    print()
    print("=====================================================================================================================================================================================================")
    print()
    db = pymysql.connect(host='localhost',user='root',password='sp230303',db='MRS')
    c = db.cursor()
    a ='%'+n+'%'
    s = (a)
    c.execute("Select Song from songs where Artists LIKE %s ORDER BY popularity DESC",s)
    o = c.fetchall()
    if o == ():
        print("Sorry :( I don't have any song of the artist to recommend you.")
    else :
        for i in o :
            print("\t\t\t\t\t\t\t\t\t\t  ->",i[0])

        song = input("Which song did you liked the most ? ")
        f = '%'+song+'%'
        x = (f)
        c.execute("select Popularity from songs where song LIKE %s",x)
        y = c.fetchall()
        z = y[0]
        w = z[0]
        w += 1
        p = "update songs set Popularity = %d where song = '"%w+song+"'"
        c.execute(p)
        db.commit()
        

    print()
    print("=====================================================================================================================================================================================================")
    print()

def rg():
    n = input("\t\t\t\t\t\t\t\t\t\t    Enter a genre : ")
    print("\t\t\t\t\t\t\t\t\t\t    Recommending %s songs..."%n)
    print()
    print("=====================================================================================================================================================================================================")
    print()
    db = pymysql.connect(host='localhost',user='root',password='sp230303',db='MRS')
    c = db.cursor()
    a ='%'+n+'%'
    s = (a)
    c.execute("Select Song from songs where Genres LIKE %s ORDER BY popularity DESC",s)
    o = c.fetchall()
    if o == ():
        print("Sorry :( I don't have any songof the genre to recommend you.")
    else :
        for i in o :
            print("\t\t\t\t\t\t\t\t\t\t  ->",i[0])
        song = input("Which song did you liked the most ? ")
        f = '%'+song+'%'
        x = (f)
        c.execute("select Popularity from songs where song LIKE %s",x)
        y = c.fetchall()
        z = y[0]
        w = z[0]
        w += 1
        p = "update songs set Popularity = %d where song = '"%w+song+"'"
        c.execute(p)
        db.commit()

    print()
    print("=====================================================================================================================================================================================================")
    print()

def rl():
    n = input("\t\t\t\t\t\t\t\t\t\t    Enter language : ")
    print("\t\t\t\t\t\t\t\t\t\t    Recommending %s songs..."%n)
    print()
    print("=====================================================================================================================================================================================================")
    print()
    db = pymysql.connect(host='localhost',user='root',password='sp230303',db='MRS')
    c = db.cursor()
    a ='%'+n+'%'
    s = (a)
    c.execute("Select Song from songs where Languages LIKE %s ORDER BY popularity DESC",s)
    o = c.fetchall()
    if o == ():
        print("Sorry :( I don't have any song of the language to recommend you.")
    else :
        for i in o :
            print("\t\t\t\t\t\t\t\t\t\t  ->",i[0])
        song = input("Which song did you liked the most ? ")
        f = '%'+song+'%'
        x = (f)
        c.execute("select Popularity from songs where song LIKE %s",x)
        y = c.fetchall()
        z = y[0]
        w = z[0]
        w += 1
        p = "update songs set Popularity = %d where song = '"%w+song+"'"
        c.execute(p)
        db.commit()

    print()
    print("=====================================================================================================================================================================================================")
    print()

def r():
    print("\t\t\t\t\t\t\t\t\t\t    Recommending songs...")
    print()
    print("=====================================================================================================================================================================================================")
    print()
    db = pymysql.connect(host='localhost',user='root',password='sp230303',db='MRS')
    c = db.cursor()
    c.execute("Select Song from songs ORDER BY popularity DESC")
    o = c.fetchall()
    if o == ():
        print("Sorry :( I don't have any song to recommend you.")
    else :
        for i in o :
            print("\t\t\t\t\t\t\t\t\t\t  ->",i[0])
        song = input("Which song did you liked the most ? ")
        f = '%'+song+'%'
        x = (f)
        c.execute("select Popularity from songs where song LIKE %s",x)
        y = c.fetchall()
        z = y[0]
        w = z[0]
        w += 1
        p = "update songs set Popularity = %d where song = '"%w+song+"'"
        c.execute(p)
        db.commit()

    print()
    print("=====================================================================================================================================================================================================")
    print()


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("                                                        !!!!             !!!! !!!!    !!!! !!!!!!!!     !!!!!!!!!!! !!!!!!!!!!                                         ")
print("                                                        !!!!!           !!!!! !!!!    !!!! !!!!! !!!!   !!!!!!!!!!! !!!!!!!!!!       ")
print("                                                        !!!!!!         !!!!!! !!!!    !!!! !!!!   !!!!  !!!!        !!!!          ")
print("                                                        !!!!!!!       !!!!!!! !!!!    !!!! !!!!    !!!! !!!!        !!!!          ")
print("                                                        !!!! !!!!   !!!! !!!! !!!!    !!!! !!!!   !!!!  !!!!!!!!    !!!!!!!!!!       ")
print("                                                        !!!!   !!!!!!!   !!!! !!!!    !!!! !!!! !!!!    !!!!!!!!    !!!!!!!!!!       ")
print("                                                        !!!!    !!!!!    !!!! !!!!    !!!! !!!!!!!!     !!!!              !!!!     ")
print("                                                        !!!!             !!!! !!!!    !!!! !!!! !!!!    !!!!              !!!!       ")
print("                                                        !!!!             !!!! !!!!!!!!!!!! !!!!  !!!!   !!!!!!!!!!! !!!!!!!!!!       ")
print("                                                        !!!!             !!!! !!!!!!!!!!!! !!!!   !!!!  !!!!!!!!!!! !!!!!!!!!!           ")
print("                                                                                      ")
print("                                                                                     ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MUsic REcommendation System ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
    

while True :
    print()
    print("\t\t\t\t\t\t\t\t\t HOW DO YOU WANT ME TO RECOMMEND YOU SONGS ???")
    print()
    print("\t\t\t\t\t\t\t\t\t\t    1- Songs of an Artist")
    print("\t\t\t\t\t\t\t\t\t\t    2- Songs of a genre")
    print("\t\t\t\t\t\t\t\t\t\t    3- Songs of a language")
    print("\t\t\t\t\t\t\t\t\t\t    4- Any song")
    print("\t\t\t\t\t\t\t\t\t\t    5- Exit")
    print()
    while True:
        choice=int(input("\t\t\t\t\t\t\t\t\t Enter the number adjacent to your choice : "))
        print()
        if choice == 1 :
            ra()
            break

        elif choice == 2 :
            rg()
            break

        elif choice == 3 :
            rl()
            break

        elif choice == 4 :
            r()
            break

        elif choice == 5 :
            sys.exit()

        else :
            print("You entered wrong input!")


    end = input("PRESS ENTER TO EXIT AND 'Y' IF YOU WANT TO LAUNCH THE PROGRAM AGAIN : ")
    if end != 'Y' and end !='y' :
        sys.exit()

        
        
            
        
    
    
