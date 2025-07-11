# We-are-laying-out-an-online-library

## Project Description
This project provides a Python script that takes data from a *`json file`* using the [json](https://pythonworld.ru/moduli/modul-json.html) library, creates *`html files`* using a template using [jinja2](https://pypi.org/project/Jinja2/), each of which contains 10 books that are in the *`pages`* folder, then when you run the `python file: python render_website.py` localhost is displayed, when you click on it, the first page of the site opens (after installing the project, you can work offline)

## Opening a website
To open a website in a browser, follow [link](https://aw1ks.github.io/We-are-laying-out-an-online-library/pages/index1.html)
### Open the site offline
1. Download the project to your computer (click the `Code` button, select `Download ZIP`, then unzip the downloaded folder)
2. Open the downloaded project in the code editor
3. Install dependencies `pip install -r requirements.txt`
4. Start the server with the command `python render_website.py` in the console localhost will be displayed, it looks like this [http://127.0.0.1:5500](http://127.0.0.1:5500) go to it and the first page of the site will be displayed
5. Open [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/?hl=ru) and refresh the page. Select the `Network` tab, you will see all the files that the browser uses to load this page.
6. Disconnect the Internet and refresh the site, you will see the files that were not downloaded, they will be highlighted in red.
7. Download the files that are highlighted in red to your computer: right-click on them and press `Open in new Tab` then right-click and download the file.
8. Next, replace the links with those that lead to the downloaded files (On the Network tab, in the Iniciator column, it is shown where each file was connected)

## How to launch
### Dependencies
To install libraries, download the project and install requirements.txt:
```
pip install -r requirements.txt
```
### Running the script
Run the script with the command:
```
python render_website.py
```
or
```
python online_library.py --info_folder your_folder --pages_folder your_folder
```
where `your_folder` is the folder with your book data.

Also, when running the script with the command:
```
python render_website.py -h
```
you can read what each argument means. 
