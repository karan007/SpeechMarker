#!/usr/bin/python
import sys
import speech_to_text as speech
import image_manipulation as image

if __name__ == '__main__':

    if(str(sys.argv[1][1]) == 's'):
        text = speech.toText()
        name = input("Enter the path to the image you want to be watermarked")
        print (image.waterMark(text,name));
        print ('Done')
    else:
        print ('No such command')
