#armando Martinez
#1/13/23
#To-Do List part 2

list=["Home Alone", "Cars", "Iron man", "Barbie", "Wall-E"]

def toDo():
     print("Movie list")
     print("Please choose an operation:(Type in a number between 1-8)\n1.Add a task to the To-Do list \n2. View Current To-Do List \n3. Mark a task as completed \n4.Remove a task from the to-do list \n5.Remove all tasks from the to do list \n6. Sort the list alphabetically \n7.Print the number of items on the to do list \n8.Quit the program")
     option= int(input("Option: "))
     if(option == 1):
         x=input("Add Another Movie")
         list.append(x)
         print(list)
     if(option == 2):
         print (list)

     if(option==3):
        ans=input("please enter a movie to change: ")
        i=list.index(ans)
        list[i]= ans+" ✔️"
        print(list)
     if(option == 4):
        ans=input("please enter a movie to remove: ")
        i=list.index(ans)
        list.remove(ans)
        print(list)
     if(option==5):
         list.clear()
         print(list)
     if(option==6):
         list.sort()
         print(list)
     if(option==7):
         print(len(list))

     if(option == 8):
         quit()
#resources
#https://www.geeksforgeeks.org/python-string-length-len/ 
#main
toDo()