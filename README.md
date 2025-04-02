# Battleships Game

## Description
This is the Battleships Game that runs in almost any Python terminal, a program with the purpose of offering a different version of the game of Battleship to the user, challenging them with having both luck and strategy to win the game. A challenger must sink all the opponent's battleships before their battleships are sunk in order to claim victory.

## How To Play
In this version of the Battleship game a player plays against a computer opponent with both player's randomly generated game boards
Each Players squares they select during the game are marked either with an - for a Miss, or an X for a Hit on the opponent's ship
The Player and the computer take turns guessing where the opponent's ships are to sink all the opponent's remaining battleships
The winner is whoever sinks all their opponent's battleships first

## Features
### Existing Features
- Random board generation
    - Both the player's and the opponent's ships are randomly placed on each game board
    - The player cannot see the opponent's ships until the hit a correct square in the game
- Intruction message
    - Instructions summary given to the user on how to use the program and play the game
    - Also a reminder they can exit the program at any time by closing the terminal
- Input validation and error checking
    - Player cannot enter an invalid player name
    - Player cannot enter numbers too low or too high
    - Player cannot enter letter past I
    - Player cannot enter text or special characters for row numbers
    - Player cannot enter numbers or special characters for column letters

### Future Features
- Allow player to place their ships manually
- Keep track of how many games the player has won already
- Allow the user to increase the size of the board and increase the challenge of the game

## Technologies Used
-  Python was used as the foundation coding of this game
- VSCode was used as the main tool to manage project files/folders, write and edit code, upload Commit changes, and upload images
- Git was used for the version control of the site
- GitHub was used to host the code of this site
- GitHub Pages was used to host the live version of this site

## Testing
### Manual Testing
I have manually tested this project with the following:
- Passed the code through PEP8 linter and confirmed there were no series errors, no runtime errors, just warningings about the length of some of the lines of code
- Given invalid inputs inucluding numbers and letters out of range of the program, the same input square twice
- Tested in my local terminal in VS code
- Tested in a Python Integration Environment known as Python IDLE version 3.13(64-bit)

### Manual Testing Results
#### PEP8 Linter
![image](https://github.com/user-attachments/assets/cd456dc6-2b61-4480-8dde-6c30b2aead85)
![image](https://github.com/user-attachments/assets/82b032c4-0c24-427f-a0ed-864b0c128b2b)

#### VS Code




### Responsiveness
- This site was tested by chrome tool https://responsivedesignchecker.com/
?????>

### Validator Testing
#### HTML
- No errors were found when scanned through the official ????>

#### CSS
- No errors were found when scanned through the official ?????>


## Deployment
###Deployment from GitHub Pages
This site was deployed to GitHub pages, the steps to deploy are as follows:
- In the GitHub repository, navigate to the Settings tab
- From the source section drop-down menu, select the Main Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
- The live link can be found here: https://programcodemastera.github.io/top-quiz/

###Deployment from VS Code
This site can also be cloned to make a local copy that can be launched via VS Code Command Line Terminal, the steps are as follows:
- Navigate to your PC Documents > vscode-projects
- Right click in the current project folder and selecet Open Terminal while in vscode-projects
- Type in and Enter: git clone https://github.com/ProgramCodeMasterA/battleships-game.git
- Type in and Enter: cd top-quiz
    - now you have navigated to the clone project folder named after the project official name: battleships-game
- Type in and Enter: code .
  - this launches the IDE VS Code for the top-quiz project clone that is now stored locally on your PC

## Credits
### Content
- Inspiration for the Object Oreinted programming design oriniated from w3schools, Python tutorial link can be found here: https://www.w3schools.com/python/python_classes.asp
- ?????>


## Acknowledgements
- code created by User cloud2236863496 from the codecademy discussion forum website was used in the implementation of this project, specifically the freely available Python code was studied and modified to create this project run.py file, link to original code can be found here: https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605
- Jmanrique-bim github repository "Code_Academy_BattelshipGame" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/Jmanrique-bim/Code_Academy_BattelshipGame/tree/main
- i-m-itch github repository "Battleship-Terminal-Game" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/i-m-itch/Battleship-Terminal-Game
- code created by User samcp01 from from the codecademy discussion forum website was used in the implementation of this project, specifically the freely available Python code was studied and modified to create this project run.py file, link to original code can be found here: https://discuss.codecademy.com/t/python-battleship-game/679583
- gbrough github repository "battleship" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/gbrough/battleship/tree/main
- VJMonk github repository "Battleship-terminal-game" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/VJMonk/Battleship-terminal-game/tree/main
- Wikipedia for battleship game board layout, website link can be fund here: https://en.wikipedia.org/wiki/Battleship_(game)
- Code Institute tutors, provided learning material, Student Care team and Slack community members for their advice, recommendations, support and help
- Code Institute tutor Julia Konovalova, providing deployment instruction to deploy Python code to the online platform Render

