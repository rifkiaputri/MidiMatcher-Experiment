import csv
import midiparser

class MidiManager:

    # Parse midi file to .csv format
    def parseMidi(self, inputPath, outputPath, fileName):
        inputName = inputPath + fileName
        outputName = outputPath + fileName[:-4] + '.csv'
        # print 'Writing ' + fileName[:-4] + ' to csv...'

        # Read midi file using midiparser library
        midi = midiparser.File(inputName)
               
        with open(outputName, 'wb') as csvfile:
            midiwriter = csv.writer(csvfile, delimiter=',')
            midiwriter.writerow(['time', 'semitone'])

            for track in midi.tracks:
                for event in track.events:
                    if event.type == midiparser.voice.NoteOn:
                        midiwriter.writerow([event.absolute, event.detail.note_no])
                        # Add Short pause model
                        midiwriter.writerow([event.absolute+1, 999])

    # Read midi note (semitone) from .csv format
    # Output: list of semitone
    def readMidi(self, path, fileName):
        temp = []
        inputName = path + fileName
               
        with open(inputName) as csvfile:
            midireader = csv.DictReader(csvfile)

            for row in midireader:
                temp.append(int(row['semitone']))

        return temp
