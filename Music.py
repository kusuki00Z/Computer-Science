# -----------------------------------------+
# Shengnan Zhou, Alex Tseng                |
# CSCI 107, Assignment 8                   |
# Last Updated: April 9, 2018              |
# -----------------------------------------|
# Make modifications to a musical          |
# composition program.                     |
# -----------------------------------------+

import pyaudio     # Remember to install pyaudio or this will not work
import math
import struct

# beats per minute
BPM = 260

# allowed notes and their frequencies
FREQUENCIES = {'A': 880, 'A#': 466, 'B': 493,
               'C': 523, 'C#': 554, 'D': 587,
               'D#': 622, 'E': 659, 'F': 698,
               'F#': 740, 'G': 784, 'G#': 830}

# the possible musical notes
POSSIBLE_NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# -------------------------------------------------

def main():

    # title
    print("Welcome to TunePlayer!")

    # give people a place to store their tune
    myEpicSong = []

    # options menu display, mistakes are caught
    while True:

        # menu items
        print("Some options are...")
        print("1. Create a tune.")
        print("2. View tune.")
        print("3. Play a tune.")
        print("4. Erase the tune and start over.")
        print("5. Please choose the beat per minute.")
        print("6. Exit. ")

        # make a selection
        selection = input("What would you like to do?: ")

        # choose between the menu items
        if selection == "1":
            # create a composition with the score editor
            myEpicSong = composeSong()
        elif selection == "2":
            # view the score
            viewSong(myEpicSong)
        elif selection == "3":
            # play the song that I've written
            playSong(myEpicSong)
        elif selection == "4":
            # replace the song with a blank array
            myEpicSong = []
        elif selection == "5":
            # change the beat per minute
            global BPM
            BPM = int(input("Please enter the beat per minute:"))
            while BPM < 60 or BPM > 200:
                print("Invalid input. Please Enter between 60 and 200.")
                BPM = int(input("Please enter the beat per minute:"))
            BPM = BPM
            print("The BPM you entered is", str(BPM) + ".")
        elif selection == "6":
            # we can leave the while loop now
            break
        else:
            # a poor choice
            print("The selection was invalid, please try again...")

    # we're done here
    print("Goodbye!")

# -------------------------------------------------

def viewSong(song):
    
    if len(song) == 0:
        print("No song data to display.")
        
    else:
        # print the header row
        for note in POSSIBLE_NOTES:
            print("{0:4s}".format(note), end="")
        print()

        for note in song:
            noteName = note[0]     # note name
            noteName = noteName.upper()
            noteLength = note[1]   # note length

            # now print this line of the score
            for bar in range(noteLength):
                for note in POSSIBLE_NOTES:
                    if note == noteName:
                        print("{0:4s}".format("*"), end="")
                    else:
                        print("{0:4s}".format("-"), end="")
                print()

# -------------------------------------------------

def composeSong():
    
    # create a list of tuples that is the song and return it
    # tuple must be (note, length)
    listOfNotes = []

    # continue until done
    while True:
        try:
            # get the note and length input here
            newNote = input("What note would you like to play (or type 'DONE' if finished) ?: ")
            newNote = newNote.upper()
            if newNote == 'DONE':
                break
            
            newLength = int(input("What is the length of this note?: "))

            # now turn the item into a tuple
            noteTuple = (newNote, newLength)

            # check for an error
            noteValid = False
            lengthValid = False

            # loop through and see what is happening
            for note in POSSIBLE_NOTES:
                if note == newNote:
                    noteValid = True

            if  newLength > 0 and newLength <= 4:
                lengthValid = True

            if lengthValid and noteValid:
                listOfNotes.append(noteTuple)
            else:
                print("Invalid entry.  Please try again.")
                
        except Exception as e:
            print("Something went wrong ... " + str(e))

    # get the composition
    return listOfNotes

# -------------------------------------------------

def playSong(song):

    if len(song) == 0:
        print("Invalid song, contains no notes!")
    else:
        # sample rate
        sample_rate = 44100
        bar_length = 90 / BPM

        # create the audio device and open the audio stream
        # fp precision is default, 1 channel (mono) audio
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, output=1)

        # read the song tuples and translate,
        # error out on an incorrect translation
        try:

            # create a stream to add things to
            currentStream = []
            for i in song:

                # get the note name and note length
                note = i[0]
                note = note.upper()

                if not (note in POSSIBLE_NOTES):
                    raise Exception("Note cannot be handled by the player class.")

                noteFrequency = FREQUENCIES[note]
                noteLength = float(i[1])

                if noteLength <= 0:
                    raise Exception("Invalid note length of 0 or less.")

                if noteLength > 4:
                    raise Exception("The length of a note is too long to be musically possible.")

                if noteFrequency <= 0:
                    raise Exception("Invalid frequency of zero or less, won't be playable.")

                if noteFrequency > 20000:
                    raise Exception("Invalid frequency of greater than 20000, as the note will be unhearable.")

                for i in range(0, int(noteLength * bar_length * sample_rate)):

                    # sine calculation for the current instrument
                    sample = (1.0 * math.pi * noteFrequency * i) / sample_rate

                    # a sine wave is the current instrument
                    currentNote = math.sin(sample)

                    # append the value to the stream
                    currentStream.append(currentNote)

                # append some silence so we don't get a bad pop
                for i in range(1, 1000):
                    currentStream.append(0.0)

            # write data to the stream
            # once finished, then write all data to the stream buffer (a special pack routine to implement the buffer as a list)
            stream.write(struct.pack('f'*len(currentStream), *currentStream))

        except Exception as e:

            # tell the user something's awry
            print("Something went wrong... " + str(e))
            stream.close()
            p.terminate()

        # finish by closing the stream and term the object
        print("Done playing!")
        stream.close()
        p.terminate()

# -------------------------------------------------

# start the music program
# main()

# When you submit your solution, uncomment the lines below
# and replace the notes for myEpicSong with the song you compose






# Ultimate Battle Simplified Version

myEpicSong = [('d#', 1), ('d#', 1), ('d#', 1), ('d#', 1), ('d#', 1), ('D', 1), ('C', 1), ('A#', 2), 
              ('D#', 1), ('D#', 1), ('D#', 1), ('D#', 1), ('D#', 1), ('f', 1), ('G', 1), ('F', 2), 
              ('D#', 1), ('d#', 1), ('D#', 1), ('d#', 1), ('D#', 1), ('G#', 1), ('G', 1), ('f', 1), 
              ('D#', 2), ('G', 1), ('F', 2), ('d#', 1), ('F', 1), ('G', 1), ('f', 1), ('D#', 1), 
              ('C', 1), ('D#', 1), ('C', 1), ('D#', 1), ('F', 1), ('G', 1), 
              ('f', 1), ('c', 1), ('a#', 1), ('c', 3)]


viewSong(myEpicSong)
playSong(myEpicSong)







