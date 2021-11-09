cuvant = input("Cuvantul este ")
h=0
for c in range(0,int(len(cuvant)/2)):
    if(cuvant[c].lower()!=cuvant[len(cuvant)-c-1].lower()) and (h==0):
        print("Cuvantul nu este palindrom")
        h=1
if(h==0):
    print("Cuvantul este palindrom")