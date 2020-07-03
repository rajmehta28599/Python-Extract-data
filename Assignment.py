# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:33:54 2020

@author: Raj Mehta

Create a program in python to extract questions, multi choice options and answers from the attached test paper (Use of filters to remove garbage is must)

"""

q1="""
Q1 Which of the following is not a result of cell division?
(1) Growth (2) Repair (3) Metabolism (4) Reproduction"""

q2="""
Q2 Mark the incorrect pair
(1) Hydra – Budding (2) Flatworm – Regeneration
(3) Amoeba – Fragmentation (4) Yeast – Budding"""

q3="""
Q3 Which of the following is incorrect for reproduction?
(1) Unicellular organisms reproduce by cell division
(2) Reproduction is a characteristic of all living organisms
(3) In unicellular organisms, reproduction and growth are linked together
(4) Non-living objects are incapable of reproducing
"""

q4="""
Q4 Mark the incorrect statement w.r.t. metabolism.
(1) Microbes exhibit the metabolism
(2) It is the property of all living forms
(3) The metabolic reactions can be demonstrated in-vitro
(4) It is not a defining feature of life forms
"""

q5="""
Q5 Non-living objects exhibit/show
(1) Property of self-replication (2) Evolution
(3) Self-regulating interactive systems (4) Reversible growth"""

q6="""
Q6 Which statement is false about the growth shown by non-living objects?
(1) The growth occurs from outside
(2) The growth is reversible
(3) The growth is due to the accumulation of material on the surface
(4) The growth is intrinsic"""

q7="""
Q7 Local names of various plants and animals
(1) Help in recognizing organisms worldwide (2) Are used universally
(3) Are specific and distinct names (4) Vary from place to place
"""
que={q1:"3",q2:"3",q3:"2",q4:"4",q5:"4",q6:"4",q7:"4"}

print("Questions and Answers")
marks=0
for i in que:
    print(i)
    ans=input("Enter Answer 1/2/3/4 : ")
    if ans ==que[i]:
        print("Correst Answer")
        marks=marks+1
    else:
        print("Wrong Answer")
        marks=marks
print("Total Marks is : ",marks)
