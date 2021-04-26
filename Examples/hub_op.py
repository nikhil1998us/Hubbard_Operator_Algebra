
import collections


#helper functions
def compare_list(a,b):
    return collections.Counter(a)==collections.Counter(b)

#compare list test
'''
a=[1,2,3,"test"]
b=[3,"test ",1,2]
print(compare_list(a,b))
'''

#helper func to simplify expressions
def removecoeffs(txt):
    sgn1="\\eta(\\sigma)"
    sgn1count=0
    sgn2="\\eta(-\\sigma)"
    sgn2count=0
    txt=txt.replace(" ","")
    flag=-1
    while(len(txt)>0):
        if(txt.find(sgn1)==0):
            txt=txt[len(sgn1):]
            sgn1count+=1
            flag=0
        elif(txt.find(sgn2)==0):
            txt=txt[len(sgn2):]
            sgn2count+=1
            flag=1
        else:
            print("unknown error")
    #if return is 0 indicates + for 2nd arr element below, first ele is coeff string
    #if return is 1 indicates - or sign change
    if(flag==-1):
        return [txt,0]
    elif(((sgn1count+sgn2count)%2)==0):
        return ["",((sgn1count%2)+(sgn2count%2))//2]
    elif(flag==0):
        return [sgn1,(((sgn1count-1)%2)+(sgn2count%2))//2]
    else:
        return [sgn1,1-(((sgn2count-1)%2)+(sgn1count%2))//2]
#Selection sort
def sort(arr):
    for i in range(len(arr)-1):
        minv=arr[i]
        pos=i
        for j in range(i,len(arr)):
            if(arr[j]<minv):
                minv=arr[j]
                pos=j
        arr[pos]=arr[i]
        arr[i]=minv
    return arr
    
    
    

#The hubbard operator class initialized from latex code of Hubbard operators 
#and can be used to perform operations like commutation on these operators and gives the result in latex.
class Hub_op:
    #variables below breakdown the storage of the latex operators into easily usable forms
    zeroflag=0
    sign=["+"]
    coeff=[""]
    label=[[""]]
    brav=[[-1]]
    ketv=[[-1]]
    #default constructor
    def __init__(self,sign,coeff,label,brav,ketv):
        #test code
        '''
        for i in range(len(coeff)):
            if(coeff[i].find("(\\sigma)+")!=-1):
                print("Init occured here with vars ",sign,coeff,label,brav,ketv)
        '''
        self.sign=sign
        for i in range(len(label)):
            coeff[i]=coeff[i].replace(" ","")
            for j in range(len(label[i])):
                label[i][j]=label[i][j].replace(" ","")
                brav[i][j]=brav[i][j].replace(" ","")
                ketv[i][j]=ketv[i][j].replace(" ","")
        self.coeff=coeff
        self.label=label
        self.brav=brav
        self.ketv=ketv
    #used to initialize search on certain terms to find out certain properties and pairings.
    def search_term(self,label,brav,ketv):
        #not optimized for duplicate searching
        posarr=[]
        for i in range(len(self.label)):
            for j in range(len(self.label[i])):
                flagarr=[0]*len(label)
                flag=1
                for k in range(len(label)):
                    if(label[k]==self.label[i][j] and brav[k]==self.brav[i][j] and ketv[k]==self.ketv[i][j]):
                        flagarr[k]=1
                for k in range(len(flagarr)):
                    if(flagarr[k]==0):
                        flag=0
                        break
                if(flag==1):
                    posarr.append(i)
        return posarr
    #bug fix testing function
    def verify(self):
        for i in range(len(self.coeff)):
            if(self.coeff[i].find("(\\sigma)+")!=-1):
                print("wrong value occured here with vars ",self.sign,self.coeff,self.label,self.brav,self.ketv)
    #simplifies A+B-A to B
    def docancels(self):
        cancellist=[]
        for i in range(len(self.label)):
            zippedi=[tuple(zip(self.label[i][k],self.brav[i][k],self.ketv[i][k]))for k in range(len(self.label[i]))]
            for j in range(len(self.label)):
                zippedj=[tuple(zip(self.label[j][k],self.brav[j][k],self.ketv[j][k]))for k in range(len(self.label[j]))]
                if(compare_list(zippedi,zippedj)and self.coeff[i].replace(" ","")==self.coeff[j].replace(" ","") and self.sign[i]!=self.sign[j]):
                    cancellist.append(i)
                    cancellist.append(j)
                    self.label[i]=["0"]
                    self.brav[i]=[""]
                    self.ketv[i]=[""]
                    self.sign[i]="+"
                    self.coeff[i]=""
                    self.label[j]=["0"]
                    self.brav[j]=[""]
                    self.ketv[j]=[""]
                    self.sign[j]="+"
                    self.coeff[j]=""
                    zippedi=[tuple(zip(self.label[i][k],self.brav[i][k],self.ketv[i][k]))for k in range(len(self.label[i]))]
        cancellist=sort(cancellist)
        if(len(cancellist)!=0):
            for i in range(len(cancellist)-1):
                if(cancellist[i]==cancellist[i+1]):
                    print("repeated cancel at",cancelllist[i])
        nlabel=[]
        ncoeff=[]
        nsign=[]
        nbrav=[]
        nketv=[]
        for i in range(len(self.label)):
            if not(self.label[i]==["0"] and self.brav[i]==[""] and self.ketv[i]==[""] and self.sign[i]=="+" and self.coeff[i]==""):
                nlabel.append(self.label[i])
                ncoeff.append(self.coeff[i])
                nsign.append(self.sign[i])
                nbrav.append(self.brav[i])
                nketv.append(self.ketv[i])
        retobj=Hub_op(nsign,ncoeff,nlabel,nbrav,nketv)
        if(len(retobj.label)==0):
            retobj.zeroflag=1
        self=retobj
        return retobj    
    #storing coefficients
    def coeffmult(self,univcoeff):
        for i in range(len(self.coeff)):
            self.coeff[i]+=univcoeff
    #inverts the spin of all operators in the expression. Useful if there is a summation over sigma
    def sigmainverse(self):
        invobj=Hub_op(self.sign[:],self.coeff[:],[x[:] for x in self.label],[x[:] for x in self.brav],[x[:] for x in self.ketv])
        for i in range(len(invobj.brav)):
            for j in range(len(invobj.brav[i])):
                if(invobj.brav[i][j].find("-")!=-1):
                    invobj.brav[i][j]=invobj.brav[i][j].replace("-\\sigma","\\sigma")
                else:
                    invobj.brav[i][j]=invobj.brav[i][j].replace("\\sigma","-\\sigma")
                if(invobj.ketv[i][j].find("-")!=-1):
                    invobj.ketv[i][j]=invobj.ketv[i][j].replace("-\\sigma","\\sigma")
                else:
                    invobj.ketv[i][j]=invobj.ketv[i][j].replace("\\sigma","-\\sigma")
            invobj.coeff[i]=invobj.coeff[i].replace("-\\sigma","dummy")
            invobj.coeff[i]=invobj.coeff[i].replace("\\sigma","-\\sigma")
            invobj.coeff[i]=invobj.coeff[i].replace("dummy","\\sigma")
        return invobj
    #returns negative object, see __neg__ which makes this work for -(A+B) to return -A-B
    def invert_sign(self):
        mod_sign=[]
        for i in range(len(self.sign)):
            if(self.sign[i]=="+"):
                mod_sign.append("-")
            else:
                mod_sign.append("+")
        inverted=Hub_op(mod_sign,self.coeff[:],[x[:] for x in self.label],[x[:] for x in self.brav],[x[:] for x in self.ketv])
        return inverted
    #test helper function
    def arrprint(self):
        print("zeroflag",self.zeroflag)
        print("sign",self.sign)
        print("coeff",self.coeff)
        print("label",self.label)
        print("brav",self.brav)
        print("ketv",self.ketv)
    #returns commutator A.commute(B) returns computed value of [A,B] as a new object
    def commute(self,obj):
        obji=obj.sigmainverse()
        return self*(obj+obji)-(obj+obji)*self
    #simplifies the repeated eta in the coefficients. Nothing else is supported. Only eta simplification
    def coeffsimplify(self):
        for i in range(len(self.coeff)):
            newcoeff,flag=removecoeffs(self.coeff[i])
            self.coeff[i]=newcoeff
            if(flag):
                #print("Did coeff simplify")
                if(self.sign[i]=="+"):
                    self.sign[i]="-"
                else:
                    self.sign[i]="+"
        newobj=self.docancels()
        return newobj
    #returns the latex code for the Hubbard operator object   
    def __str__(self):
        strv=""
        if(self.zeroflag):
            strv+="0"
            return strv
        for i in range(len(self.label)):
            strv+=self.sign[i]
            strv+=self.coeff[i]
            for j in range(len(self.label[i])):
                strv+="X_{"+self.label[i][j]+"}^{"+self.brav[i][j]+" \\leftarrow "+self.ketv[i][j]+"}"
        return strv
    #Adds two Hubbard operators and returns new object which is sum of two Hubbard operators
    def __add__(self,other):
        if(self.zeroflag):
            return other
        elif(other.zeroflag):
            return self
        nsign=self.sign+other.sign
        ncoeff=self.coeff+other.coeff
        nlabel=self.label+other.label
        nbrav=self.brav+other.brav
        nketv=self.ketv+other.ketv
        uncancelledobj=Hub_op(nsign,ncoeff,nlabel,nbrav,nketv)
        cancelledobj=uncancelledobj.docancels()
        return cancelledobj
    #negative of object
    def __neg__(self):
        return self.invert_sign()
    #implements subtraction
    def __sub__(self,other):
        if(self.zeroflag):
            neg=other
            if(other.zeroflag==0):
                neg=other.invert_sign()
            return neg
        elif(other.zeroflag):
            return self
        neg=other.invert_sign()
        return self+neg
    #implements product
    def __mul__(self,other):
        if(self.zeroflag==1):
            #print("zero flagged")
            return self
        elif(other.zeroflag==1):
            #print("zero flagged")
            return other
        sgarr1=self.sign
        cfarr1=self.coeff
        lbarr1=self.label
        braarr1=self.brav
        ketarr1=self.ketv
        sgarr2=other.sign
        cfarr2=other.coeff
        lbarr2=other.label
        braarr2=other.brav
        ketarr2=other.ketv
        ls=len(self.label)
        lo=len(other.label)
        nsign=[]
        ncoeff=[]
        nlabel=[]
        nbrav=[]
        nketv=[]
        for i in range(ls):
            for j in range(lo):
                #test code for functionality
                '''
                print("Running i",i,"j",j)
                print("Making obj1 from",sgarr1[i],"|",cfarr1[i],"|",lbarr1[i],"|",braarr1[i],"|",ketarr1[i])
                print("Making obj2 from",sgarr2[j],"|",cfarr2[j],"|",lbarr2[j],"|",braarr2[j],"|",ketarr2[j])
                tempobj1=Hub_op([sgarr1[i]],[cfarr1[i]],[lbarr1[i]],[braarr1[i]],[ketarr1[i]])
                tempobj2=Hub_op([sgarr2[j]],[cfarr2[j]],[lbarr2[j]],[braarr2[j]],[ketarr2[j]])
                print("Comparing",str(tempobj1),"and",str(tempobj2))
                '''
                flag=1
                tcoeff=""
                tcoeff+=cfarr1[i]+cfarr2[j]
                #print("tcoeff=",tcoeff)
                tlabel=[]
                tbrav=[]
                tketv=[]
                complete=[]
                for pos1 in range(len(lbarr1[i])):
                    v=lbarr1[i][pos1]
                    #print("comparing first arrays v",v,"at pos",pos1)
                    braketmatchflag=0
                    if v in lbarr2[j]:
                        pos2=lbarr2[j].index(v)
                        #print("found in 2nd array at",pos2)
                        complete.append(pos2)
                        if(ketarr1[i][pos1].replace(" ","")==braarr2[j][pos2].replace(" ","")):
                            braketmatchflag=1
                            #print("bra ket match")
                            tlabel.append(v)
                            tbrav.append(braarr1[i][pos1])
                            tketv.append(ketarr2[j][pos2])
                        else:
                            #print("bra ket mismatch|",ketarr1[i][pos1],"|and|",braarr2[j][pos2],"|")
                            flag=0
                            break
                    else:
                        tlabel.append(v)
                        tbrav.append(braarr1[i][pos1])
                        tketv.append(ketarr1[i][pos1])
                for pos2 in range(len(lbarr2[j])):
                    if(not(pos2 in complete)):
                        tlabel.append(lbarr2[j][pos2])
                        tbrav.append(braarr2[j][pos2])
                        tketv.append(ketarr2[j][pos2])
                if(flag):
                    if(sgarr1[i]==sgarr2[j]):
                        nsign.append("+")
                    else:
                        nsign.append("-")
                    ncoeff.append(tcoeff)
                    nlabel.append(tlabel)
                    nbrav.append(tbrav)
                    nketv.append(tketv)
        retobj=Hub_op(nsign,ncoeff,nlabel,nbrav,nketv)
        if(len(retobj.label)==0):
            retobj.zeroflag=1
        return retobj
                        
                        
  
#finds position of end of first set of square brackets. Helps decompose to objects easier
def bracketzerodepth(stringv):
    if(stringv.find("X")==-1):
        print("No hubbard operators encountered in depth calc")
    depth=0
    start=0
    end=-1
    for i in range(len(stringv)):
        if(stringv[i]=="["):
            depth+=1
            if(depth==1):
                start=i
        elif(stringv[i]=="]"):
            depth-=1
            if(depth==0):
                end=i
        if(depth==0 and stringv[i]=="]"):
            if(stringv[start:end].find("X")==-1 and end!=-1):
                bracketzerodepth(stringv[end+1:])
            return end
    return -1
    
    
# only left side coefficients are detected by this function
#converts a simple latex expression with a single Hubbard operator to an object
def simplestrtoobj(stringv):
    #print("running simplestr algo on",stringv)
    startbracket=stringv.find("[")
    if(startbracket==-1):
        startbracket=len(stringv)
    coeffpos=min(stringv.find("X"),startbracket)
    substartpos=stringv.find("{",coeffpos)
    subendpos=stringv.find("}",substartpos)
    brastartpos=stringv.find("{",subendpos)
    braendpos=stringv.find("\\left",brastartpos)
    ketstartpos=stringv.find("w",braendpos)
    ketendpos=stringv.find("}",ketstartpos)
    endcoeffpos=max(ketendpos,bracketzerodepth(stringv))
    endcoeff=stringv[endcoeffpos+1:]
    coeff=stringv[0:coeffpos]
    sign="+"
    if(len(coeff)>0):
        if(coeff[0]=="+"):
            coeff=coeff[1:]
            sign="+"
        elif(coeff[0]=="-"):
            coeff=coeff[1:]
            sign="-"
    coeff+=endcoeff
    objv=Hub_op([sign],[coeff],[[stringv[substartpos+1:subendpos]]],[[stringv[brastartpos+1:braendpos]]],[[stringv[ketstartpos+1:ketendpos]]])
    return objv
#checks if there is just one Hubbard operator in the expression
def checksimplestr(stringv):
    xcount=0
    for i in range(len(stringv)):
        if(stringv[i]=='X'):
            xcount+=1
    return (xcount<=1)
    
    
    

#converts latex code to an object and simplifies the coefficients
def lattoobj(stringv):
    val=latextoobj(stringv)
    val=val.coeffsimplify()
    return val
#converts latex code to an object without simplifying the coefficients
def latextoobj(stringv):
    tempobj=""
    univcoeff=""
    bigobj=Hub_op(["+"],[""],[["testobj"]],[["0"]],[["0"]])
    flag=0
    depth=0
    start=0
    end=-1
    #If it has just a single Hubbard operator
    if(checksimplestr(stringv)):
        return simplestrtoobj(stringv)
    #splitting SoP form
    for i in range(len(stringv)):
        if(stringv[i]=="["):
            depth+=1
        elif(stringv[i]=="]"):
            depth-=1
        if((depth==0 and stringv[i]=='+' and i!=0)or(flag==1 and i==len(stringv)-1)):
            #print("Running addition split on",stringv)
            if(i==len(stringv)-1):
                i+=1
            flag=1
            substrv=stringv[start:i]
            start=i+1
            tempobj=lattoobj(substrv)
            '''
            tempobj.arrprint()
            print()
            print("bigobj,label",bigobj.label)
            bigobj.arrprint()
            '''
            if(bigobj.label[0][0]=="testobj"):
                bigobj=tempobj
            else:
                bigobj=bigobj+tempobj
            #print("tempobj",tempobj,"\n")
            #print("bigobj",bigobj,"\n")
    #if split by addition marks then result is recursively calculated already
    if(flag):
        #print("bigobj before return",bigobj,"\n")
        return bigobj
    #Now we check if it is in PoS form and split the terms
    depth=0
    start=0
    execflag=0
    for i in range(len(stringv)):
        if(stringv[i]=="["):
            depth+=1
        elif(stringv[i]=="]"):
            depth-=1
        if(depth==0 and stringv[i]=="X"):
            #print("Running mult split no brackets on ",stringv,"\n")
            execflag=1
            if(i!=0):
                univcoeff=stringv[:i]
                start=i
            #make sure that it is escape char if needed check
            end=stringv.find("}",stringv.find("\\leftarrow"))
            #print("first string",stringv[start:end+1])
            obj1=simplestrtoobj(stringv[start:end+1])
            obj2=lattoobj(stringv[end+1:])
            '''
            print("tHE OBjects are obj1",str(obj1),"\n \n obj2",str(obj2),"\n")
            print("with details obj1")
            obj1.arrprint()
            print("with details obj2")
            obj2.arrprint()
            print()
            '''
            bigobj=obj1*obj2
            break
        if(depth==1 and stringv[i]=="["):
            #print("Running mult split with brackets on",stringv,"\n")
            execflag=1
            if(i!=0):
                univcoeff=stringv[:i]
            end=bracketzerodepth(stringv)
            obj1=lattoobj(stringv[i+1:end])
            '''
            print("obj1 in mult",str(obj1),"\n")
            print("with details obj1")
            obj1.arrprint()
            '''
            if(end>len(stringv)-3 and end<len(stringv)+3):
                bigobj=obj1
            else:
                #print("long string is",stringv[end+1:])
                obj2=lattoobj(stringv[end+1:])
                '''
                print("obj2 in mult",str(obj2),"\n")
                print("with details obj2")
                obj2.arrprint()
                '''
                bigobj=obj1*obj2
            break
    if(execflag==0):
        print("Unknown error encountered")
    #print("univcoeff",univcoeff)
    bigobj.coeffmult(univcoeff)
    #print("Bigobj result ",str(bigobj),"\n")
    return bigobj





#calculating higher order terms from same array commutation with itself or two different arrays
def higher_order_terms_calc(ltermtxt,ltermval,ltermcost,ltermketf,lltermtxt=[],lltermval=[],lltermcost=[],lltermketf=[]):
    htermtxt=[]
    htermval=[]
    htermEcost=[]
    htermketf=[]
    if(len(lltermtxt)==0):
        for i in range(len(ltermval)-1):
            for j in range(i+1,len(ltermval)):
                commutator=ltermval[i].commute(ltermval[j])
                commutator=commutator.coeffsimplify()
                htermtxt.append("["+ltermtxt[i]+","+ltermtxt[j]+"]")
                htermval.append(commutator)
                htermEcost.append(ltermcost[i]+ltermcost[j])
                if(ltermketf[i]==1 or ltermketf[j]==1):
                    htermketf.append(1)
                else:
                    htermketf.append(0)
    else:
        for i in range(len(ltermval)):
            for j in range(len(lltermval)):
                commutator=ltermval[i].commute(lltermval[j])
                commutator=commutator.coeffsimplify()
                htermtxt.append("["+ltermtxt[i]+","+lltermtxt[j]+"]")
                htermval.append(commutator)
                htermEcost.append(ltermcost[i]+lltermcost[j])
                if(ltermketf[i]==1 or lltermketf[j]==1):
                    htermketf.append(1)
                else:
                    htermketf.append(0)
    return htermtxt,htermval,htermEcost,htermketf
#calculating terms which have zero Energy from the commutation relations
def zeroEtermcalc(ltermtxt,ltermval,ltermcost,ltermketf,lltermtxt=[],lltermval=[],lltermcost=[],lltermketf=[]):
    htermzeroEtxt=[]
    htermzeroEval=[]
    htermzeroEEcost=[]
    htermzeroEketf=[]
    if(len(lltermtxt)==0):
        for i in range(len(ltermval)-1):
            for j in range(i+1,len(ltermval)):
                if(ltermcost[i]+ltermcost[j]==0):
                    if(ltermketf[i]==0 and ltermketf[j]==0):
                        commutator=ltermval[i].commute(ltermval[j])
                    elif(ltermketf[i]==0 and ltermketf[j]==1):
                        commutator=-(ltermval[j]+ltermval[j].sigmainverse())*ltermval[i]
                    elif(ltermketf[i]==1 and ltermketf[j]==0):
                        commutator=ltermval[i]*(ltermval[j]+ltermval[j].sigmainverse())
                    else:
                        commutator=Hub_op("+","","","","")
                        commutator.zeroflag=1
                    commutator=commutator.coeffsimplify()
                    htermzeroEtxt.append("["+ltermtxt[i]+","+ltermtxt[j]+"]")
                    htermzeroEval.append(commutator)
                    htermzeroEEcost.append(ltermcost[i]+ltermcost[j])
                    htermzeroEketf.append(0)
    else:
        for i in range(len(ltermval)):
            for j in range(len(lltermval)):
                if(ltermcost[i]+lltermcost[j]==0):
                    if(ltermketf[i]==0 and lltermketf[j]==0):
                        commutator=ltermval[i].commute(lltermval[j])
                    elif(ltermketf[i]==0 and lltermketf[j]==1):
                        commutator=-(lltermval[j]+lltermval[j].sigmainverse())*ltermval[i]
                    elif(lltermketf[j]==0 and ltermketf[i]==1):
                        commutator=ltermval[i]*(lltermval[j]+lltermval[j].sigmainverse())
                    else:
                        commutator=Hub_op("+","","","","")
                        commutator.zeroflag=1
                    commutator=commutator.coeffsimplify()
                    htermzeroEtxt.append("["+ltermtxt[i]+","+lltermtxt[j]+"]")
                    htermzeroEval.append(commutator)
                    htermzeroEEcost.append(ltermcost[i]+lltermcost[j])
                    htermzeroEketf.append(0)
    return htermzeroEtxt,htermzeroEval,htermzeroEEcost,htermzeroEketf

#function to generate the latex code to print a Hubbard operator in LaTeX to a txt file
def gen_print_string(term,termlab):
    #adding prefix and suffix for aligning the latex code
    fulltext="\\begin{align}\n\\nonumber"+termlab+"=&"+str(term)+"\\\\ \\nonumber \n\\end{align} \n"
    #string to help split long latex operations into the next line
    inserttxt="\\\\ \\nonumber &"
    posadd=[]
    count=0
    for it in range(len(fulltext)):
        if(fulltext[it]=="+" and not(fulltext[it:].replace(" ","").find("+\\ominus")==0 or fulltext[it:].replace(" ","").find("+}")==0)):
            count+=1
        elif(fulltext[it:].replace(" ","").find("-\\eta")==0):
            count+=1
        elif(fulltext[it:].replace(" ","").find("-X")==0):
            count+=1
        if(count==2):
            posadd.append(it)
            count=0
    newfulltext=""
    prevpos=0
    for it in range(len(posadd)):
        newfulltext+=fulltext[prevpos:posadd[it]]+inserttxt
        prevpos=posadd[it]
    newfulltext+=fulltext[prevpos:]
    return newfulltext



