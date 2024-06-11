mealList=[] #initialising the meal list for use in functions
class Meal:

    def __init__(self,time,mealType,description,serving,calories,saturatedFat):
        self.time=time
        self.mealType=mealType
        self.description=description
        self.serving=serving
        self.calories=calories
        self.saturatedFat=saturatedFat

    @classmethod
    def OutputRecords(self):

        mealFile = open("meals.txt", "r")  # open meal file in read mode
        for row in mealFile:
            row = row.rstrip("\n").split(', ')
            mealList.append(Meal(row[0],row[1],row[2],row[3],row[4],row[5]))
        count=0
        for meal in mealList:
            print("\nRecord ", count + 1)
            print("Time: ", meal.time)
            print("Meal Type: ", meal.mealType)
            print("Description Of Meal: ", meal.description)
            print("Serving(in g): ", meal.serving)
            print("Calories: ", meal.calories)
            print("Saturated Fat(in g): ", meal.saturatedFat)
            count=count+1
        # for loop to print out record details
        mealList.clear()  # clears meal list
        mealFile.close()  # Closing meal file

    @classmethod
    def TotalCalories(self):
        mealFile = open("meals.txt", "r")  # open meal file in read mode
        totalCalories = 0


        for row in mealFile:
            row = row.rstrip("\n").split(', ')
            mealList.append(Meal(row[0],row[1],row[2],row[3],row[4],row[5]))
        # for loop to append rows of meal file to meal list

        for meal in mealList:
            totalCalories=totalCalories+int(meal.calories)

        # for loop to add up total calories
        print("The total calories consumed today is ", totalCalories)
        mealList.clear()  # clears meal list
        mealFile.close()  # Closing meal file
    # function to calculate and output total calories consumed

    @classmethod
    def AverageServing(self):
        mealFile = open("meals.txt", "r")  # open meal file in read mode
        totalServing = 0.0

        for row in mealFile:
            row = row.rstrip("\n").split(', ')
            mealList.append(Meal(row[0],row[1],row[2],row[3],row[4],row[5]))
        # for loop to append rows of text file to meal list
        for meal in mealList:
            totalServing=totalServing+float(meal.serving)
        # for loop for adding serving size to totalServing
        average = totalServing / len(mealList)
        print("The average serving is ", format(average, '.2f'), "g")
        mealList.clear()  # clears meal list
        mealFile.close()  # Closing meal file
    # function to calculate average serving and output it

    @classmethod
    def AmountAte(self):
        mealFile = open("meals.txt", "r")  # open meal file in read mode
        totalAmount = 0.0
        count = 0
        for row in mealFile:
            row = row.rstrip("\n").split(', ')
            mealList.append(Meal(row[0], row[1], row[2], row[3], row[4], row[5]))
        # for loop to append rows of text file to meal list

        for meal in mealList:
            totalAmount=totalAmount+float(meal.serving)
        print("The total amount of food consumed today is ", format(totalAmount, '.2f'), "g")
        # for loop for adding serving size to totalAmount
        mealList.clear()  # clears meal list
        mealFile.close()  # Closing meal file
    # function to calculate the total amount consumed and output it

    @classmethod
    def FatQuery(self):
        mealFile = open("meals.txt", "r")  # open meal file in read mode
        fatThreshold = float(input("Enter Fat Threshold: "))  # prompts ser to enter in a saturated fat threshold
        filteredList = []  # initalising a filtered list to contain any records above the fat threshold
        count=0

        for row in mealFile:
            row = row.rstrip("\n").split(', ')
            mealList.append(Meal(row[0], row[1], row[2], row[3], row[4], row[5]))
        # for loop to append rows to meal list
        for meal in mealList:
            if float(meal.saturatedFat)>fatThreshold:
                filteredList.append(Meal(meal.time,meal.mealType,meal.description,meal.serving,meal.calories,meal.saturatedFat))
        # for loop to append any meals that have a saturated fat amount above the fat threshold into the filtered list
        if (filteredList == []):
            print("No records found")
        else:
            for meal in filteredList:
                print("\nRecord ", count + 1)
                print("Time: ", meal.time)
                print("Meal Type: ", meal.mealType)
                print("Description Of Meal: ", meal.description)
                print("Serving(in g): ", meal.serving)
                print("Calories: ", meal.calories)
                print("Saturated Fat(in g): ", meal.saturatedFat)
                count = count + 1
            # for loop to print out record details
        # if filtered list is empty, the system will print that no records have been found else all records in the filtered list will be printed
        mealList.clear()  # clears meal list
        mealFile.close()  # Closing meal file
    # function to query records above a certain fat threshold and output it

    @classmethod
    def AddRecord(self):
        mealFile = open("meals.txt", "a")  # open meal file in append mode
        time = str(input("Time(in XX:XX format): "))
        mealType = str(input("Meal Type: "))
        description = str(input("Meal Discription: "))
        serving = str(input("Serving(in g): "))
        calories = str(input("Calories: "))
        saturatedFat = str(input("Saturated Fat(in g): "))
        # prompts the user to enter in values

        mealFile.write(time)
        mealFile.write(", ")
        mealFile.write(mealType)
        mealFile.write(", ")
        mealFile.write(description)
        mealFile.write(", ")
        mealFile.write(serving)
        mealFile.write(", ")
        mealFile.write(calories)
        mealFile.write(", ")
        mealFile.write(saturatedFat)
        mealFile.close()
        # Appends the prompted values into the text file
        Meal.SortRecords()  # calls SortRecords() function
    # function to add a record to the meals.txt text file

    @classmethod
    def SortRecords(self):
        mealFile = "meals.txt"

        with open(mealFile) as mealIn:  # open meal file
            for row in mealIn:
                row = row.rstrip("\n").split(', ')
                mealList.append(Meal(row[0],row[1],row[2],row[3],row[4],row[5]))
            # for loop to append rows into meal list
        mealList.sort(key=lambda x:x.time, reverse=False)  # sorts meal list on order of time
        mealIn.close()  # closes mealFile

        with open(mealFile, 'w') as mealOut:  # open meal file in write mode
            for meal in mealList:
                mealOut.write(meal.time)
                mealOut.write(", ")
                mealOut.write(meal.mealType)
                mealOut.write(", ")
                mealOut.write(meal.description)
                mealOut.write(", ")
                mealOut.write(meal.serving)
                mealOut.write(", ")
                mealOut.write(meal.calories)
                mealOut.write(", ")
                mealOut.write(meal.saturatedFat)
                mealOut.write('\n')
            # for loop to write each meal into the meals.txt file
        mealOut.close()  # Closing meal file
    # function to sort records in the meals.txt text file in ascending order of time

