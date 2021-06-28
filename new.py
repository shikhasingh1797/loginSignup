import json
user=input("Hello , You want to do login or signup=")
# dic1={}
# list1=[]
# f={}
if user=="signup":
    name=input("enter your name=")
    l, p, d = 0, 0, 0
    print("Note: In password alphabet , number , special charcter should be there(length 8)")
    paas = input("enter your password=")
    paas1=input("verify your password=")
    if (len(paas) == 4):
        if paas==paas1:
            for i in paas:
                if (i.islower()):
                    l+=1                        
                if (i.isdigit()):
                    d+=1            
                if(i=='@'or i=='$'or i=='#'):
                    p+=1  
                            
            if (l>=1 and p>=1 and d>=1):
                j=open("new_details.json","r")
                k=j.read()
                if k=="":
                    detail_list = []
                    full_detail = {}
                    user_name_password={}
                    user_name_password["name"]=name
                    user_name_password["password"]=paas
                    dis=input("enter your Discrption=")
                    dob=input("enter your DOB=")
                    hobby=input("enter your hobby=")
                    gender=input("male or female=")
                    user_name_password['profile'] = {
                        "dis":dis,
                        "dob":dob,
                        "hobby":hobby,
                        "gender":gender
                    } 
                    detail_list.append(user_name_password)
                    full_detail["user"] = detail_list
                    with open("new_details.json", "w") as filehandle:
                        json.dump(full_detail, filehandle,indent=5)
                        print("Congratulations , You are signup sucessfully")
                else:
                    with open("new_details.json", "r") as j:
                        json_data = json.load(j)
                        print(json_data["user"],"user coming here")
                        for i in json_data["user"] : 
                            if i["name"]==name and i["password"]==paas:
                                print("User already exist , Thank you 🙏")
                                break
                        else:
                            user_name_password={}
                            user_name_password["name"]=name
                            user_name_password["password"]=paas
                            dis=input("enter your Discrption=")
                            dob=input("enter your DOB=")
                            hobby=input("enter your hobby=")
                            gender=input("male or female=")
                            user_name_password['profile'] = {
                              "dis":dis,
                              "dob":dob,
                              "hobby":hobby,
                              "gender":gender
                            } 
                            json_data["user"].append(user_name_password)
                            with open("new_details.json", "w") as filehandle:
                                json.dump(json_data, filehandle,indent=5)
                                print("You are signup sucessfully")
        else:
            print("Both password are not same")
    else:
        print("password length 8 should be there")

#Login process        
else:
    if user=="login":
        print('Hey:Welcome To Login Page :)')
        Name=input("enter the userName:")
        loginPassword=input("enter the password:")
        with open("new_details.json","r") as f:
            Data=json.load(f)
            for i in Data["user"]:
                if i["name"]==Name and i["password"]==loginPassword:
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