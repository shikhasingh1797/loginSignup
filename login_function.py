import json
def sign():
    global name
    global paas
    global sign
    user=input("enter what you want login or signup=")
    name=input("enter your name=")
    paas=input("enter password=")
    paas1=input("enter password=")
    l,p,d=0,0,0
    if user=="s":
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
                    j=open("function.json","r")
                    k=j.read()
                    detail_list=[]
                    full_detail={}
                    user_name_password={}
                    detail_list.append(user_name_password)
                    full_detail["user"] = detail_list
                    discription()
                    with open("function.json", "w") as filehandle:
                        json.dump(full_detail, filehandle,indent=5)
                        print("Congratulations , You are signup sucessfully")
                else:
                    with open("function.json", "r") as j:
                        json_data = json.load(j)
                        print(json_data["user"],"user coming here")
                        for i in json_data["user"] : 
                            if i["name"]==name and i["password"]==paas:
                                print("User already exist , Thank you 🙏")
                                break

sign()
def discription():
    global user_name_password
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