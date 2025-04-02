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
![image](https://github.com/user-attachments/assets/492bf9a3-ea1e-4d69-86ee-9899994e5732)
![image](https://github.com/user-attachments/assets/8b47accb-047b-4426-bfb6-668e73686e0d)

#### Python IDLE
![image](https://github.com/user-attachments/assets/ae195e16-168f-48fa-9cce-329df97755ce)
![image](https://github.com/user-attachments/assets/8752e379-582d-4791-9261-983520bb4b40)

### Remaining Bugs
- There are a few bugs with the length of some of the lines of code but nothing that affects the execution of the program

### Validator Testing
#### PEP8
- No major errors were found when scanned through the PEP8online.com
- A few minor errors were reported with the length of some of the lines of code

## Deployment
###Deployment from 
- The program can be reached by the [[link](htt)](https://battleships-game-1.onrender.com)
### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/ProgramCodeMasterA/battleships-game).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/ProgramCodeMasterA/battleships-game.git`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ProgramCodeMasterA/battleships-game.git)

  1. Install Python module dependencies:
     
      1. Navigate to the folder madlib_with_python by executing the command:
      - `cd madlib_with_python`
      1. Run the command pip install -r requirements.txt
        - `pip3 install -r requirements.txt`
      1. *Note:* If you are located in China ![China](https://www.countryflags.io/cn/flat/32.png) or any other country with restricted internet access, you may need to add the following code in order to be able to use the nltk package.
      
       - For example:

        ```python
        nltk.set_proxy('127.0.0.1:41091')
        ```
      - To set the proxy, you need to open setting in preferred VPN, find Server address and HTTP/HTTPS Proxy Port joining them by colons as it is shown in the example above:
      ![Settings VPN](documentation/deployment/settings_vpn.png)


### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/ProgramCodeMasterA/battleships-game.git`

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`
  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  1. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

      - ![New Heroku App](documentation/deployment/new_heroku_app.png)

  1. Go to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)

      - ![Deployment Method](documentation/deployment/deployment_method.png)

  1. Link your GitHub account and connect the application to the repository you created.

      - ![Link GitHub account](documentation/deployment/link_to_github.png)

  1. Go to the Settings tab:
  
      - ![Settings Tab](documentation/deployment/settings_tab.png)

  1. Click "Add buildpack":

      - ![Add Buildpack](documentation/deployment/add_buildpack.png)

  1. Add the Python and Node.js buildpacks in the following order:

      - ![Add Python and Node.js](documentation/deployment/add_python_and_node_js.png)

  1. Click "Reveal Config Vars."

      - ![Reveal Config Vars](documentation/deployment/reveal_config_vars.png)

  1. Add 1 new Config Vars:
      - Key: PORT Value: 8000
      - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.

  1. Go back to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)

  1. Click "Deploy Branch":

      - ![Deploy Branch](documentation/deployment/deploy_branch.png)

      - Wait for the completion of the deployment.

      - ![Deploying Branch](documentation/deployment/deploying_branch.png)

  1. Click "Open app" to launch the application inside a web page.

      - ![View Button](documentation/deployment/view_app.png)


### To deploy the project to Render so it can be run as a remote web application:

Link to the deployed application on Render: [battleships-game](https://battleships-game-1.onrender.com)

1. Create a new Render account if you don't already have one here [Render](https://render.com/).

2. Create a new application on the following page here [New Render App](https://dashboard.render.com/), choose **Webserver**:

    - ![New Render App](documentation/deployment/render_new_web_service.png)

3. Select the GitHub option and connect the application to the repository you created.

    - ![GitHub Option](documentation/deployment/render_configure_github_account.png)

4. Search for the repository you created and click "Connect."

    - ![Connect to GitHub](documentation/deployment/render_connect_repository.png)

    - ![Connect to GitHub](documentation/deployment/render_connect_repository_connect.png)

5. Create name for the application

    - ![Create Application Name](documentation/deployment/render_create_name.png)

6. Select the region where you want to deploy the application.

    - ![Select Region](documentation/deployment/render_select_region.png)

7. Select branch to deploy.

    - ![Select Branch](documentation/deployment/render_select_branch.png)

8. Select environment.

    - ![Select Environment Variables](documentation/deployment/render_select_environment.png)

9. Render build command: `pip3 install -r requirements.txt && npm install`

    - ![Render Build Command](documentation/deployment/render_build_command.png)

10. Render start command: `node index.js`

    - ![Render Start Command](documentation/deployment/render_start_command.png)

11. Select Free plan.

    - ![Select Free Plan](documentation/deployment/render_payment_info.png)

12. Click on "Advanced" settings.

    - ![Advanced Settings](documentation/deployment/render_advanced_settings.png)

13. Add the following environment variables:

    - Key: PORT Value: 8000
    - Key: PYTHON_VERSION Value: 3.10.7

    - ![Add Environment Variables](documentation/deployment/render_advanced_settings_variables.png)

14. Click "Create Web Service."

    - ![Save Web Service](documentation/deployment/render_create_web_service.png)

15. Wait for the completion of the deployment.

### Deployment from VS Code
This site can also be cloned to make a local copy that can be launched via VS Code Command Line Terminal, the steps are as follows:
- Navigate to your PC Documents > vscode-projects
- Right click in the current project folder and selecet Open Terminal while in vscode-projects
- Type in and Enter: git clone https://github.com/ProgramCodeMasterA/battleships-game.git
- Type in and Enter: cd top-quiz
    - now you have navigated to the clone project folder named after the project official name: battleships-game
- Type in and Enter: code .
  - this launches the IDE VS Code for the top-quiz project clone that is now stored locally on your PC

 ### Deployment in Python IDLE
 - This site can also be cloned to make a local copy that can be launched via Python IDLE
 - Navigate to your PC Documents > vscode-projects
 - Right click on the run.py file and select Open With > Python
    - this launches the program in the Python Integrated Development Environment

## Credits
### Content
- Inspiration for the Object Oreinted programming design oriniated from w3schools, Python tutorial link can be found here: https://www.w3schools.com/python/python_classes.asp
- Inspiration for the way in which the battleship game would operate came from discuss.codecamp forums, this design was chosen for ease of use for the user and to minimize the program runtime
- Inspiration for the battleship game board design was taken from the orignal games design 10x10 board, Wikipedia link can be found here: https://battleship.fandom.com/wiki/Battleship_(game)

## Acknowledgements
- code created by User cloud2236863496 from the codecademy discussion forum website was used in the implementation of this project, specifically the freely available Python code was studied and modified to create this project run.py file, link to original code can be found here: https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605
- Jmanrique-bim github repository "Code_Academy_BattelshipGame" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/Jmanrique-bim/Code_Academy_BattelshipGame/tree/main
- i-m-itch github repository "Battleship-Terminal-Game" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/i-m-itch/Battleship-Terminal-Game
- code created by User samcp01 from from the codecademy discussion forum website was used in the implementation of this project, specifically the freely available Python code was studied and modified to create this project run.py file, link to original code can be found here: https://discuss.codecademy.com/t/python-battleship-game/679583
- gbrough github repository "battleship" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/gbrough/battleship/tree/main
- VJMonk github repository "Battleship-terminal-game" was used in the implementation of this project, specifically the repository Python code was studied and modified to create this project run.py file, link to original github repository code can be found here: https://github.com/VJMonk/Battleship-terminal-game/tree/main
- Wikipedia for battleship game board layout, website link can be fund here: https://en.wikipedia.org/wiki/Battleship_(game)
- Code Institute tutors, provided learning material, Student Care team and Slack community members for their advice, recommendations, support and help
- Code Institute tutor Julia Konovalova, providing deployment instruction to deploy Python code to the online platform Render and README instructions for Render
