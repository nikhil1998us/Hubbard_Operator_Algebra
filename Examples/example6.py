import hub_op


#sigmainverse is useful in summations over sigma. This can be used to find the other value in a summation over sigma


#obj=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{\sigma\leftarrow 0} X_{jN}^{-\sigma\leftarrow d}+X_{jN}^{\sigma\leftarrow 0} X_{iN}^{-\sigma\leftarrow d}]")
#obj=hub_op.lattoobj("X_{iN}^{0\leftarrow \sigma}[X_{iR}^{\sigma\leftarrow0}+\eta(\sigma)X_{iR}^{d\leftarrow-\sigma}]")
obj=hub_op.lattoobj("\eta(\sigma)X_{iR}^{d\leftarrow-\sigma}")
#obj=hub_op.lattoobj("X_{iN}^{\sigma\leftarrow 0} X_{jN}^{-\sigma\leftarrow d}")
#obj=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{\sigma\leftarrow 0}+X_{iN}^{-\sigma\leftarrow d}]")
print(str(obj),"\n")
obj.arrprint()
#testing inverse functionality for sigma to -sigma
obj.sigmainverse()
print("inverse is ",str(obj),"\n")