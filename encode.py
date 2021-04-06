import wave, random, sys, math
from constants import END_SEQUENCE, FRAMES_PERIOD
from pydub import AudioSegment

inputfile = input("Enter audio file path: ")
outputfile = input("Enter output file path (out.wav): ")
datafile = input("Enter data file path: ")

if inputfile.endswith(".mp3"):
	sound = AudioSegment.from_mp3(inputfile)
	sound.export(".exported.wav", format="wav")
	inputfile = ".exported.wav"
elif not inputfile.endswith(".wav"):
	print("Input audio file must be .wav or .mp3.")
	sys.exit()
if len(outputfile) == 0:
	outputfile = "out.wav"

endsequence = bytearray(END_SEQUENCE)

file = wave.open(inputfile)
nchannels = file.getnchannels()
sampwidth = file.getsampwidth()
framerate = file.getframerate()
nframes = file.getnframes()
comptype = file.getcomptype()
compname = file.getcompname()
params = file.getparams()

new_file = wave.open(outputfile, 'wb')
new_file.setnchannels(nchannels)
new_file.setsampwidth(sampwidth)
new_file.setframerate(framerate)
new_file.setnframes(nframes)
new_file.setcomptype(comptype, compname)
new_file.setparams(params)

bytes_content = open(datafile, 'rb').read()

full_bytes_content = bytes_content + endsequence

frames = bytearray(file.readframes(nframes))
frame_index = 0

frames_to_use = 8 * FRAMES_PERIOD * len(full_bytes_content)
if(frames_to_use > len(frames)):
	print("Data is too large for the input file: {}% too large.".format(((frames_to_use / len(frames)) - 1) * 100))
	FRAMES_PERIOD = math.floor(len(frames) / (len(full_bytes_content) * 8))
	if FRAMES_PERIOD <= 0 or input("Would you like to decrease your frames period to {} to fix (Y/n)? ".format(FRAMES_PERIOD)).lower() == "n":	
		sys.exit()

for byte in full_bytes_content:
	for i in range(8):
		bit = byte >> (8 - i - 1) & 1
		frames[frame_index] = ((frames[frame_index] >> 1) << 1) + bit
		frame_index += FRAMES_PERIOD

new_file.writeframes(bytes(frames))

print("Encoded file exported to {} successfully.".format(outputfile))
print("The frames period of {} was used.".format(FRAMES_PERIOD))