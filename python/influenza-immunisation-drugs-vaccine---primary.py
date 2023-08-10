# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"10905001","system":"gprdproduct"},{"code":"11288001","system":"gprdproduct"},{"code":"12770001","system":"gprdproduct"},{"code":"13403001","system":"gprdproduct"},{"code":"1401001","system":"gprdproduct"},{"code":"14256001","system":"gprdproduct"},{"code":"14264001","system":"gprdproduct"},{"code":"2187001","system":"gprdproduct"},{"code":"2699001","system":"gprdproduct"},{"code":"465001","system":"gprdproduct"},{"code":"5882001","system":"gprdproduct"},{"code":"7313001","system":"gprdproduct"},{"code":"8968001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('influenza-immunisation-drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["influenza-immunisation-drugs-vaccine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["influenza-immunisation-drugs-vaccine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["influenza-immunisation-drugs-vaccine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
