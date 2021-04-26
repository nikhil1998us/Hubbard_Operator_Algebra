# Hubbard Operator Algebra
This library creates a python class defining Hubbard operators which are an alternative expression for Fock Space creation and anhilation Operators specifically defined on a lattice. It works on the LaTeX expression of the operators which is stored in a array like structure and can be used to calculate the sum, difference and product between any two operators and thereby their commutators. This can also been used to calculate all possible sets of commutators between two or more operators with another defined function in the library. 

The expressions which you obtain as result should be put into a LaTeX code interprester like TexStudio or overleaf to see the expression form.

To use the library add the script hub_op.py to the folder where you want to use the library. Now import the library using import hub_op and you will be able to use the functions in the library. See examples to see how the library can be used.

7 examples are provided to help with the usage of this library. 

* Example 1 shows a primitive method to make a Hubbard Operator. This is the way the Hubbard operators are stored by the program but there are better ways to do the same procedure.

* Example 2 shows how a LaTeX expression of Hubbard Operator can be taken as an input.

* Example 3 and 4 shows how to calculate a commutator of Hubbard Operators. Example 5 calculates a simple product between two Hubbard Operators

* Example 6 shows a function which can be used to do a summation over sigma.

* Example 7 is perhaps the most important. This might be all you need to use. Given a number of operators this program extensively calculates all possible commutators between any two terms. This process can be similarly extended to calculate even higher order terms. Code is also written to write these expressions to a txt file. This was manually interpreted using TexStudio to get the compiled expressions of the results.
