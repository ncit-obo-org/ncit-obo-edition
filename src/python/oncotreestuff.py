import sys
import csv
import re

subjectpattern = ('<http://purl.obolibrary.org/obo/NCIT_')
predobjpattern = ('<http://www.geneontology.org/formats/oboInOwl#inSubset> <http://purl.obolibrary.org/obo/ncit#oncotree_slim> .')

def oncotree(infile, outfile):
    with open(infile, newline='') as oncotreedata: #open the oncotree data
        myreader = csv.reader(oncotreedata, delimiter='\t') #read the file in and tell python it is a tab-delimited file
        ncidlist = [] #create a new empty list which we will put stuff in later
        next(myreader) #strips header row
        for row in myreader: #for each row in the oncotreedata list of lists
            if row[9] != "": #ignore column 8 if it is blank
                ncidlist.append(row[9]) #and put all other items in column 8 in this list
                ncidlist2 = [] #make a new list
                for item in ncidlist:
                    splitncid = item.split(',') #for each item in the first list (ncidlist), split it if it has a comma in it and store it in splitncid
                    for ncid in splitncid:
                        ncidlist2.append(ncid.strip()) #append each item from splitncid to ncidlist2



        with open(outfile, 'w') as rdfoutput: #open a new file to write to
            for ncid2 in ncidlist2: #for each nci-id, write a triple composed of the above and below patterns
                spiffytriples = (subjectpattern + ncid2 + '> ' + predobjpattern + '\n') #ultimate pattern which combines subject, predobj, and a newline
                rdfoutput.write(spiffytriples) #write that sucker to the file

oncotree(sys.argv[1], sys.argv[2])
