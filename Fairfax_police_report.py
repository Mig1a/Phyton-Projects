#Million Aboye
class FCPDCrime:
    def __init__(self, name = 'Fairfax CountyPolice Crime Report'):
        self.name = name
        self.stateinfo = []

    def countByCrime(self, select = 'all'):
        self.select = select
        week = [week[3] for week in self.stateinfo]
        week_start, week_end = week[0], week[-1]
        crime_count = {}
        new = []
        if self.select == 'all':
            for i in self.stateinfo:
                key = i[2]
                if key not in crime_count:
                    crime_count[key] = 1
                    new.append([i[1], key, 1])
                else:
                    crime_count[key] += 1
                    for k in new:
                        if k[1] == key:
                            k[2] = crime_count[key]
                            break
            sorted_crimes = sorted(new, key=lambda x: x[2], reverse=True)
            print(f"FCPD police Crime Statistics for the week {week_start} through {week_end}:\n")
            print(f"List of crimes, sorted by frequency for all zip codes are the following\n")
            print("{:<15} {:<25} {:<25} {:<25}".format('Code', 'Reported incident', 'Frequency', 'Crime type'))
            print("-" * 100)
            total_sum = 0
            for i in sorted_crimes:
                total_sum += i[2]
            for i in sorted_crimes:
                frequency = str(round((i[2] * 100) / total_sum, 2)) + '%'
                print("{:<20} {:<20} {:<20} {:<20}".format(i[0], i[2], frequency, i[1]))
        else:
            for i in self.stateinfo:
                if self.select == i[-1]:
                    key = i[2]
                    if key not in crime_count:
                        crime_count[key] = 1
                        new.append([i[1], key, 1])
                    else:
                        crime_count[key] += 1
                        for k in new:
                            if k[1] == key:
                                k[2] = crime_count[key]
                                break
            sorted_crimes = sorted(new, key=lambda x: x[2], reverse=True)
            print(f"FCPD police Crime Statistics for the week {week_start} through {week_end}:\n")
            print(f"List of crimes, sorted by frequency for {self.select} are the following\n")
            print("{:<15} {:<25} {:<25} {:<25}".format('Code', 'Reported incident', 'Frequency', 'Crime type'))
            print("-" * 100)
            total_sum = 0
            for i in sorted_crimes:
                total_sum += i[2]
            for i in sorted_crimes:
                frequency = str(round((i[2] * 100) / total_sum, 2)) + '%'
                print("{:<20} {:<20} {:<20} {:<20}".format(i[0], i[2], frequency, i[1]))
    def countByZip(self):
        reported_crimes = self.stateinfo
        week = [week[3] for week in self.stateinfo]
        week_start, week_end = week[0], week[-1]
        crime_count = {}
        new = []
        for i in reported_crimes:
            key = i[-1]
            if key not in crime_count:
                crime_count[key] = 1
                new.append([i[1], key, 1])
            else:
                crime_count[key] += 1
        sorted_crimes = sorted(crime_count.items(), key=lambda x: x[1], reverse=True)
        print(f"FCPD police Crime Statistics for the week {week_start} through {week_end}:\n")
        print(f"Count of number of reports by Zip Code, sorted by frequency\n")
        print("{:<15} {:<25} {:<25}".format('Zip Code', 'Reported incident', 'Frequency'))
        print("-" * 50)
        total_sum = 0
        for i in sorted_crimes:
            total_sum += i[1]
        for i in sorted_crimes:
            frequency = str(round((i[1] * 100) / total_sum, 2)) + '%'
            print("{:<20} {:<20} {:<20}".format(i[0], i[1], frequency))

    def load(self, file = "C:/Users/mella/OneDrive/Desktop/GMU/IT 209/CrimeReports (1).csv"):
        self.file = file
        with open(self.file, 'r') as x:
            self.read = x.readlines()
            for i in self.read:
                self.stateinfo.append(i.strip().split(','))
        return len(self.stateinfo)
    def printCrimes(self, zip = 'all'):
        week = [week[3] for week in self.stateinfo]
        week_start, week_end = week[0], week[-1]
        self.zip = zip
        print(f"Fairfax County Police Crime Report\n")
        print(input(f"FCPD police Crime Statistics for the week {week_start} through {week_end}\n {len(self.stateinfo)} lines follow, hit 'Enter' to view"))
        print("{:<5} {:<15} {:<55} {:<10} {:<15} {:<25} {:<18} {:<15} {:<25}".format(" ", "Code", "Crime Type", "Date", "Time", "Address", "City",
                                            "State","Zip code"))
        print('-' * 180)
        if self.zip == 'all':
            for i in self.stateinfo:
                print("{:<5} {:<15} {:<50} {:<15} {:<10} {:<30} {:<20} {:<15} {:<20}".format(i[0], i[1], i[2],i[3], i[4], i[5], i[6], i[7], i[8]))
        else:
            for i in self.stateinfo:
                if self.zip == i[-1]:
                    print("{:<5} {:<15} {:<50} {:<15} {:<10} {:<30} {:<20} {:<15} {:<20}".format(i[0], i[1], i[2], i[3],
                                                                                                 i[4], i[5], i[6], i[7],i[8]))

    def zipCodeList(self, zip='22030'):
        self.zip = zip
        ziplist = []
        for i in self.stateinfo:
            if self.zip == i[-1]:
                ziplist.append(i)
        return ziplist

Fairfax_police= FCPDCrime()
Fairfax_police.load()
Fairfax_police.printCrimes()
Fairfax_police.countByZip()
Fairfax_police.countByCrime()





