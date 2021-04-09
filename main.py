import base64
import re
import argparse
import sys

def encode(n,text):
    while True:
        if n == 0:
            print("encode:",text)
            break
        b64encoded = base64.b64encode(text.encode()).decode()
        text = b64encoded
        n -= 1


def decode(text):
    while True:
        try:
            b64decoded = base64.b64decode(text.encode()).decode()
            judge = re.fullmatch('^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$',b64decoded)
        
            if judge is not None:
                text = b64decoded
            else:
                print("decode:",b64decoded)
                break

        except UnicodeDecodeError:
            print("decode:",text)
            break

def main():
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--decode",action="store_true")
    parser.add_argument("-e","--encode",action="store_true")
    parser.add_argument("text", help="target text")
    parser.add_argument("-t","--times",default=1,type=int,help="number of encode times")
    args = parser.parse_args()
    if args.encode:
        encode(args.times,args.text)
    elif args.decode:
        decode(args.text)
    else:
        print("command base64 -help and follow it")
    
if __name__ == "__main__":
    main()

    