import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)

Index = names.index('sam')
loanStatus = stats[Index]
print("sam's loan status is "+loanStatus)

with open('utilities/loanapp.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob", "Rejected"])
