# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:35:39 2014

@author: swalters
"""

import numpy
import random
import wave
import struct
import math

def makeTransition():
    LA = [[0.18, 0.5, 0.15], [0.6, 0.5, 0.75], [0.22, 0, 0.1]]
    LD = [[0, 0.25, 0.9], [0, 0, 0.1], [1, 0.75, 0]]
    LG = [[0.4, 0.5, 1], [0.4, 0.25, 0], [0.2, 0.25, 0]]

    return [numpy.matrix(LA), numpy.matrix(LD), numpy.matrix(LG)]

# memoize?
# sampling wheel
def predict(k, currentState, prevState):
    [a, d, g] = makeTransition()

    p = numpy.matrix(prevState)
    c = numpy.matrix(currentState)

    L = None
    for i in range(k):
        # choose transition matrix
        if p[0,0] == 1: L = a
        elif p[1,0] == 1: L = d
        else: L = g

        # compute next
        p = samplingWheel(c)
        c = samplingWheel(L*c)
    return c

def samplingWheel(a):
    r = random.random()
    if 0 < r < a[0,0]:
        return numpy.matrix([[1],[0],[0]])
    elif a[0,0] < r < a[1,0]+a[0,0]:
        return numpy.matrix([[0],[1],[0]])
    else:
        return numpy.matrix([[0],[0],[1]])

def generateMusic(length=10):
    currentState = [[1],[0],[0]] # Arbitrarily start on an 'a' note for now
    prevState = [[0],[1],[0]] # And arbitrarily decide we just came off a 'd' note
    notes = []

    for i in range(length):
        futureState = predict(i,currentState,prevState)
        notes.append(whichNote(futureState)) # build the list of notes to write out later
        prevState = currentState # advance a timestep
        currentState = futureState

    createWav(notes)
    return

def whichNote(stateArray,notes=['a','d','g']):
    if not len(notes) == len(stateArray): # do some quick sanity checking
        print "what is this I don't even"
        return None

    for i in range(len(notes)):
        if stateArray[i] == 1:
            return notes[i]

    return None # if there's no match, just fail out

def createWav(notes):
    audioPhile = [] # Get it, it's funny because audio file sounds like audiophile
    maxAmplitude = 30000.0

    for note in notes:
        tone = generateTone(note) # generate 1 second of that note
        audioPhile.extend(tone)

    w = wave.open('soundfile.wav','w')
    channels = 2 # stereo audio
    samplewidth = 2 # 16 bit audio
    framerate = 44100 # CD quality
    nframes = len(notes)*framerate # total number of frames we'll be writing
    w.setparams((channels,samplewidth,framerate,nframes,'NONE','not compressed'))

    frames = []
    for sample in audioPhile:
        sample *= maxAmplitude
        frames.extend(struct.pack('h',int(sample)))
    frames = ''.join(frames)

    w.writeframesraw(frames)
    w.close()

def generateTone(note):
    # generates 1 second of sine wave in a note's frequency
    tone = []
    framerate = 44100
    noteLookup = {'d':293.665,'a':440,'g':391.995}
    frequency = noteLookup[note]
    for i in range(framerate): # for 1 second
        wave = math.sin(2.0*math.pi*float(frequency)*(float(i)/float(framerate))) #fundamental wave
        wave += math.sin(2.0*math.pi*float(2.0*frequency)*(float(i)/float(framerate))) #add first harmonic
        wave += math.sin(2.0*math.pi*float(3.0*frequency)*(float(i)/float(framerate))) #add second  harmonic
        wave /= 3 # adding harmonics has made our waveform too big
        tone.append(wave)
    return tone

# NOTE: this should really be turned into a class. noteLookup should be a member
# var that provides all "known" notes and their frequencies. Framerate, sample
# width, channels, etc. should all be member vars, and the current audio file
# should probably also be a member var that can be written out by createWav. Or
# something like that.
