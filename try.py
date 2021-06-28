import json
user=input("Hello , You want to do login or signup=")
f={}
data=[]
if user=="s":
    name=input("enter your name=")
    l, p, d = 0, 0, 0
    print("Note: In password alphabet , number , special charcter should be there(length 8)")
    paas = input("enter your password=")
    pass2=input("verify your password=")
    #for i in paas:
    if (len(paas) == 4):
        if paas==pass2:
            for i in paas:
                if (i.islower()):
                    l+=1                        
                if (i.isdigit()):
                    d+=1            
                if(i=='@'or i=='$'or i=='#'):
                    p+=1           
            if (l>=1 and p>=1 and d>=1): 
                e={}
                print("Enter the Profile")
                dis=input("enter your Discrption=")
                dob=input("enter your DOB=")
                hobby=input("enter your hobby=")
                gender=input("male or female")
                pro={}
                pro["dis"]=dis
                pro["dob"]=dob
                pro["hobby"]=hobby
                pro["gender"]=gender
                #print(pro)
                f["name"]=name
                f["pass"]=paas
                f["profile"]=pro
                data.append(f)
                e["user"]=data
                print(e,"***********************")
                j=open("user_details.json","r")
                k=j.read()

                if k=="":
                    with open("user_details.json", "w") as filehandle:
                        json.dump(e, filehandle,indent=5)
                        print("You are signup sucessfully")
                    
                else:
                    with open("user_details.json", "r") as j:
                        json_data = json.load(j)
                        list1= json_data['user']
                        print(list1,"&&&&&&&&&&&&&&&&&&&&&&")
                        for i in json_data["user"] : 
                            if i["name"]==name and i["pass"]==paas:
                                print("User already exist , Thank you 🙏")
                                break
                        else:
                            list1.append(f)
                            e["user"]=list1
                            print(list1,"######")
                            with open("user_details.json", "w") as filehandle:
                                json.dump(e, filehandle,indent=5)
                                print("You are signup sucessfully")
        else:
            print("Both password are not same")
    else:
        print("Password length 8 should be there")
    
else:               
    if user=="login":
        print('Hey:Welcome To Login Page :)')
        Name=input("enter the userName:")
        loginPassword=input("enter the password:")
        with open("user_details.json","r") as f:
            Data=json.load(f)
            for i in Data["user"]:
                if i["name"]==Name and i["pass"]==loginPassword:
                    print("Login Successfully")
                    print("user_name",Name)
                    print("Dis:",i["profile"]["dis"])
                    print("DOB:",i["profile"]["dob"])
                    print("Hobby:",i["profile"]["hobby"])
                    print("Gender:",i["profile"]["gender"])
                    break

            else:
                print("No match something is wrong")
    else:
        print('Please Enter The C0rrect Input')