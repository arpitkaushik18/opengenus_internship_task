# opengenus_internship_task

It include two tasks:-
* Size of the webpage in bytes
* Number of links in that page pointing to same domain (find <a> tags)
## Getting Started

These instructions will tell you about the whole working flow of project.

### Prerequisites

These things you need to install

```
Pycharm IDE
```

### Working Flow
we can divide the whole task into 5 python scripts:-
* Demo.py :- This will create directory and txt file. it will also help to link them.apart from that we convert files to set data structure and set to files for increase fetching speed.

![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/Capture1.PNG?raw=true)

![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/Capture.PNG?raw=true)

* link_finder :- This will take bunch of html codes and extract links from it.

![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/link.PNG?raw=true)

* Spider.py :- This is our core part of web crawler. this will going to store all link from url into queue.txt file.

![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/Sp1.PNG?raw=true)

![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/Sp2.PNG?raw=true)

![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/Sp3.PNG?raw=true)

* Domain.py :- This will return the domain name so that we can extract only those links that are pointing to same domain.

![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/Domain.PNG?raw=true)

* main.py :- This is our main script that connect all python files and produce output according to input.
![alt tag](https://github.com/arpitkaushik18/opengenus_internship_task/blob/master/main.PNG?raw=true)

