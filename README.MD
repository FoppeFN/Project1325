Project1

Prerequisites: Have miniconda, visual studio code, git (if pushing to repository) and a working python compiler, if you have miniconda, you can use your environment as your compiler.

Step 1: Download Ollama from github

https://github.com/ollama/ollama

Here is the link to the github, follow the readme from their github in order to install it if you are on macOS or linux, I will be going over the installation for windows, click on the download link under the windows button.

Step 2: Click on the exe after it is installed on your computer and make sure the install is complete. Go through the setup as normal, it may take a while. Then go to your search bar and type in ollama, click and nothing will appear, congratulations, you have failed the installation!

just kidding you did it all right, thats just how ollama works.

Step 3: Type in command prompt into your search bar, click on it and type ollama into your command prompt, if you get something to return like "Usage: ollama [flags]" you installed it correctly

Step 4: Now go back to their github page and look at the models that they have, simply copy the command and run it and it will install that model locally, like "ollama run llama3.3" now llama 3.3 will install on your computer.

Step 5: Remember, if you want to use the model in order to accomplish something like I did, you have to import the library, and do model="phi:3latest" or some other model and do client = ollama.Client()

Congrats! now you have your LLM finally installed on your machine and can use it to do whatever you want, you can use it to do something similiar that I have accomplished or not. I am going to link a very useful youtube video that shows you all the different things that you are able to do with this installed llm on your computer that I used to get started.

https://www.youtube.com/watch?v=UtSSMs6ObqY&t=652s
