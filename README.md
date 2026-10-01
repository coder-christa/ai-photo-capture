This project is licensed under the MIT License. See the License.txt for details.

Summary:

I'm building this project for end users to have a code base with open source gardening knowledge and tools for home gardening automation. This is also for general learning purposes. This is part one of many furture releases and updates. I have no set schedule at the moment.

What does this initial portion of code do?

    This is a very simple photo capture tool. 
    This feeds eventually into custom local models and used for other purposes in the future.
    It feeds in the overall ecosystem I am actively building and running in my home. 
    This is a small part of a larger API service(application programming interface) and larger code base. 

What's next in the future of this code base?

    meta data tagging pipelines for captured photo sets 
    Cleansing and sorting algorithms 
    Feeding cleansed and tagged photo sets to various training models or used for more purposes and use cases.
    Hugging face tie ins and other functions as I test and vet them.

Who I'm trying to gather as an audience?

    I'm intentionally writing this readme and the code comments for learning purposes and minimizing tech jargon. 
    I'm assuming a low level of baseline tech knowledge and experterise. 
    Although that is a bold assumption posting this on git. 
    If you found this repo through github you probably don't need a painful level of handholding, but this readme isn't for you but you probably      aren't reading this and skipped to the technical specs and code.

    This overall project is for the fellow DIYers/gardeners that want to claw back some of their labor.
    The people that want personalized AI gardening tools without a large sticker price 
    and a pathway to make it customizable to their setup and plants.

What drives me to do all this?

    If nothing else is achieved from this project, I hope to get a few people to think about what kind of society they want to live in. 
    This is one small step towards re-building more equality and dignitity through knowledge sharing.

    This code base is one angle to chip away at the narrative that 
    you must pay an endless subscription for common useful software while sacrificing your privacy. 
    The perceived alternative is no access or limited access with creepy ads. 
    Those statements are false if you look for the information. 
    Reading through this document is a small step forward.

AI use in this code base:

    This readme is mostly hand typed except the MIT license which I copied and pasted from the generated MIT license directly. 
    This is for liability purposes. 
    
    The comments are hand written without AI. 
    They probably go into more detail than needed. 
    This is partially so I keep track of things and it helps me if I take longer breaks. 
    I'm also trying to handhold people if they're interested in what the code is doing and why.

    The code was AI assisted to a degree through a local Jan chatbot.
    
    For more info on Jan: https://www.jan.ai/ 
   
    When using Jan, human logic is intentionally put into the design choices. 
    I don't blindly copy and paste anything without fully thinking it through before testing and publishing publicly. 
    I run everything myself locally and try to run on multiple devices and OS patches when possible. 
    
    Not every situation or device will be throughly tested and there will likely be some amount of friction and troubleshooting for anyone else       using this

Warnings and misuse:

Please be careful and mindful of where a camera using this code is pointed. There are no warning shots or warnings displayed due to the intended use case. It is easily automated with the intention to take a massive number of photos for AI training purposes and capturing long periods of plant growth.
    
Unflattering background objects can be captured unintentionally if not handled appropriately. Be mindful to unplug the camera or cover any webcam just in case and/or check the logs and find additional information if you aren't sure. Don't publish/fork this code base with your own photos publicly in the photos folder unless you are sure they are clean.

Do not knowingly use this for any malicious purposes, I am not liable for such actions. 
This is intented to be used on local personal devices for plant identiicaiton and learning purposes. I
ultimately have no control over people using it in unintented ways, but please be a good person and don't be an intentional asshole. 

Technical specs:

    Language: Python 3.x
    Dependences: 
    cv2 (OpenCV) - for photo capture
    datetime
    other standard python libraries

How do you download/install this?

    These are the high level instructions and will vary depending on the OS and device used:

    1) Create a directory for this project on your local hard drive
    2) Download/clone this repo to the created folder
    3) Install python if needed(found through a websearch, homebrew or whatever means if it's not already installed)
    4) pip install opencv-python



To take a one off photo:

Switch to the directory where the .py files of this project were downloaded.

To take a one off photo run this on your CLI(command line interface/black box):

    python3 take_photos.py photos

Additional warnings:
    THERE IS NO WARNING IN THE CODE FOR WHEN A PHOTO WILL BE TAKEN. PROCEED WITH CAUTION.
    For safety, always double check everything and/or put a cover over your camera when not in use. 
    There are no warnings other than a light for a moment or two on some devices(this may vary). 

    Proceed at your own risk with giving permissions to your personal web cam, especially on a laptop or desktop. 
    There is a real risk of photos being taken automatically without you realizing especially if you don't know what you are doing and why.

    This code base does not take automatic photos as is and only triggers manually. 
    I am not including instructions for large photo dumps and scheduling to minimize accidental harm. 
    For the intended uses you have to schedule this workflow and manage it on your own. 

    Always look through this code base throughly before downloading and look up specifics if you aren't sure. 
    Look into further details about your specific devices and OS behaviors before executing or scheduling this code. 


Included in this code base:

take_photos.py: 
    This acts as the main entry point for photo triggering. This also handles logging, global variables, global calls and calls the camera management functions

camera_management.py: 
    takes the photos, stores the photos, handles warming up the camera, ensures a good photo can be taken, ensures the camera is ready to take a photo etc

key sub directories in this code base:

configs: 
    logging, global settings, function for current datetime capture, modules for handling logging etc

photos:
    default directory for photo dumps. file names have a unique timestamp to avoid overwriting previous photos. 

logs: 
    logs files are placed here when the application is executed. Logs are currently append only with timestamps in each entry for troubleshooting. You may need to manually purge the log file if it becomes large or modify the code to manage it longer term. 




