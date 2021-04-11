#this file contains storage to a .txt, where is not used anywhere in the project
#Kept fow showing teammate contributeion, created by Joe
class qConnect:

    def __init__(self):
        self.aValue = 0  #action... -1 if moving and +12 for pickup/dropoff
        self.sValue = 0  #state


    #Qformula = Q(a,s)  (1-@)*Q(a,s) + @*[R(s’,a,s)+ γ*maxVa’Q(a’,s’)]
    #@=0.5 and y=0.5

    print("Connecting to Q-Table..")
    f= open("q.txt","r+")

    content = f.read()
    print(content)
    f.close()
    #Q table now closed


    with open("q.txt") as textFile:
        lines = [line.split() for line in textFile]


    print ("")#add some space

    print ( "value at row 1 line 2 is: " + lines[0][1])
    print ("value at row 3 line 4 is: " + lines[2][3])

    #writes updated q table into this file
    file = open("updatedQ.txt","w")
    file.write(content)
    file.close()

    #this function takes the current Node and returns either the coordinates or actual Node with the best Q value
    def returnMove():
        print ("Checking for best move..")

    returnMove()

    


