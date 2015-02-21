import midimanager
import mlpy

def main():
    # Set input and output path
    inputPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/files/'
    outputPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/transcriptions/'
    recordPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher/records/'

    # Create MidiManager instance
    manager = midimanager.MidiManager()
    manager.parseMidi(inputPath, outputPath, 'HanyaSatu_Mocca_Vocal.mid')

    # Match record and reference's semitone using DTW
    record = manager.readMidi(recordPath, 'hanyasatu_result.csv')
    reference = manager.readMidi(outputPath, 'HanyaSatu_Mocca_Vocal.csv')
    print 'Calculating distance...'
    dist, cost, path = mlpy.dtw_subsequence(record, reference)
    print 'DTW distance: ' + str(dist)

if __name__ == '__main__':
    main()