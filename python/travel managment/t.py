# -- coding: utf-8 --
import sys
cc=True
def main():
  print("\n" + "=" * 70)
  print("\t W E L C O M E   T O   T R A V E L   M A N A G E M E N T   S Y S T E M")
  print("=" * 70)
  print("1...Add Package")
  print("2...Enquire Package")
  print("3...Modify Package")
  print("4...Display All Packages")
  print("5...Remove Package")
  print("6...Customer Registration")
  print("7...Customer List")
  print("8...Booking Package")
  print("9...Booking Details")
  print("10...Quit")
  print("-" * 70)
  ch=int(input("\t..::Select option::.."))
  if ch==1:
          print("\t\t Add new package details....")
          print("Enter package id:")
          id=int(input())
          print("Package Name")
          pname=input()
          print("Package Soruce-Destination")
          psd=input()
          print("Package Day-Night")
          pdn=input()
          print("Package Charges")
          pamt=input()
        
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "INSERT INTO package (id,pname,psd,pdn,pamt) VALUES (%s, %s,%s,%s,%s)"
          val = (id,pname,psd,pdn,pamt)
          mycursor.execute(sql, val)
          mycon.commit()
  if ch==2:
          print("\t\t Enquire package details....")
          print("Enter package id:")
          id=int(input())
                 
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "select * from package where id={}".format(id)
          
          mycursor.execute(sql)
          rec=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
          for rec1 in rec:
             print("Package Name: ",rec1[1])
             print("Source - Destination: ",rec1[2])
             print("Day Night: ",rec1[3])
             print("Amount: ",rec1[4])
  if ch==5:
          print("\t\t Remove package details....")
          
          print("Enter package id:")
          id=int(input())
              
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "delete from package where id={}".format(id)
          mycursor.execute(sql)
          mycon.commit()
          print("The  Package id:",id," details have been deleted...")
 
  if ch==4:
          print("\t\t Display all package details....")
              
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "select * from package"
          
          mycursor.execute(sql)
          rec=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
          for rec1 in rec:
             print("Package ID: ",rec1[0])
             print("Package Name: ",rec1[1])
             print("Source - Destination: ",rec1[2])
             print("Day Night: ",rec1[3])
             print("Amount: ",rec1[4])
  if ch==3:
          print("\t\t Modify Package Details....")
          print("1...Package Name")
          print("2...Package Soruce-Detstination")
          print("3...Package Day-Night")
          print("4...Package Charges")
          choice=int(input("Enter Choice:"))
          if choice==1:
              package_id=int(input("Enter Package ID:"))
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "select * from package where id={}".format(package_id)
              mycursor.execute(sql)
              recm=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
              for rec1 in recm:
                  print("Package ID: ",rec1[0])
                  print("Package Name: ",rec1[1])
                  print("Source - Destination: ",rec1[2])
                  print("Day Night: ",rec1[3])
                  print("Amount: ",rec1[4])
          
              package_name=input("New package Name:")
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "update package set pname='{}' where id={}".format(package_name,package_id)
              #print(sql)
              mycursor.execute(sql)
              mycon.commit()
              print("The  Package id:",package_id," name has been updated...")
          if choice==2:
              package_id=int(input("Enter Package ID:"))
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "select * from package where id={}".format(package_id)
              mycursor.execute(sql)
              recm=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
              for rec1 in recm:
                  print("Package ID: ",rec1[0])
                  print("Package Name: ",rec1[1])
                  print("Source - Destination: ",rec1[2])
                  print("Day Night: ",rec1[3])
                  print("Amount: ",rec1[4])
          
              package_sd=input("New Package Source-Destinations:")
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "update package set psd='{}' where id={}".format(package_sd,package_id)
              #print(sql)
              mycursor.execute(sql)
              mycon.commit()
              print("The  Package id:",package_id," source-destination has been updated...")
          if choice==3:
              package_id=int(input("Enter Package ID:"))
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "select * from package where id={}".format(package_id)
              mycursor.execute(sql)
              recm=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
              for rec1 in recm:
                  print("Package ID: ",rec1[0])
                  print("Package Name: ",rec1[1])
                  print("Source - Destination: ",rec1[2])
                  print("Day Night: ",rec1[3])
                  print("Amount: ",rec1[4])
          
              package_dn=input("New Package Day-Night:")
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "update package set pdn='{}' where id={}".format(package_dn,package_id)
              #print(sql)
              mycursor.execute(sql)
              mycon.commit()
              print("The  Package id:",package_id," day-night has been updated...")
          if choice==4:
              package_id=int(input("Enter Package ID:"))
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "select * from package where id={}".format(package_id)
              mycursor.execute(sql)
              recm=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
              for rec1 in recm:
                  print("Package ID: ",rec1[0])
                  print("Package Name: ",rec1[1])
                  print("Source - Destination: ",rec1[2])
                  print("Day Night: ",rec1[3])
                  print("Amount: ",rec1[4])
          
              package_dn=input("New Package Amount:")
              import mysql.connector
              mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
              mycursor = mycon.cursor()
              sql = "update package set pamt='{}' where id={}".format(package_dn,package_id)
              #print(sql)
              mycursor.execute(sql)
              mycon.commit()
              print("The  Package id:",package_id," changes have been updated...")
  if ch==6:
          print("\t\t Add new customer details....")
          print("Enter Customer Name id:")
          cid=int(input())
          print("Customer Name:")
          cname=input()
          print("Customer Address:")
          cadd=input()
          print("Customer Contact No:")
          cno=input()
          
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "INSERT INTO customer (cid,cname,cadd,cno) VALUES (%s, %s,%s,%s)"
          val = (cid,cname,cadd,cno)
          mycursor.execute(sql, val)
          mycon.commit()
          print("The Customer has been registered")
      
  if ch==7:
          print("\t\t Display all Customer details....")
              
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "select * from customer"
          
          mycursor.execute(sql)
          rec=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
          for rec1 in rec:
             print("Customer ID: ",rec1[0])
             print("Customer Name: ",rec1[1])
             print("Address: ",rec1[2])
             print("Contact No: ",rec1[3])
             
  if ch==8:
          print("\t\t Display all Package details....")     
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "select * from package"
          
          mycursor.execute(sql)
          rec=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
          for rec1 in rec:
             print("Package ID: ",rec1[0])
             print("Package Name: ",rec1[1])
             print("Source - Destination: ",rec1[2])
             print("Day Night: ",rec1[3])
             print("Amount: ",rec1[4])
      
          print("Enter package id for booking:")
          pid=int(input())
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "select * from package where id={}".format(pid)
          mycursor.execute(sql)
          recm=mycursor.fetchall()
          pbid=""
          pbname=""
          pbamt=""
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
          for rec1 in recm:
            print("Package ID: ",rec1[0])
            pbid=rec1[0]
            print("Package Name: ",rec1[1])
            pbname=rec1[1]
            print("Source - Destination: ",rec1[2])
           # pbsn=rec1[2]
            print("Day Night: ",rec1[3])
            #pbdn=rec1[3]
            print("Amount: ",rec1[4])
            pbamt=rec1[4]
          print("You have selected the above  package  booking:")  
          print("Enter customer id for booking:")
          cid=int(input())
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "select * from customer where cid={}".format(cid)
          
          mycursor.execute(sql)
          rec=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
          cbid=""
          cbname=""
          for rec1 in rec:
            print("Customer ID: ",rec1[0])
            cbid=rec1[0]
            print("Customer Name: ",rec1[1])
            cbname=rec1[1] 
            print("Address: ",rec1[2])
            print("Contact No: ",rec1[3])
          print("Enter Total Member :")
          tm=int(input())
          tamt=tm*int(pbamt)
          
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "INSERT INTO booking (cid,cname,pid,pbname,person,tamt) VALUES (%s, %s,%s,%s,%s,%s)"
          val = (cbid,cbname,pbid,pbname,tm,tamt)
          mycursor.execute(sql, val)
          mycon.commit()
          print("The Package is booked for the id:",cbid)  
  if ch==9:
          print("\t\t Display all Package details....")     
          import mysql.connector
          mycon= mysql.connector.connect(host="localhost",user="root",passwd="1234",database="travel")
          mycursor = mycon.cursor()
          sql = "select * from booking"
          
          mycursor.execute(sql)
          rec=mycursor.fetchall()
         # print("Package Name","\t","Source-Destination","\t","Day-Night","\t","Charges")
          for rec1 in rec:
             print("Customer ID: ",rec1[0])
             print("Customer Name: ",rec1[1])
             print("Package ID: ",rec1[2])
             print("Package Name: ",rec1[3])
             print("Member: ",rec1[4])
             print("Total Amount: ",rec1[5]) 
  if ch==10:
       #  print("exit")
         sys.exit()
 #         cc=False
         # break
             
             

while cc==True:
 main()
