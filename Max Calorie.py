# OPen the starbucks csv file for reading
sbfile = open("Starbucks.csv","r")

# The first line is a header throw it away (look at the file, you'll see)
rec = sbfile.readline()

#Initialize the max calorie variable to none. 
maxcal = 'None'

# This for loop loops through all the lines in the file. 
for rec in sbfile:
    
# split the line, on a comma,
# and assign each split (3 of them) into 3 string variables
# item, calories, and carbs
    (item, calories, carbs) = rec.split(",")
    
# do the usual comparison to find max.
# question: can we covert the last item (carbs)
# directly into float? try it. why does it fail?
# why do we have the maxitem variable?
# did we properly initialize maxitem? 
    if (maxcal == 'None' or maxcal < float(calories)):
        maxcal = float(calories)
        maxitem = item
        
#after seeing all the calories print the item with
#most calories        
print(maxitem, " Max cal = ", maxcal)

