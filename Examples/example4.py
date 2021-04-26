import hub_op


#Another example of calculating the commutator and simplifying the coefficients of eta(sigma)
HtNip=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{d\leftarrow-\sigma}X_{jN}^{0\leftarrow\sigma}+X_{jN}^{d\leftarrow-\sigma}X_{iN}^{0\leftarrow\sigma}]")
print("HtNip=",str(HtNip),"\n")
HtNim=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{\sigma\leftarrow 0} X_{jN}^{-\sigma\leftarrow d}+X_{jN}^{\sigma\leftarrow 0} X_{iN}^{-\sigma\leftarrow d}]")
print("HtNim=",str(HtNim),"\n")
comval=HtNip.commute(HtNim)
print("Raw commutator",comval,'\n')
comval=comval.coeffsimplify()
print("Simplified to ",comval,"\n")