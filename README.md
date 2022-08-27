# Face-filter-using-open-cv
used pycharm IDE for this project
used opencv-python

used cvzone


create a new project and install necessary libraries mentioned above

create a Resources folder in your project file and add images to that folder.

used haarcascade frontal face default.xml
used facemesh from cvzone to detect points on face
then i used four points to separate the lips the lips,
in this i used 2 points to make the red points on edges of lips
you can uncomment some parts of the code to see how it works
also removing draw=false from detector shows the face mesh.

the four points on lips are connected by 2 lines(also hidden) and the ratio of these lines provide the data needed to find the opening or closing of mouth,

####
then i used haarcade to detect the face and overlapped a image when the mouth is open 
also using if else satements i implemented a second effect if you your mouth little bit 1st effect shows
and if you open it wider a second effect shows
####

the overlay png i used here was taken from internet, you can just change the overlay and by changing the image but this will need a little bit of adjustment to layout

there are two variation of the code in respect to the overlays they use the file [mainProgram.py] has a dog overlay which stays normal when you open mouth a little bit but
takes out tounge when you open mouth wider.(similar to snapchat dog filter)

the second program [mainProgramEmoji.py] uses emoji of smiling with mouth being little bit open and laughing when opened a bit wider.

the reason i uploaded two programs is because the dog filter one may not properly match with layout of your it works fine for me and i tried it on a few other people
but may not work with your face's layout, so the emoji one will be a smoother working example.

try out both and tell me which one you like!!!!
