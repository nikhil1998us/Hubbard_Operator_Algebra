import hub_op


#Example showing how to use the commutator functionality
HtNi0=hub_op.lattoobj("[X_{iN}^{\sigma\leftarrow 0}X_{jN}^{0\leftarrow\sigma}+X_{iN}^{-\sigma\leftarrow d}X_{jN}^{d\leftarrow-\sigma}+X_{jN}^{\sigma\leftarrow 0}X_{iN}^{0\leftarrow\sigma}+X_{jN}^{-\sigma\leftarrow d}X_{iN}^{d\leftarrow-\sigma}]" )
print("HtNi0=",str(HtNi0),"\n")
HtR=hub_op.lattoobj("[X_{iR}^{\sigma \leftarrow 0}+\eta(\sigma)X_{iR}^{d \leftarrow -\sigma}][X_{jR}^{0 \leftarrow \sigma}+\eta(\sigma)X_{jR}^{-\sigma \leftarrow d}]+ [X_{jR}^{\sigma \leftarrow 0}+\eta(\sigma)X_{jR}^{d \leftarrow -\sigma}][X_{iR}^{0 \leftarrow \sigma}+\eta(\sigma)X_{iR}^{-\sigma \leftarrow d}] ")
print("HtR=",str(HtR),"\n")
comval=HtNi0.commute(HtR)
print("Raw commutator",comval,'\n')