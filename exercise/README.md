## Setup
In de terminal onderin het scherm moet je het volgende zien:
`@username -> /workspace/exercise/src` 
Als je in een andere folder zit ga naar deze folder.

## De app draaien
Run de volgende command in de terminal:
`$ uv run fastapi dev`
Na een tijdje moet je output er zo uitzien:
![terminal output](docs/startup-output.png)

Als je hierin met ctrl ingedrukt op de `http://127.0.0.1:8000` drukt open je de app.

Door de URL waar je naar toegestuurd wordt te appenden met `/docs` (let erop, geen extra `/` op het einde!) kan je de Swagger UI zien, met daarin alle API endpoints uitgelegd.


## Assignments

### 0a. Preparation for local development
0. Create a [Github account](github.com)
1. Install the required programs:
  * [git](https://git-scm.com/install/)
  * Install [Python](https://www.python.org/downloads/)
  * Install [Visual Studio Code](https://code.visualstudio.com/download)
2. Configure git to use your github account credentials
3. Install the python dependencies: in a terminal type: `pip install uv`
4. Clone the repository locally using the `git clone` command in your terminal

### 0b Preparation for online development
0. Create a [Github account](github.com)
1. Go to this repository
2. Open a codespace on the `master` branch

### 1. Git Basics
0. Run the FastAPI application
1. Create a new route in the `app.py` file, and sync your changes
   After this, commit and push your changes to the master branch
2. Pull changes from the remote
