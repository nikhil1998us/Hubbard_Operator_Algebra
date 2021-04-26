import hub_op


#The code converts the array form in which the Hubbard operators are stored to LaTeX
test=hub_op.Hub_op(["+"],["\eta{\sigma}"],[["iN"]],[["0"]],[["d"]])
test2=hub_op.Hub_op(["+"],[""],[["iN"]],[["d"]],[["0"]])
test3=hub_op.Hub_op(["+"],[""],[["iR"]],[["d"]],[["0"]])
sumv=test+test2
print("Result",str(test))
print("Result",str(test2))
print("test3",str(test3))
print("sum",str(sumv))
prodv=test*test2*test3
print("prod",str(prodv))
diffv=test-test2
print("diff",diffv)
print("Inverse of test",str(test.sigmainverse()))