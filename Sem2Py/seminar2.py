# -*- coding: utf-8 -*-
import sys
import heapq


#################### DEFINITION OF CLASSES #####################################

class Point:    
    pointCounter = 0    
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.id = Point.pointCounter
        Point.pointCounter += 1
        self.partOf = set()        
    
    def assignToLine(self,line):
        self.partOf.add(line)
    
    def __repr__(self):
        return "( "+ "ID: " + str(self.id) +" " + str(self.x) + ", " + str(self.y) + ", " + str(self. color) +  " )"
    
    def __lt__(self,other):
        return self.x < other.x

class Line:
    def __init__(self,point1,point2):
        self.p1 = point1
        self.p2 = point2
        self.color = self._setColor()
        self.start = self._setStart()
        self.end = self._setEnd()
        
    def _setColor(self):
        try:            
            if self.p1.color == self.p2.color:
                return self.p1.color
            else:
                raise ValueError(" Point collors are not the same")
        except(ValueError,IndexError):
            exit("Could not produce right lines. Check code")
    
    def _setStart(self):
        if self.p1.x < self.p2.x:
            return self.p1
        else:
            return self.p2
    
    def _setEnd(self):
        if self.p1.x > self.p2.x:
            return self.p1
        else:
            return self.p2
    def __repr__(self):
        return "[" + str(self.p1) + "-->" + str(self.p2) + "]"

class Segment:
    def __init__(self,lineList, color):
        self.lines = lineList
        self.color = color
    
    def __repr__(self):
        return "{" + str(self.lines) + "}"

#class AVLtree:
#    
#    def __init__(self, valList = []):


#################### DEFINITION OF CLASSES #####################################

#################### DEFINITION OF FUNCTIONS #####################################
def createSegments(rawEntries):
    pointList = []
    lineList = []
    segmentList = []
    
    for point in rawEntries:        
        newPoint = Point(point[0],point[1],point[2])
        pointList.append(newPoint)
    
    i = 0
    while(i<len(pointList)-1):    
        p1 = pointList[i]
        p2 = pointList[i+1]
        if p1.color == p2.color:
            newLine = Line(p1,p2)
            lineList.append(newLine)
            p1.assignToLine(newLine)
            p2.assignToLine(newLine)
        i += 1
    
    currentSegment = []
    currentColor = None
    for line in lineList:
        if currentColor == None:
            currentColor = line.color    
        if currentColor == line.color:
            currentSegment.append(line)
        else:
            newSegment = Segment(currentSegment,currentColor)
            segmentList.append(newSegment)
            currentColor = line.color
            currentSegment = []
    newSegment = Segment(currentSegment,currentColor)
    segmentList.append(newSegment)
        
    
    return pointList, lineList, segmentList
#################### DEFINITION OF FUNCTIONS #####################################


################################### EXECUTION OF THE PROGRAM ############################
INPUT_FILE = sys.argv[1]
print("Input file: ", INPUT_FILE)

with open(INPUT_FILE) as file:
    l = file.readlines()
    for line in enumerate(l):        
        splitLine = line[1].split(",")        
        for ele in enumerate(splitLine):
            newEle = ele[1].strip()
            newEle = float(newEle)
            splitLine[ele[0]] = newEle        
        l[line[0]] = splitLine

#print(lines)
#print()
points, lines, segments = createSegments(l)
print("POINTS: ")
print(points)
print("########")
print("LINES: ")
print(lines)
print("########")
print("SEGMENTS: ")
print(segments)
print("########")

print("Line start and end points")
for l in lines:
    print(l," Start: ",l.start,"End: ", l.end)

print("Which lines is a point part of?")
for p in points:
    print("PointID :",p.id,"PartOf: ",p.partOf)

print("Pre heapify points: ")
print(points)
heapq.heapify(points)
print("After heapify points: ")
print(points)
x1 = heapq.heappop(points)
x2 = heapq.heappop(points)
print("Heap tests")
print(x1.partOf)
print(x2.partOf)
print("Type of points: ",type(points) )
print("After poping top heap points")
print(points)




################################### EXECUTION OF THE PROGRAM ############################





























    
        
    































