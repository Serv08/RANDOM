def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz" # to locate what room the animal will be
    print("Enter 'done' when done.")
    
    zoo = [[] for ele in alphabet]
    # main list for all animals
    # each list elements is the stable for each letters
    
    # takes all user input until 'done'
    animalShipment = askAnimals()
    
    # puts them accordingly in the proper element list in the 'housing' list
    for animals in animalShipment:
        # initial of animal in shipment
        initial_of_animal = animals[0]
        
        # index of initial of animal in the alphabet
        initial_of_animal_indexed = alphabet.index(initial_of_animal)
        
        # append tha animals in their respective stables
        zoo[initial_of_animal_indexed].append(animals)
    
    zoo = [sorted(stables) for stables in zoo]
    print(zoo)
    

def askAnimals():
    animalShipment = []
    while True:
        animal = str(input('Enter name of the animal: '))
        animalShipment.append(animal)
        if animal == 'done':
            del animalShipment[-1]
            break
        elif animal == ' ':
            del animalShipment[-1]
            print('\tENTER AN ANIMAL!')
    return animalShipment\

if __name__ == '__main__':
    main()