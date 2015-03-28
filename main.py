import os
import searchmanager

def main():
    # Set input and output path
    rawDBPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/files/'
    dbPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/transcriptions/'
    recordPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/records/'

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
    
        # Begin searching module
        result = controller.getDistance(recordPath, recordName, dbPath)
        sortedResult = controller.sortByDist(result, 10)
    else:
        print 'No such file.'

if __name__ == '__main__':
    main()