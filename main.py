import csv
import os
import searchmanager

# For Experiment Purpose
# Create sequence of semitone
def createTranscription(path, fileName):
    temp = []
    inputName = path + fileName
    outputName = inputName[:-4] + "_transcript.csv"
           
    with open(inputName) as csvfile:
        transcriptreader = csv.DictReader(csvfile)

        for row in transcriptreader:
            temp.append(int(row['semitone']))

    with open(outputName, 'wb') as csvfile:
        transcriptwriter = csv.writer(csvfile, delimiter=',')
        transcriptwriter.writerow(['semitone'])

        for index in range(len(temp)):
            if (temp[index] != temp[index-1]):
                transcriptwriter.writerow([temp[index]])

def main():
    # Set input and output path
    rawDBPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/files/'
    dbPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/transcriptions/'
    recordPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/records/Eksperimen 4/'

    # Init database
    print 'Initializing database...'
    controller = searchmanager.SearchManager()
    controller.init(rawDBPath, dbPath)
    print 'Database successfully initialized.'

    print '\n*************************************************************'
    print '************************ MIDIMATCHER ************************'
    print '*************************************************************\n'

    # Get record file name from user input
    recordName = raw_input('Insert record name (without file format): ')

    if os.path.isfile(recordPath + recordName + '.wav'):
        # Call praat script
        os.system('praatcon.exe pitch_listing.praat 10 yes 0 70 2000 \"' + recordName + '\"')
        createTranscription(recordPath, recordName + '_result.csv')
    
        # Begin searching module
        result = controller.getDistance(recordPath, recordName, dbPath)
        controller.sortByDist(result, 10, recordPath, recordName)
    else:
        print 'No such file.'

if __name__ == '__main__':
    main()