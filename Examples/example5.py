import hub_op


#Testing the product of two Hubbard Operators
val1=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{d\leftarrow-\sigma}X_{jN}^{0\leftarrow\sigma}+X_{jN}^{d\leftarrow-\sigma}X_{iN}^{0\leftarrow\sigma}]")
val2=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{\sigma\leftarrow 0} X_{jN}^{-\sigma\leftarrow d}+X_{jN}^{\sigma\leftarrow 0} X_{iN}^{-\sigma\leftarrow d}]")
print("\n")
print("val1",str(val1),"\n")
val1.arrprint()
print()
print("val2",str(val2),"\n")
val2.arrprint()
print("\n")
testv=val2*val1
print("\n")
print("testvalue",str(testv),"\n")