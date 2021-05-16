import airsim
import argparse

import SpeechRecognizer as srs

parser = argparse.ArgumentParser(description='MobiBox')
parser.add_argument('--device', type=str,
                    help='Either Drone or Car, def', required=True)
args = parser.parse_args()

if __name__ == "__main__":
    if args.device == 'Drone':
        #import drone.py
        print("Drone")
    elif args.device == 'Car':
        #import car.py
        print("Car")
    else:
        print('Device not available \n')
        exit

    recognizer = srs.speech_recognizer()
    print("done")
    
else:
    exit