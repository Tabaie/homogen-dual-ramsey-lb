from z3 import BitVecVal, ULE, Function, BoolSort, BitVecSort, ForAll, Bool, Solver, Const, Sort

one = BitVecVal(1, 2)
sort = BitVecSort(1)
f = Function("f", sort, BitVecSort(2))


x = Const("x", sort)
statement = ForAll(x, ULE(f(x), one))

s = Solver()
s.add(statement)
s.check()
print (s.model())