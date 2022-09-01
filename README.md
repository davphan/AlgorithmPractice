# Algorithm Data Visualizer App

Welcome to [David Phan's](https://gpa0verkd.github.io/Portfolio/) Algorithm
Visualization app! This project is built from scratch using pygame to animate
and render the application, and made both to practice coding in python and
to help myself (and others if they find this) on visualizing and understanding
algorithms in computer science!

This is completely free to use, both the code base and the app itself, as I'd
love the opportunity to help others understand coding concepts if I can, so
use anything to your heart's content! However, I'd appreciate it if you let me
know if you're using any of my code or the app :) You can find my contact info
in the link above on my name!

## Dependencies
This data visualizer only uses pygame to run, so make sure to run

> `npm install pygame`

before running the app.

---

## Getting started
*Note: currently in development, so no .exe file quite yet to download.*

To run the app while developing, run the `App.py`. This can either be done
through an IDE's run button or by running

> python App.py

in the command line. Note that your current directory must be the top of the
**AlgorithmPractice** folder.

---

## Notes on directory structure
### GameFiles
> The GameFiles folder holds the code for any
> **parts that need functionality in multiple screens**. This includes the array
> element blocks, for example, which can be used in every screen that needs to
> display an array.
### Screens
> The Screens folder holds the functionality for every screen and screen change.
> App.py initializes the `Home.py` screen, and any screen after that is built on top
> of the home screen. To return home, just break the current screen's while loop.
### Common.py
> The `Common.py` file holds simple methods that are used everywhere. It differs
> from the GameFiles folder by its simplicity (only functions instead of classes)
> and very frequent use cases, and should be imported to every file.

# Patch Notes
*Nothing yet since its not done yet hehe but patch notes sounds like a cool*
*idea to fix bugs and add new content in the future!*