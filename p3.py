from model import *
import pickle

class MainApp():
    cat_list=[]
    exp_list=[]
    def startApp(self):
        with open("data","rb") as f1:
            obj=pickle.load(f1)
        MainApp.cat_list=obj
        
        with open("data1","rb") as f2:
            obj1=pickle.load(f2)
        MainApp.exp_list=obj1
        
        while True:
            choice = self.printOption()
            if choice==1:
                self.add_Category()
            elif choice==2:
                self.listing()
            elif choice==3:
                self.expenseentry()
            elif choice==4:
                self.reportcatwise()
            elif choice==5:
                self.reportmonthyear()
            elif choice==6:
                self.amount()
            elif choice==7:
                self.montrange()
            elif choice==8:
                with open("data","wb") as cl:
                    pickle.dump(MainApp.cat_list,cl)
                with open("data1","wb") as el:
                    pickle.dump(MainApp.exp_list,el) 
                break

        
    def printOption(self):
        print("=================================")
        print("press 1 for add category        !")
        print("press 2 for category listing    !")
        print("press 3 for Expanse Entry       !")
        print("press 4 for report - cat-wise   !")
        print("press 5 for report month-year   !")
        print("press 6 for amounts             !")
        print("press 7 for report month range  !")
        print("press 8 for exit                !")
        print("=================================")
        ch=int(input("enter your choice"))
        return ch

    
    def add_Category(self):
        cid=int(input("enter id"))
        cname=input("enter category name")
        x=[]
        y=[]
        for i in MainApp.cat_list:
            x.append(i.get_cat_id())
            y.append(i.get_cat_name())
            print(x,y)
        '''if cid.get_cat_id() in main.cat_list or cname.get_cat_name() in main.cat_list:
            print("already exist")
        else:
            c=Categories()
            c.set_cat_id(cid)
            c.set_cat_name(cname)
            MainApp.cat_list.append(c)
            print("=================================")
            print("done")
            '''
        
    def listing(self):
        
        for i in MainApp.cat_list:
            print(i.get_cat_id(),i.get_cat_name())
            
            
    def expenseentry(self):
        self.listing()
        print("=================================")
        cid=int(input("enter category id:- "))
        amt=float(input("enter amount"))
        rem=input("enter remark")
        date=input("enter date dd/mm/yyyy:-")
        print("=================================")
        e=Expanse()
        e.set_amount(amt)
        e.set_remark(rem)
        e.set_date(date)
        e.set_catogary_id(cid)
        MainApp.exp_list.append(e)
        print("=================================")
        print("done")
        
        
    def reportcatwise(self):
        totle=0
        self.listing()
        cid=int(input("enter category"))
        print("=================================")
        for i in MainApp.exp_list:
            a=i.get_catogary()
            
            if a == cid:
                print(i.get_ammount(),i.get_remark(),i.get_date())
                totle=totle+i.get_ammount()
        print("=================================")  
        print("totle expanse is:- ",totle)
        print("=================================")
        
        
    def reportmonthyear(self):
        totle=0
        date1=input("enter date from mm/yyyy :-")
        print("ID====remark====Amount====date====")
        for i in MainApp.exp_list:
            if date1==i.get_date()[3:]: 
                print(i.get_catogary(),i.get_remark(),i.get_ammount(),i.get_date())
                totle=totle+i.get_ammount()
        print("=================================") 
        print("totle is",totle)

        
    def amount(self):
        totle=0
        x=int(input("enter minimum range of  amount"))
        y=int(input("enter maximum range of  amount"))
        for i in MainApp.exp_list:
            if x <= i.get_ammount() and y >= i.get_ammount():
                totle=totle+i.get_ammount()
                print(i.get_catogary(),i.get_remark(),i.get_ammount(),i.get_date())
        print("=================================")       
        print("your totle expanse is:-",totle)
        

    def montrange(self):
        month1=input("enter month from mm/yyyy:-")
        month2=input("enter month to mm/yyyy:-")
        print("ID====remark====Amount====date=====")
        totle=0
        for i in MainApp.exp_list:
            x=i.get_date()[3:].split("/")
            y=month1.split("/")
            z=month2.split("/")
            if x[0] >= y[0] and x[0] <= z[0]:
                if x[1] >= y[1] and x[1] <= z[1]:
                    print(i.get_catogary(),i.get_remark(),i.get_ammount(),i.get_date())
                    totle=totle+i.get_ammount()
        print("=================================")
        print("Totle :-",totle)
        

m=MainApp()
m.startApp()
