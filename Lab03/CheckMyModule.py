# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:07:56 2020

@author: blraj
Reg.no : 2047120
Course : MCS173 - lAB03
MSC.Cs - 1st Year
"""

import MyModule

auth="*"*40
eqsym="="*50
minsym="-"*18


print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
print("*\t\tName   : Rajkumar B L\t\t   *")
print("*\t\tReg.no : 2047120\t\t\t   *")
print("*\t\tCourse : MCS173 - lAB03\t\t   *")
print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")



#%%

#Execution of Reverse Compliment DNA Function
 
print(eqsym+"\n\tRunning Function  - Reverse Compliment DNA\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> reversecompliment_DNA(\"GTCA\")")
print("\tResult --> "+MyModule.reversecompliment_DNA("GTCA"))

print("\nCase 02:\n\tFunc   --> reversecompliment_DNA(\"TG AC\")")
print("\tResult --> "+MyModule.reversecompliment_DNA("TG AC"))

print("\nCase 03:\n\tFunc   --> reversecompliment_DNA(\"GTACTGCTATCATTTACCC\")")
print("\tResult --> "+MyModule.reversecompliment_DNA("GTACTGCTATCATTTACCC"))

print("\nCase 04:\n\tFunc   --> reversecompliment_DNA(\"GTCA invalid input\")")
print("\tResult --> "+MyModule.reversecompliment_DNA("GTCA invalid input"))
print("\n"+minsym+"  END FUNC 01 "+minsym+"\n")


#%%


#%%

#Execution of Chicking if number is pronic Function
 
print("\n"+eqsym+"\n\t\tRunning Function  - Check If Pronic\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> check_if_pronic(2)")
print("\tResult --> "+MyModule.check_if_pronic(2))

print("\nCase 02:\n\tFunc   --> check_if_pronic(44)")
print("\tResult --> "+MyModule.check_if_pronic(44))

print("\nCase 03:\n\tFunc   --> check_if_pronic(72)")
print("\tResult --> "+MyModule.check_if_pronic(72))

print("\nCase 04:\n\tFunc   --> check_if_pronic(86)")
print("\tResult --> "+MyModule.check_if_pronic(86))

print("\n"+minsym+"  END FUNC 02 "+minsym+"\n")


#%%


#%%

#Execution of Encoding (String --> Morse Code)
 
print("\n"+eqsym+"\n  Running Function  - Encode (Str -> Morse Code\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> encode(\"Hey this is Raj here. Happy day.\")")
print("\tResult --> "+MyModule.encode("Hey this is Raj here. Happy day."))

print("\nCase 02:\n\tFunc   --> encode(\"Hello world\")")
print("\tResult --> "+MyModule.encode("Hello world"))

print("\nCase 03:\n\tFunc   --> encode(\"MCS173 - Python Lab03\")")
print("\tResult --> "+MyModule.encode("MCS173 - Python Lab03"))

print("\nCase 04:\n\tFunc   --> encode(\"Invalid input --> *&--09**#$\")")
print("\tResult --> "+MyModule.encode("Invalid input --> *&--09**#$"))

print("\n"+minsym+" END FUNC 03 "+minsym+"\n")


#%%

#%%

#Execution of Decoding (Morse Code --> String)
 
print("\n"+eqsym+"\n  Running Function  - Decode (Morse Code --> Str\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> decode(\".... . -.-- /- .... .. ... /.. ... /.-. .- .--- /.... . .-. . .-.-.- /.... .- .--. .--. -.-- /-.. .- -.-- .-.-.- \")")
print("\tResult --> "+MyModule.decode(".... . -.-- /- .... .. ... /.. ... /.-. .- .--- /.... . .-. . .-.-.- /.... .- .--. .--. -.-- /-.. .- -.-- .-.-.- "))

print("\nCase 02:\n\tFunc   --> decode(\".... . .-.. .-.. --- /.-- --- .-. .-.. -.. \")")
print("\tResult --> "+MyModule.decode(".... . .-.. .-.. --- /.-- --- .-. .-.. -.. "))

print("\nCase 03:\n\tFunc   --> decode(\"-- -.-. ... .---- --... ...-- /-....- /.--. -.-- - .... --- -. /.-.. .- -... ----- ...-- \")")
print("\tResult --> "+MyModule.decode("-- -.-. ... .---- --... ...-- /-....- /.--. -.-- - .... --- -. /.-.. .- -... ----- ...-- "))

print("\nCase 04:\n\tFunc   --> decode(\"Invalid input --> *&--09**#$\")")
print("\tResult --> "+MyModule.decode("Invalid input --> *&--09**#$"))

print("\n"+minsym+" END FUNC 04 "+minsym+"\n")


#%%