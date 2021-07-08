from z3 import BitVecSort, Function, ForAll, Const, ULE, And, Extract, BitVecVal
from colors import ColorInfo

class FunctionInfo:

    @staticmethod
    def aggregateAnd(rules):
        aggregate = True
        for rule in rules:
            aggregate = And(aggregate, rule)
        return aggregate

    def __init__(self, declaration, rulesFreeVar, rules):
        self.declaration = declaration
        self.rule = ForAll(rulesFreeVar, FunctionInfo.aggregateAnd(rules))

#Currently to describe an equivalence class, we ascribe classes to objects, should it be ascribing objects to classes?
#This takes mlogk / mlogl space whearas the other would take mlogm space, which is larger. However, it might be that we can have
#       more search space reducing heuristics like 1) requiring any equivalence class' objects to be listed in ascending order
#       or that 2) the first element of an equivalence class be the smallest element not yet assigned
#   Would (2) be okay? To only consider isomorphism classes of equivalence relations? Probably not

#coarseColoring = Function("coarseColoring", BoolVector("dummyCoarseEquivRel", coarseEquivClassRelSize).sort(), BitVecto)

class EquivRelInfo:

    @staticmethod
    def bitCount(elementsCount):
        return (elementsCount-1).bit_length()

    def __init__(self, objCount, classCount, colorInfo, namePrefix):
        self.classCount = classCount
        self.fullSize = EquivRelInfo.bitCount(classCount) * objCount
        self.objPerClass = objCount / classCount
        #Optimization: Always assuming that object number 0 is assigned to equivalence class number 0. Is that okay?
        self.compactSize = (classCount-1).bit_length() * (objCount-2) #The first object is interpreted to be in class 0. The last object is interpreted to have whatever class remains not full.
        self.compactSort = BitVecSort(max(1, self.compactSize))
        self.fullSort = BitVecSort(self.fullSize)
        self.coloring = Function(namePrefix + "Coloring", self.compactSort, colorInfo.sort)
        self.namePrefix = namePrefix
        
    def computeColoringRule(self, colorInfo):
        coloringRuleFreeVar = Const(self.namePrefix + "EquivRelColoringRuleFreeVar", self.compactSort) #TODO: Abusing const like this is cringy, learn how to do this with var
        return ForAll(
            coloringRuleFreeVar,
            ULE ( self.coloring(coloringRuleFreeVar), colorInfo.max)
        )
    
    #Expand the description of an equivalence class from m-2 entries up to m
    def computeExpansionFunction(self):
        expansionFunction = Function(self.namePrefix + "EquivRelExpansionFunction", self.compactSort, self.fullSort)
        x = Const(self.namePrefix + "EquivRelExpansionFunctionRulesFreeVar", self.compactSort)
        expanded = expansionFunction(x)

        #Is this simpler logic than actual counting?
        #desiredSum = 
        #sumBitCount = 

        #rules = And( x == expansionFunction(x) )

        #return FunctionInfo(expansionFunction, x, rules)

    def computeArrangeByClassFunctions(self):

        objLen = (self.classCount * self.objPerClass - 1).bit_length()
        x = Const(self.namePrefix + "EquivRelArrangeByClassFunctionRulesFreeVar", self.compactSort)
        arrangeByClassFunctions = [[
             Function(
                self.namePrefix + "EquivRelObject" + objectIndex + "ofClass" + classIndex + "Function",
                self.compactSort,
                BitVecSort(objLen)
                 ) for objectIndex in range(self.objPerClass)
        ] for classIndex in range(self.classCount)]

        consistencyRules = 
        [[
            
        for objectIndex in range(self.objPerClass)] for classIndex in range(self.classCount)]

        zeroOfZeroRule = arrangeByClassFunctions[0][0](x) == BitVecVal(0, objLen)


        

