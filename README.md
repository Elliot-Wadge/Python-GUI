The layout of the directory is as follows:

# qtdesigner_files

inside the qtdesigner_files folder are the stored UIs that were used to compile qt_designer.py
they are .ui files and can be opened with qtdesigner and then after changes are made can be
recompiled to qt_designer.py with 'pyuic5 -x <name of .ui file> -o qt_designer.py'. Unless changes
to the appearance of the UI are desired these files should not be edited (through qt designer they should never be edited by hand). I have included one identical copy as of June 15 2021 since it can be easy to mess up the ui file and hard to undo. You can always discard the changes but a copy file should be updated whenever major changes are made to the original just in case. My repository will also have these files from when I last worked on them if necessary.


# last_position.text

this is a text file that stores the last position that the spectrometer was in, it is loaded upon launch
and written to when the close button is used. If this file isn't present or the contents are unreadable spectrometer will set the value of position to zero, upon using the close button it will write to this file the last position and overwrite anything inside or create the file if it has been deleted.

# graphing.py

this is where the plot classes, there is one for log scale and one for linear. I decided to move away from matplotlib because despite its familiar syntax it was too slow, I'm now using QChart which is a less robust but much faster at plotting.

# qt_designer.py

this is the compiled code from Qtdesigner it is messy as a result of being compiled by a robot. It is where all the names of the buttons and labels are defined and where they are given there size and position on the UI window, this file should not be edited from as all changes will be lost if you want to change the look and recompile a new .ui file see learning resources for more details.

# GUI.py

this is the work horse file, it imports the above qt_designer.py UI and stores it in an object called
self.ui, it then connects all the buttons to their corresponding functions and upon running will
display the fully functioning UI. THIS IS THE FILE YOU RUN IF YOU WANT TO SEE THE WORKING UI.

if you want to add additional buttons with functions here is what I think is the simplest way. navigate to the qtdesigner_files, open the spectrometer.ui with Qtdesigner (watch youtube tutorials on how to install and find this file if the shortcut I made has been removed or you are working on a different computer, the introduction to pyqt5 video has some advice) add the additional buttons with appropriate names so you can reference them easily. compile the code into the qt_designer.py file using the method described in the qtdesigner_files section. Then in the spectrometer_GUI.py file (this one) write the function that you want to connect to the button and connect it following the examples that are already written there.

# spectrometer.py

this is where the spectrometer class is created which is then imported and loaded in the spectrometer_GUI.py file. it will also store which devices to communicate with as well as what channels to use. If the channels are changed you will need to open this file and alter the channels appropriately

# workers

in order for us to be able to interrupt and update our UI in real time we have to use QThreads. The move.py file holds the class and the functions that the thread will run in, the thread being set up and connected occurs in the GUI.py file under the corresponding method name ex. move, scan. We have to use classes because when moving to a thread you cannot pass arguments so you have to store the arguments in a class and then move to a method of that class.

# miscellaneous.py

this is a file with a few functions that I need frequently or don't want to write in the existing functions as they would be uneccesarily large. Right now it consists of a function to make the header, a function to check if the filename is in use and return the next free filename and a precise clock.

# dependencies
1. numpy: pip install numpy
2. pyqt5: pip install pyqt5
3. nidaqmx: pip install nidaqmx
4. QChart: pip install PyQtChart


# additonal comments
this modular approach can be a bit confusing when looking at the whole picture, however it makes working with pieces of the code much easier and cleaner. I have done my best to make it clear, some things that may cause you trouble when first working with this directory or being new to classes.

1. Every method (a function inside a class) must take 'self' as its first variable this is just the way python is, and it allows classes to access their properties within a method.

2. when you add or access any variable stored in a class it must be proceeded by self.example where example is the property you are trying to access (when outside the function self is replaced by the name you assign to the class, for example; double = spectrometer(), to access the position use double.position).

3. in spectrometer.py there is a niche bit of code using a decorator, the @property above self.position and again below. What this does is allow us to write conditions on the assigning of a value, it really isn't complicated (you don't need to understand decorators) once you know what it does. There are good simple examples of the @property online.

4. threading, in order for our GUI to be responsive and update in real time we have to introduce threads using QThreads, these essentially allow us to do two things at once, the UI on it's own can't be collecting data and updating itself at the same time, so instead we make a thread to collect the data and emit it to the main UI update functions. Threads need only be used for long running processes for example a thread is not needed for the recalibrate function since it is near instant, however if you desire a responsive UI that can be interrupted the simplest method I know is QThread. I highly recommend the tutorial in learning resources for further informatin.

# learning resources

1. introduction to classes: https://www.w3schools.com/python/python_classes.asp
2. introduction to pyqt5 (first three videos are a good start): https://www.youtube.com/watch?v=Vde5SH8e1OQ&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj
3. why you shouldn't edit the qt_designer.py (it's a bit long winded): https://www.youtube.com/watch?v=XXPNpdaK9WA
4. @property: https://www.programiz.com/python-programming/property
5. how to interface with the daq: https://www.youtube.com/watch?v=umXMrr6Z0Og&t=589s
6. the code and examples for nidaqmx python library this is the best resource for documentation I have found https://github.com/ni/nidaqmx-python/blob/master/nidaqmx/_task_modules/ao_channel_collection.py
7. best tutorial I could find for QThread: https://realpython.com/python-pyqt-qthread/
