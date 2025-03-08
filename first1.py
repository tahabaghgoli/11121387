first_name = input("please enter your first name = ")
last_name = input("please enter your last name = ")
national_code = input("please enter your national code = ")
age = input("please enter your age = ")

data = {}
data['2982112213'] = {"first_name" : 'mohammadtaha' , "last_name" : 'baghgoli' ,"age" : "16" , "national_code" : "2982112213" }
data['2982102811'] = {"first_name" : 'mohammadmahdi' , "last_name" : 'shamsaldini' ,"age" : "16" , "national_code" : "2982102811" }
data['2982099918'] = {"first_name" : 'mohammadfazel' , "last_name" : 'saebi' ,"age" : "16" , "national_code" : "2982099918" }

if national_code in data:
        user_data = data[national_code]
        if (user_data["first_name"] == first_name and user_data["last_name"] == last_name and user_data["national_code"] == national_code and user_data["age"] == age):
            print("information is correct, Welcome!")
        else:
            print("information isnt correct!")
else:
    print("There is no user with this national code !")




