# snake water gun



import random
# ------------------------- this generate the random number from the selected space  for the computer 
computer=random.choice([-1,0,1])
selects={"snake":-1,"water":0,"gun":1}
# print(computer)
selected_com=" "
for key,value in selects.items():
    if computer==value:
        selected_com=key
        break
# -------------




print("This is a Snake,Water,Game\n")
user=input("Here,You need to select \n s for Snake \n w for Water \n g for gun\n").lower()

select=" "
choose=["snake","water","gun"]

for name in choose:
    if(name.startswith(user)):
        select=name
        break
print("------------------------------")
print(f"\nYou choose {select}")
print(f"Computer choose {selected_com}\n")
print("------------------------------")


if selected_com==select:
    print("Tie!!")
elif selected_com=="snake" and select=="water":
    print("Computer win!")
elif selected_com=="snake" and select=="gun":
    print("You won!")
elif selected_com=="water" and select=="snake":
    print("You won!")
elif selected_com=="water" and select=="gun":
    print("Computer won!")
elif selected_com=="gun" and select=="water":
    print("Computer Won!")
elif selected_com=="gun" and select=="snake":
    print("Computer won!")
else:
    print("Error!")









        

    
