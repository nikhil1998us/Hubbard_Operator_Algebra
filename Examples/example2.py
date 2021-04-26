import hub_op

#Converts a simple latex expression of Hubbard operator to the array form
objvt=hub_op.simplestrtoobj("-\eta(\sigma)X_{iR}^{d \leftarrow -\sigma}")
print(str(objvt))
objvt.arrprint()