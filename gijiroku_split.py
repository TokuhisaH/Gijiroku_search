import os
g=open("gijiroku.tsv",encoding="utf-8_sig", errors='replace')
lists=g.read().splitlines()
g.close()

years=["194","195","196","197","198","199","200","201"]

for year in years:
    if os.path.exists("gijiroku"+year+"0.tsv"):
        print(year)
        os.remove("gijiroku"+year+"0.tsv")

n=0
for list in lists:
    for year in years: 
        
        
        if list.find(year)==0:
            if year!=n:
                n=year
                print(n)
            
            with open("gijiroku"+year+"0_normal.txt", 'a') as f:
               f.write(list[15:list.find("kokkai")-1]+"\n")