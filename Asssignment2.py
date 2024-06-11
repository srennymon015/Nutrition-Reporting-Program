
from Assignment2Class import * #imports all code from Assignment2Class
import sys #imported sys to use to close the program

def main():
    print("Welcome to te Nutrition Reporting Program")
    print("Select 1 to view all records")
    print("Select 2 to view Total Calories consumed today")
    print("Select 3 to view Average Serving Weight")
    print("Select 4 to view Total Amount of Food Consumed today")
    print("Select 5 to Query about foods over Saturated Fat Threshold")
    print("Select 6 to Add a Record")
    print("Select 7 to quit the program")
    choice=int(input("Select Option: ")) #prompts user to select option

    while(choice==1 or choice==2 or choice==3 or choice==4 or choice==5 or choice==6 or choice==7):
        if(choice==1):
            Meal.OutputRecords()# calls Meal.OutputRecords() function
            main()#calls main fuction

        elif(choice==2):
            Meal.TotalCalories()#calls Meal.TotalCalories() fuction
            main()#calls main fuction

        elif(choice==3):
            Meal.AverageServing()#calls Meal.AverageServing() fuction
            main()#calls main fuction

        elif(choice==4):
            Meal.AmountAte()#calls Meal.AmountAte() fuction
            main()#calls main fuction

        elif(choice==5):
            Meal.FatQuery()#calls Meal.FatQuery() fuction
            main()#calls main fuction

        elif(choice==6):
            Meal.AddRecord()#calls Meal.AddRecord() fuction
            main()#calls main fuction

        elif(choice==7):
            print("Thank you for using the Nutrition Reporting Program. Goodbye!!")
            sys.exit()#exits program


    else:
        print("ERROR!!! Select a valid option")
        main()#calls main() function
        # #while loop for choice. If choice is not 1 to 7, an error message will be printed and the main method will be recalled
#main function

main()#calls main fuction