L=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"5005"},{"V":"S009"},
 {"VIII":"S007"}] 
print("Original list==",L) 
uniqueval=set(val for dic in L for val in dic.values()) 
print("Unique values==",uniqueval)
