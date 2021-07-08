from z3 import  Bool, Function, Sort, BitVecs, BitVecSort, Solver, ForAll, Var, BitVecVal, ULE, Const, BoolSort, And
from equiv_rel_sorts_obj2class import EquivRelInfo
from colors import ColorInfo
#The name Object to Class means that equivalence relations are specified by assigning to each 

k = 1 #Number of classes in equivalence relations
N = 2 #Number of colors
m = 2 #Number of objects

l = 2 #Number of classes in the witness "fine" equivalence class

colorInfo = ColorInfo(N)
coarseEquivRels = EquivRelInfo(m, k, colorInfo, "coarse")
fineEquivRels = EquivRelInfo(m, l, colorInfo, "fine")

s = Solver()

#Limit colors
s.add(coarseEquivRels.computeColoringRule(colorInfo), fineEquivRels.computeColoringRule(colorInfo))

coarseEquivRelExpansion = Function("coarseEquivRelExpansion", coarseEquivRelSort, coarseEquivRelFullSort)
fineEquivRelExpansion = Function("fineEquivRelExpansion", fineEquivRelSort, fineEquivRelFu)

print("Done")