from constants import END_SEQUENCE, FRAMES_PERIOD
import wave

print("=== RESONANCE: decode audio file ===\n")
print("Encoded audio file must be a .wav.")
print("Frames period is 20 by default. If you did not receive a message specifying a different frame period, use 20.")
print()

encodedfile = input("Enter encoded audio file path (out.wav): ")
new_frames_period = input("Enter frames period ({}): ".format(FRAMES_PERIOD))
decodedfile = input("Enter decoded output path: ")

if(len(new_frames_period) == 0):
	new_frames_period = FRAMES_PERIOD
else:
	try:
		new_frames_period = int(new_frames_period)
	except Exception as e:
		print("Invalid frames period.")

FRAMES_PERIOD = new_frames_period

if len(encodedfile) == 0:
	encodedfile = "out.wav"

file = wave.open(encodedfile)
nframes = (file.getnframes())

frames = file.readframes(nframes)
frame_index = 0
result = []
while result[-len(END_SEQUENCE):] != END_SEQUENCE:
	cur = 0
	for i in range(8):
		cur += (frames[frame_index] & 1) * (1 << (8 - i - 1))
		frame_index += FRAMES_PERIOD
	result.append(cur)
result = result[:-len(END_SEQUENCE)]

f = open(decodedfile, 'wb')
f.write(bytearray(result))
f.close()

print()
print("Decoded contents exported to {} successfully.".format(decodedfile))