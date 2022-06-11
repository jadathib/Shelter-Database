from animal_shelter import AnimalShelter
#create the object from the class
shelter = AnimalShelter("myUserAdmin","trinidad1" )
data = {"age_upon_outcome":"1.7 years","animal_type":"Cat"}
if shelter.create(data): 
    print("animal added")
    else:
        print ("Error")
    
# return the value of the created record 
return shelter.data