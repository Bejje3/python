import random 

print("\n-----------------------") 
print(".:gissatalet:") 

print("Gissa ett tal mellan 1-10, du får 3 st försök\n") 
slumptal = random.randint(1, 10) 
print(f"Fusk: {slumptal}") 
i=0 
hittat = False 


while i<3: 
    gissatal = input("Mata in ett tal: ") 

    if slumptal == int(gissatal): 
        hitta = True 
        print("Gratis du får en fet öl!") 
        break 

    i += 1 

    if hittat:
        print("Du får en öl till") 

    else: 
        print("du får ett försök till! ") 



if hittat:
    print("Du får en öl till!")
else: 
    print ("bättre lycka nästa gång") 


print("---------------------------------------")