# ipoffice-xml-reader

## Description

A simple GUI Python application to parse user data from the 'users.xml' file made available by Avaya IP Office Server Edition Web Manager and save the custom report to an Excel spreadsheet (.xlsx).

Originally built in Pop!_OS 22.04.


## Important

To collect the 'users.xml' file, head to IPO Web Manager @ https://<IPO_IP_ADDR>:7070 --> Call Management --> Users --> Actions --> Export All
    * You will need an Administrator login in order to collect this file.


### Dependencies

* Python 3.x
* pandas
* BeautifulSoup
* openpyxl
* lxml
* customtkinter


### Installing

* Make a directory for the project and access it:
```
mkdir ipoffice-xml-reader && cd ipoffice-xml-reader/
```

* Create folder 'results' inside the repo directory:
```
mkdir results
```

* Clone this repository:
```
git clone https://github.com/gustavoakira-sw/ipoffice-xml-reader.git
```

* Install requirements:
```
pip install -r requirements.txt
```


### Executing program

* Option 1 (GUI) - Run the gui.py file:
```
python3 gui.py
```
![image](https://user-images.githubusercontent.com/125785377/223854635-471f0a25-cff4-48f1-9670-79e63ea4b10c.png)

* Select a tag from the menu

![image](https://user-images.githubusercontent.com/125785377/223854974-4e4386bb-b6aa-4467-a6eb-528b3da9524d.png)

* You can also type in your tag if you are familiar with it. The most usual/common tags are already embedded into the combobox.

![image](https://user-images.githubusercontent.com/125785377/223855172-3a262c77-565f-4ff7-b019-7d606e99efe7.png)

* Pick a file
* Run!
* The resulting report will be available inside the "results" folder as IPO_XML_report_YYYY_MM_DD_HH_MM_SS.xlsx
    * You can also check the terminal for a quick peek.



* Option 2 (CLI) - Run only the scripts/user_reader.py and pass the .xml file and chosen Tag as arguments:
```
python3 scripts/user_reader.py /home/$USER/ipoffice-xml-reader/users.xml --tags Last-Modified
```
The output should look like this:

```
user@machine:~/ipoffice-xml-reader$ python scripts/user_reader.py ../users.xml --tags Last-Modified
File selected: ../users.xml
Tags received: ['Last-Modified']
userchoice is: Last-Modified
                    Full Name  ...                    Last-Modified
0                  [John Doe]  ...  [Tue, 22 Nov 2022 09:42:28 GMT]
1                  [Jane Doe]  ...  [Tue, 22 Nov 2022 09:42:28 GMT]
...
231            [Peter Parker]  ...  [Fri, 16 Dec 2022 01:10:13 GMT]
232             [Bruce Wayne]  ...  [Fri, 16 Dec 2022 01:10:13 GMT]

[233 rows x 5 columns]
---- File IPO_XML_report_2023_03_08_18_34_21_919816.xlsx created successfully.
```


All logs are saved to the "./logs/" folder.


## Help

I am building this application in order to hone my Python skills, so there are a few bugs you can help with!

* [UI] Refresh search is not working properly
* [LOG] Log timestamp only shows the time the thread started


## Authors

Gustavo Akira
[@Mail me!](mailto:gustavoakira.ti@gmail.com)


## Acknowledgments

Inspiration, code snippets, etc.
* [Pandas](https://github.com/pandas-dev/pandas)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
