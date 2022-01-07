import webvtt
import sys

if __name__=='__main__':
    V = webvtt.read(sys.argv[1])
    V.show_statistics()
