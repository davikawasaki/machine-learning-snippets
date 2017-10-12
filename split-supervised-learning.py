#!/usr/bin/python

import csv, sys

class SplitBase:

    def __init__( self, reader ):
        self.reader = reader
    
    # Split and order each truelabel rows in grups
    # Has truelabel group, truelabel index, truelabel object.
    #
    # @param self
    # @param trueLabel
    #
    # @return trueLabelGroup
    def split( self, trueLabel ):

        tlgb = {}
        for n, row in enumerate(self.reader):
            # Save header row
            if n == 0:
                self.header = row
                tli = self.getTrueLabelIndex(self.header, trueLabel)
                if(tli == -1):
                    raise Exception('There is not any truelabel as ' + trueLabel)
                else:
                    self.tli = tli
            # Get other rows
            else:
                tlo = row[self.tli]
                if tlo not in tlgb:
                    tlgb[tlo] = list()
                del(row[self.tli])
                tlgb[tlo].append(row)

        return tlgb
    
    # Split and order each truelabel rows in grups
    # Has truelabel group, truelabel index, truelabel object.
    #
    # @param self
    # @param trueLabelGroupedBy
    # @param trainingRate
    # @param dataFileName
    #
    # @return Boolean
    def extractSaveBaseRates( self, tlgb, trRate, dfn ):
        if not tlgb:
            return False
        if not trRate:
            return False
        else:
            trGroup = []
            ttGroup = []
            
            trRate = trRate/100.0

            for key, arrays in tlgb.items():
                n = len(arrays)
                trQty = int(n*trRate)
                for i, item in enumerate(arrays):
                    item.insert(0, key)
                    if i < trQty-1:
                        trGroup.append(item)
                    else:
                        ttGroup.append(item)

            # Generate training sample file                 
            trOutFile  = open('data/output/' + dfn + '_training' + '.csv', "wb")
            writer = csv.writer(trOutFile, delimiter=',')

            # Header as the first row to save
            writer.writerow(self.header)
            # Save other rows
            for item in trGroup:
                writer.writerow(item)

            trOutFile.close()

            # Generate testing sample file                 
            trOutFile  = open('data/output/' + dfn + '_testing' + '.csv', "wb")
            writer = csv.writer(trOutFile, delimiter=',')

            # Header as the first row to save
            writer.writerow(self.header)
            # Save other rows
            for item in ttGroup:
                writer.writerow(item)

            trOutFile.close()
            
            return True

    # Return true label column index inside csv file
    #
    # @param self
    # @param header
    # @param trueLabel
    #
    # @return index (-1 for non-existent)
    def getTrueLabelIndex ( self, header, trueLabel ):
        colnum = 0
        for col in header:
            if col == trueLabel:
                return colnum
        return -1

################
# Main process #
################

# truelabel and datafile
tl = sys.argv[1]
df = sys.argv[2]

# training and testing rates
trRate = int(sys.argv[3])
ttRate = int(sys.argv[4])

if((trRate + ttRate) != 100):
    print 'Training and Testing rates must complete 100%! Try it again.'
elif(ttRate > trRate):
    print 'Testing rate must not be bigger than Training rate! Try it again.'
else:    
    idf = open('data/raw/' + df + '.csv', 'rU')
    reader = csv.reader(idf, delimiter=',')

    splitBase = SplitBase(reader)
    tlgb = splitBase.split(tl)
    #print tlgb

    if splitBase.extractSaveBaseRates(tlgb, trRate, df):
        print 'Successful extraction of ' + df + ' file!'
    else:
        print 'There was an error in the extraction of ' + df + ' file!'
    idf.close()
