# AI@motion

## General

5th May - 31st of July

End of june and beginnign of july will be mostly dediated to the exams.

--> very short timespan

--> Use as much pre existing libs /pretrained models etc. as possible
--> Fuck over great test etc..

Focus on time saving / getting to smth. we can present at the end

End of may will be a short talk with the profs, we should have atleast a plan by then, aswell as some basic code structure.


## Problem Overview

Hypothetical "Mobibox" takes commands in natural speech, executes them in airsim.
Transform natural speech to text, classify text into commands, execute commands while avoiding obstacles, staying on road etc...
Here a basic overview of what i was imagining, please note that this is mostly pseudo uml.

<img src="./overview.svg">

## Subproblems in more detail

### SpeechRecognizer: 
- fetch audio input from a microphone
- convert audio input to text
- mayne libs available for example: https://pypi.org/project/SpeechRecognition/

### TextClassifier:   
- gets text from SpeechRecognizer as input  
- classifies the text into commands  
e.g. "move right at the next corner", becomes a move(0, 5, 0) -> where the vehicle is   currently moving on the x axis, moving at a corner instead of into a building etc. then happens in the vehicle class  
- then calls command on the vehicle  

### Vehicle:          
- Interface of drone, car and theoratically more   
- my idea here is to group the vehicles so we can use one classifier because i think the  classifier will be one of the hardest tasks, instead of having a classifier for each  vehicle. The logic tha for example a car cant move up will then happen in the car class. Which is hopefully  also more robust.  

### Drone:            
- logic and api for drone  
- has move, land, takeoff etc functions which internally check for collisions etc. using the sensors and call the airsim api functions  
- Goal here will be to take it as simple as possible, we have an outside observer with  the user, so GPS as position should be enough. Same goes for collision avoidance. We do  not need to know that this is a house or a tree, we just need to not crash into it, the  user will know the rest.  

### Car:              
- logic and api for car  
- many parallels to the drone  
- biggest difference is probably that the car will need some lane detection  




