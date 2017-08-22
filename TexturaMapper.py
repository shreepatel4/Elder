import csv
from datetime import datetime

result = {}
lineresult ={}

with open("ImportFile.csv",'wb') as csvfile:
    writer=csv.writer(csvfile, skipinitialspace=True, delimiter=',',
                      quoting=csv.QUOTE_MINIMAL)



    with open('TexturaExport.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        next(csvreader)
        for row in csvreader:
            Project = row[0]
            Vendor = row[1]
            Subcontract = row[2]
            Description = row[3]
            SubcontractDate = datetime.strptime(row[4],'%m/%d/%Y %H:%M:%S %p')
            SubcontractDate = SubcontractDate.strftime('%m%d%Y')
            Retention = row[5]
            CONumber = row[6]
            SubcontractLineNumber = row[7]
            Description = row[8]
            OriginalAmount = row[9]
            ChangeAmount = row[10]
            CostCode = row[11]
            Category = row[12]
            headerkey = Project + Vendor + Subcontract + CONumber
            linekey = Project + Vendor + Subcontract + CONumber + SubcontractLineNumber

           
            if headerkey in result:
                result[headerkey].append(headerkey)
                print "in"
                if CONumber =="" :
                    print OriginalAmount
                    if OriginalAmount != '0':
                        Sublines = ["CI", Project, Vendor, Subcontract, SubcontractLineNumber, OriginalAmount, Description, Project,'','','','',CostCode,Category]
                        #print Sublines

                        writer.writerow(Sublines)
                else:
                    if ChangeAmount != '0':
                        print CONumber
                        COlines = ["CCOI", Project, Vendor, Subcontract, SubcontractLineNumber, ChangeAmount, Description, Project,'','','','',CostCode,Category]
                        writer.writerow(COlines)
                    #print COlines
            else:
                result[headerkey] = [headerkey]
                print "out"
                amount = [OriginalAmount]
                total = sum(float(i) for i in amount)
                Subheader = ["C", Project, Vendor, Subcontract, total, SubcontractDate, Retention, Description, Project,
                             0, 0, 0, 0, 0, 0]
                if OriginalAmount != '0':
                    writer.writerow(Subheader)
                if linekey in lineresult:
                    result[linekey].append(linekey)
                    if CONumber =="":

                        if OriginalAmount != '0':
                            Sublines = ["CI", Project, Vendor, Subcontract, SubcontractLineNumber, OriginalAmount, Description, Project,'','','','',CostCode,Category]

                            writer.writerow(Sublines)

                        #print Subheader
                    else:
                        print 'no'

                else:
                    result[linekey] = [linekey]
                    if OriginalAmount != '0':
                        Sublines = ["CI", Project, Vendor, Subcontract, SubcontractLineNumber, OriginalAmount,
                                    Description, Project, '', '', '', '', CostCode, Category]
                        # print Sublines

                        writer.writerow(Sublines)
                    else:
                        if ChangeAmount != '0':
                            COheader = ["CCO", Project, Vendor, Subcontract, CONumber, SubcontractDate, Description,
                                            Project]
                                # COlines = ["CCOI", Project, Vendor, Subcontract, SubcontractLineNumber, OriginalAmount, Description, Project,'','','','',CostCode,Category]
                            writer.writerow(COheader)
                            COlines = ["CCOI", Project, Vendor, Subcontract, SubcontractLineNumber, ChangeAmount,
                                           Description, Project, '', '', '', '', CostCode, Category]
                            writer.writerow(COlines)
                            #print COheader
    #print result

