# Resonance — Audio Steganography in Python

Resonance is a Python program that uses least-significant-bit (LSB) audio steganography to encode files and data in audio files.

Resonance is unique in that it can encode any type of file — PDFs, .zip files, images, other audio files, etc. — into an audio track. It also avoids the primary downside of added static noise that the LSB method has by adding a 'frame period'.

## Usage

 1. Make sure Python 3 is installed. If you intend to use Resonance with MP3 files, install ffmpeg as well.

 2. Encode a file in an audio track by running `encode.py`:

```
python3 encode.py
```

 3. Decode a file in an audio track by running `decode.py`:

```
python3 decode.py
```

## Encoding and Decoding Algorithm

Resonance uses least-significant-bit (LSB) audio steganography with the WAV file format.

When encoding, the algorithm takes an audio file and a file to encode, and encodes the bytes of the file to encode into the audio file, and outputs the resulting encoded audio file.

When decoding, the algorithm takes an encoded audio file and outputs the decoded bytes to a specified file path.

### Encoding Algorithm

When encoding the contents of a file into an audio file, the algorithm takes the contents of the file to encode as bytes and encodes each bit of each byte into a single WAV frame of the original audio file.

At first, the algorithm ordered each bit consecutively, but that caused a noticable amount of static noise in the outputted audio file. As a result, a 'frame period' is used, in which only every 20 or so frames are used to encode. This causes less static and makes the changes much less noticable. The frame period can be changed to allow more data to be stored in smaller/shorter audio files.

To complete the encoding, a unique sequence of bytes is encoded at the end. This unique bytes sequence marks the end of the encoded file contents and is necessary for the decoding algorithm to work.

### Decoding Algorithm

When decoding the contents of an encoded file, the algorithm goes through the encoded frames of the audio file, and reads the last bit in multiples of eight. For every additional byte added to the result, the decoding algorithm checks if the end sequence is present and stops if it is.

After completion, it writes the resulting bytes to a file.

## License

Resonance is MIT Licensed.
