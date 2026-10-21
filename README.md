This project is licensed under the MIT License. See the License.txt for details.

Summary:

I'm building this project for end users to have a code base with open source gardening knowledge and tools for home gardening automation. This is also for general learning purposes. This is part one of many furture releases and updates. I have no set schedule at the moment.

What is the overall large picture?

    I am building a fully customizable automated gardening tool set for others to use. 
    The final product will be private, will work on your own devices/hardware, no internet required and customizable to each user. 
    The idea overall idea is to train AI models on your specific pests, plant species, weeds, plant diseases etc. 
    
    
    There will be future functions such as:
    
    Automated water management, 
    automated soil testing, 
    guidance for soil deficiencies and remediation  
    pest management alerts when pests are detected, 
    pest and disease management and mitigation, 
    composting management
    and many more ideas I have actively been thinking about. 
    
    Once this code base is further along, you won't need to wait for updates, 
    you won't be beholden to a static set of data from environments 
    different than your exact setup. 
    
    If your needs change, you simply schedule to take photos, 
    upload them, add more data tags or other simple processes.
    This is the foundation to give the system more context about your exact setup. 
    
    
    Eventually a fancy user experience will be available to upload photos
    and plug in other information for machine learning. 
    
    This is a massive project so please be patient.
    
    
What is this small slice of code logic?

    The main goal here is to take a good number of photos over a period of time, fully hands off. 
    You can schedule it to take 1000 photos in a minute, or schedule it to take 4-5 photos at various times everyday for 30 or more days. 
    The schedule for photos will vary depending on what the user needs are which future modules you wish to use. 
    
    In the later versions, scheduling will be handled through a sleek web browser based user interface. 
    
    You won't need to schedule manually through cron or another scheduler, 
    the scheduler will be built in. I didn't include scheduling instructions to limit harm.

What does this initial portion of code do under the hood?

    This is a very simple photo capture tool locic to be used with a small device and a USB web cam.
    That's all this set of code can do right now.

What's next in the future of this code base?

   Designing and coding around making this logic easier to deploy and install for others
   Creating a digital 'receiver' to tie in with the larger view and 'apps' described above.
   Larger tie ins with other systems such as FarmOS.

Not going to lie, these next few updates are not going to be flashy or much to play with or use unless you're interested in the install process. 
However these updates are an extremely important building block for the rest of the vision described above to work properly. 
 
   
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

Update: For safety, blur functionality was added to prevent humans in the photos. It will blur them out automatically with a lightweight AI algorithm before saving photos. It can be adjusted for different cameras, a base 3% is used to expand or contract depending on the camera's resolution. Not perfect, but should minimize any unintentional harm. This was put in a separate class, more safety constraints can be added as needed. Still don't be an asshole.

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
    class for handling camera hardware and the shutter functions.
    Current functions: 
    taking photos, storing photos, warming up the camera, ensuring a good photo can be taken, handling multi threaded photos 

camera_safety:
    class for handling safety functions and bluring
    Currently blurs the photo if a human is detected in the photo
    
key sub directories in this code base:

configs: 
    logging, global settings, function for current datetime capture, modules for handling logging etc

photos:
    default directory for photo dumps. file names have a unique timestamp to avoid overwriting previous photos. 

ai_configs:
    these are default standard files used by AI photo detection. They are available online and are binary files for the AI algorithms used in       the camera_safety.py class
    
logs: 
    logs files are placed here when the application is executed. Logs are currently append only with timestamps in each entry for troubleshooting. You may need to manually purge the log file if it becomes large or modify the code to manage it longer term. 




