
# functions go here

def yes_no(question):
    while True:

        response =input("Do you want to see the instructions? "). lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y": 
           return "yes"
        elif want_instructions == "no" or want_instructions == "n   ":
            return "no"  
        else:
            print("Please enter yes / no")  
 
# Main routine

want_instructions =yes_no("Do you want to see the instructions? "). lower()
print(f"you choose {want_instructions}") 


print("well done")
