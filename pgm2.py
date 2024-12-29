print("welcome to the tip calculator")
bill=float(input("what was the total bill?$"))
tip=int(input("How much tip would you like to give?10 12 15:"))
persons=int(input("How many people will split the bill?"))
bill_with_tip=tip/100*bill+bill
each_person_bill=bill_with_tip/persons
print("final bill:"+str(bill_with_tip))
print("each person will pay:"+str(each_person_bill))
