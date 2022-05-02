#School Administration system
import csv

condition = True

def csv_info(lst1):
    with open("info.csv","a",newline='') as file:
        writer=csv.writer(file)

        if file.tell()== 0:
            writer.writerow(["Name","Age","Contact No.","Email ID"])

        writer.writerow(lst1)

if __name__=='__main__':
    condition = True
    n=1

    
    while (condition):
        info=input("Enter Student information for student #{} in the following format (Name, Age, Contact No., E-mail): ".format(n))

        #into list format
        lst1=info.split(",")

        print("\nThe entered information is:- \nName: {}\nAge: {}\nContact No.: {}\nEmail ID: {}".format(lst1[0],lst1[1],lst1[2],lst1[3]))

        cc=input("Is the entered information correct (yes/no): ")
        if cc=="yes":
            csv_info(lst1) 
        
            y_n=input("Enter (yes/no) if you want to enter information again: ")
          
            if y_n=="yes":
                condition=True
                n+=1
            if y_n=="no":
                condition=False
        elif cc=="no":
            print("\nPlease re-enter values")
