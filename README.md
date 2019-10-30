# capacitor_plotting

Python script to plot real data vs. regression data of the voltage across a capacitor.

### Dependencies
1. [python3](https://www.python.org/) & [pip](https://bootstrap.pypa.io/get-pip.py) (check beforehand if it is already installed)
2. [numpy](https://pypi.org/project/numpy/)
3. [matplotlib](https://pypi.org/project/matplotlib/)

### Usage
1. Clone this repository
2. ``python plotting.py <.csv file>`` (standard is: data.csv)

### Specification of .csv input format
Filename: data.csv (can be changes using function_plotting.py <.csv file>)

First line: Title of the graph

Second line: Label for the x-axis

Third line: Label for the y-axis 

Fourth line: Range tuple (startvalue, endvalue, step)

Fifth line: Ignored line (e.g. dashes or blank line) to seperate the header from the actual data

Following lines: y values (data) - seperated by commata

There is a sample file called data.csv in the same directory as this script.

### Sample output
![plotting.py output](./Capacitor.png)

### Documentation
The script ``plotting.py`` is well commented. There is a large block comment
at the top mostly providing a mathematical explanation.