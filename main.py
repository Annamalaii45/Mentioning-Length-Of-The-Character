# Comparision operators


_="""                                            Mentioning Length of the Character"""

print(_)

name=input("Enter your name: ")

if len(name) > 50:
    print("Maximum the name should be in 50 characters")

elif len(name) < 3:
    print("Name must be atleast in 3 characters")

else:
    print("Name looks good")

