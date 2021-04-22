import os
import hub_op

if (not os.path.exists("LaTeX")):
    os.mkdir("LaTeX")

#variables for calculating zero energy terms etc changing these will change the zero energy terms
U=6
epsi=2.5

#Defining all the operators without sign and t terms
HtNi0=hub_op.lattoobj("[X_{iN}^{\sigma\leftarrow 0}X_{jN}^{0\leftarrow\sigma}+X_{iN}^{-\sigma\leftarrow d}X_{jN}^{d\leftarrow-\sigma}+X_{jN}^{\sigma\leftarrow 0}X_{iN}^{0\leftarrow\sigma}+X_{jN}^{-\sigma\leftarrow d}X_{iN}^{d\leftarrow-\sigma}]" )
print("HtNi0=",str(HtNi0),"\n")
HtNip=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{d\leftarrow-\sigma}X_{jN}^{0\leftarrow\sigma}+X_{jN}^{d\leftarrow-\sigma}X_{iN}^{0\leftarrow\sigma}]")
print("HtNip=",str(HtNip),"\n")
HtNim=hub_op.lattoobj("\eta(\sigma)[X_{iN}^{\sigma\leftarrow 0} X_{jN}^{-\sigma\leftarrow d}+X_{jN}^{\sigma\leftarrow 0} X_{iN}^{-\sigma\leftarrow d}]")
print("HtNim=",str(HtNim),"\n")
Htcr0p=hub_op.lattoobj("X_{iN}^{0\leftarrow \sigma}[X_{iR}^{\sigma\leftarrow0}+\eta(\sigma)X_{iR}^{d\leftarrow-\sigma}]")
print("Htcr0p=",str(Htcr0p),"\n")
Htcr0m=hub_op.lattoobj("X_{iN}^{\sigma\leftarrow 0}[X_{iR}^{0\leftarrow \sigma}+\eta(\sigma)X_{iR}^{-\sigma\leftarrow d}]")
print("Htcr0m=",str(Htcr0m),"\n")
Htcrpm=hub_op.lattoobj("X_{iN}^{d\leftarrow -\sigma}[X_{iR}^{-\sigma\leftarrow d}+\eta(\sigma)X_{iR}^{0\leftarrow \sigma}]")
print("Htcrpm=",str(Htcrpm),"\n")
Htcrmp=hub_op.lattoobj("X_{iN}^{-\sigma\leftarrow d}[X_{iR}^{d\leftarrow -\sigma}+\eta(\sigma)X_{iR}^{\sigma\leftarrow 0}]")
print("Htcrmp=",str(Htcrmp),"\n")
HtR=hub_op.lattoobj("[X_{iR}^{\sigma \leftarrow 0}+\eta(\sigma)X_{iR}^{d \leftarrow -\sigma}][X_{jR}^{0 \leftarrow \sigma}+\eta(\sigma)X_{jR}^{-\sigma \leftarrow d}]+ [X_{jR}^{\sigma \leftarrow 0}+\eta(\sigma)X_{jR}^{d \leftarrow -\sigma}][X_{iR}^{0 \leftarrow \sigma}+\eta(\sigma)X_{iR}^{-\sigma \leftarrow d}] ")
print("HtR=",str(HtR),"\n")
#compiling the arrays and their latex values these are the labels for the terms which stand for the Hubbard operator commutators
Htarr=[HtNi0,HtNip,HtNim,Htcr0p,Htcr0m,Htcrpm,Htcrmp,HtR]
Htlabarr=["\\hat{H}^{0}_{t,Ni}","\\hat{H}^{+}_{t,Ni}","\\hat{H}^{-}_{t,Ni}","\\hat{H}^{0\\oplus}_{t,cross}",
         "\\hat{H}^{0\\ominus}_{t,cross}","\\hat{H}^{+\\ominus}_{t,cross}","\\hat{H}^{-\\oplus}_{t,cross}","\\hat{H}^{}_{t,R}"]

#Energy cost for operation of each of these operators
HtEcost=[0,U,-U,epsi,-epsi,U-epsi,-U+epsi,0]
#flag for- if the operator can be the first operation on the ket; 1 stands for an impossible process
Htketflag=[0,0,1,0,0,0,1,0]
#print(Htlabarr)
print(len(Htlabarr),len(Htarr),len(HtEcost),len(Htketflag))
#HtR.arrprint()


#Doing derivation again with the recursive functions
Htarr=[HtNi0,HtNip,HtNim,Htcr0p,Htcr0m,Htcrpm,Htcrmp,HtR]
Htlabarr=["\\hat{H}^{0}_{t,Ni}","\\hat{H}^{+}_{t,Ni}","\\hat{H}^{-}_{t,Ni}","\\hat{H}^{0\\oplus}_{t,cross}",
         "\\hat{H}^{0\\ominus}_{t,cross}","\\hat{H}^{+\\ominus}_{t,cross}","\\hat{H}^{-\\oplus}_{t,cross}","\\hat{H}^{}_{t,R}"]

#Energy cost for operation of each of these operators
HtEcost=[0,U,-U,epsi,-epsi,U-epsi,-U+epsi,0]
#flag for if the operator can be the first operation on the ket 1 stands for a impossible process
Htketflag=[0,0,1,0,0,0,1,0]


#calculating two term commutator relations
term2labarr,term2arr,term2Ecost,term2Eketf=hub_op.higher_order_terms_calc(Htlabarr,Htarr,HtEcost,Htketflag)
term2_0Elabarr,term2_0Earr,term2_0Ecost,term2_0Eketf=hub_op.zeroEtermcalc(Htlabarr,Htarr,HtEcost,Htketflag)    

#writing to file and printing 2 term commutators
f=open("LaTeX/term_2_0E.txt","w")
for i in range(len(term2_0Elabarr)):
    #print("results are",term2_0Elabarr[i],"and term is",str(term2_0Earr[i]))
    f.write(hub_op.gen_print_string(term2_0Earr[i],term2_0Elabarr[i]))
f.close()
f=open("LaTeX/term_2_all.txt","w")
for i in range(len(term2labarr)):
    #print("results are",term2labarr[i],"and term is",str(term2arr[i]))
    f.write(hub_op.gen_print_string(term2arr[i],term2labarr[i]))
f.close()

#calculating 3 term commutators
term3labarr,term3arr,term3Ecost,term3Eketf=hub_op.higher_order_terms_calc(term2labarr,term2arr,term2Ecost,term2Eketf,Htlabarr,Htarr,HtEcost,Htketflag)
term3_0Elabarr,term3_0Earr,term3_0Ecost,term3_0Eketf=hub_op.zeroEtermcalc(term2labarr,term2arr,term2Ecost,term2Eketf,Htlabarr,Htarr,HtEcost,Htketflag)    

#writing to file and printing 3 term commutators
f=open("LaTeX/term_3_0E.txt","w")
for i in range(len(term3_0Elabarr)):
    #print("results are",term3_0Elabarr[i],"and term is",str(term3_0Earr[i]))
    f.write(hub_op.gen_print_string(term3_0Earr[i],term3_0Elabarr[i]))
f=open("LaTeX/term_3_all.txt","w")
for i in range(len(term3labarr)):
    #print("results are",term3labarr[i],"and term is",str(term3arr[i]))
    f.write(hub_op.gen_print_string(term3arr[i],term3labarr[i]))
f.close()

