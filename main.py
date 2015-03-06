import os
import searchmanager

def main():
    # Set input and output path
    rawDBPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/files/'
    dbPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/transcriptions/'
    recordPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/records/'

    # Call praat script
    os.system('praatcon.exe pitch_listing.praat 10 yes 0 70 2000')

    # Init database
    print 'Initializing database...'
    controller = searchmanager.SearchManager()
    controller.init(rawDBPath, dbPath)
    print 'Database successfully initialized.'

    print '\n*************************************************************'
    print '************************ MIDIMATCHER ************************'
    print '*************************************************************\n'

    # Get record file name from user input
    recordName = raw_input('Insert record file name (without file format): ')

    # Begin searching module
    if os.path.isfile(recordPath + recordName + '_result.csv'):
        result = controller.getDistance(recordPath, recordName, dbPath)
        sortedResult = controller.sortByDist(result, 15)
    else:
        print 'No such file.'

if __name__ == '__main__':
    main()