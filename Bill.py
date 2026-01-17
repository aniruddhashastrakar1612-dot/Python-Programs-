unit=int(input("enter the electricity unit")) #101
bill=0
if unit<=100:
  bill=0
elif unit>100 and unit<=200:
  bill=(unit-100)*5  #101-100*5
elif unit>=201 and unit<=300:
  bill=(100*5)+(unit-200)*7
elif unit>300:
  bill=(100*5)+(100*7)+(unit-300)*10
print("Electricity Bill Amount:",bill)
