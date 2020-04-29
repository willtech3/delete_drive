## A Script to Mass Delete Files From Google Drive

I've spent a decent amount of time searching on the internet for a "delete all" button on Google Drive so I can both free up space and have the option to cancel my Google One subscription. As far as I can tell, that doesn't exist and you need to delete files one by one and then empty the trash. That can take forever if you have hundreds of thousands of little files like I do.

**This is a short script that solves that problem.**

### How to use it starting from no technical knowledge (Windows or Mac)

#### Installing Necessary Dependencies to run the program

1. Install Python 3.6 or higher if you don't already have it
   - You can find Python 3.8 and instructions for installation at this link [Python Downloads](https://www.python.org/downloads/release/python-382/). **Make sure to pick the correct one for your operating system**
   - If you're on Windows make sure to check the **"add Python 3.8 to PATH"** checkbox when running the installer
2. Open a terminal
   - On a mac just type terminal in spotlight and one will come up
   - On windows type `cmd` in the search bar and hit enter
3. If Python installs correctly you should be able to run the command `python` in the terminal and see an interactive python interpreter come up.
   - type quit() to exit
4. Install the dependencies necessary to run the script
   - run the command below
   -  ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```


#### Setting up an unregistered Google Application so you can programatically access your own Google Drive data.

1. Open a browser and go to the [Google Drive API Site](https://developers.google.com/drive/api/v3/quickstart/python)
   - Click on the button that say "Python codelab"
   - You'll have already done most of steps 1 - 5 but feel free to read them over anyway
2. On the Python Codelab step 6 click the link [console.developers.google.com/start/api?id=drive](console.developers.google.com/start/api?id=drive)
   - Select the dropdown and click Create a Project.
   - Additionally the Google Drive API will be enabled for you automatically as well.
3. Next click, "Go to Credentials"
   - In the first dropdown just select **Google Drive API**
   - In the second dropdown select **Other UI (e.g. Windows, CLI tool)**
   - In the last question check the radio button labeled **User Data** 
   - Then click on the button "What credentials do I need?"
4. A dialog box should appear titled Set up OAuth consent screen.
   - Click on the SET UP CONSENT SCREEN button
   - Don't click any of the radio buttons and just click the CREATE button
5. Now you should be on the OAuth consent screen
   - In the Application name text box, put any name you'd like.
   - Skip the Application logo upload (it's optional as far as I can tell)
   - Fill in your own email in the Support Email drop down
   - Click on the Add scope button and it's important you check the following three check boxes
     - Google Drive API (with a lock next to it). Scope: **../auth/drive**
     - Google Drive API. Scope: **../auth/drive.appdata**
     - Google Drive API. Scope: **../auth/drive.file**
     - Then click the ADD button at the bottom left
6.  At the bottom of the form click the "Save" button and then you will be able to click "Submit for Verification"
7.  Now go back to the credentials screen and click the + CREATE CREDENTIALS dropdown at the top, then select OAuth Client ID
8.  Now you'll be given a choice of Application type. Choose the radio button labeled **Other**. 
     - In the name that drops down put anything you want and click on the create button.
9. Now you'll see a dialogue that says OAuth client created. Close it
    - All the way to the right under the **OAuth 2.0 Client IDs** you'll see a downward arrow. Click on it and your credentials will be downloaded automatically

#### Downloading the script and running it (The Easy Part)

1. Install Git
   - On windows you can find the installer at the following link [Git Bash](https://git-scm.com/download/win)
   - Most Mac's already come with Git installed
2. Clone the repository where the script is by running the following command
   - `git clone https://github.com/willtech/delete_drive`
3. Copy the credentials file you downloaded at the end of step 9 in the previous section to the root of the repository
4. Rename the file to `client_secret.json`
5. Run the script with `python del.py`

### Modifying the script

Lines 52-53 are where the script discriminates on what types of files to delete. Feel free to modify those lines to delete the files that you deem necessary.
