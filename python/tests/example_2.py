frontRotation = [[0,1,2,3,4,5,6,7,8],[6,7,8],[0,3,6],[2,5,8],[0,1,2]]
frontRotationRules = [[6,3,0,7,4,1,8,5,2]]
class Cube:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.front = [0,1,2,3,4,5,6,7,8,]
        #self.front = [1]*9
        self.up    = [2]*9
        self.down  = [3]*9
        self.back   = [4]*9
        self.left  = [5]*9
        self.right = [6]*9
        
    def printOUT(self) -> None:
        print (self.front[0:3])
        print (self.front[3:6])
        print (self.front[6:9])
    #node чать которую нужно повернуть
    def rotation(self,frontArr,upArr,rightArr,leftArr,downArr,frontRotation,frontRotationRules) -> None:
        tempArrFront = frontArr.copy()
        tempArrUp = upArr.copy()
        tempArrRight = rightArr.copy()
        tempArrLeft = leftArr.copy()
        tempArrDown = downArr.copy()
        frontRules = frontRotationRules[0]
        
        #делаем фронт 
        i = 0
        j = 0
        while i<9:
            frontArr[j]=tempArrFront[frontRules[j]]
            j += 1
            i +=1

       
        
    #def testFunc(arr, b) -> None:
            
        
      
cube = Cube()
cube.printOUT()
arrayTest = [cube.front, cube.up, cube.right, cube.left, cube.down, cube.back]
cube.rotation(arrayTest[0],arrayTest[1],arrayTest[2],arrayTest[3],arrayTest[4],frontRotation,frontRotationRules)
print (arrayTest)  