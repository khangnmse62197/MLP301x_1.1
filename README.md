# Test Grade Calculator

Test Grade Calculator is a Python project to grade the exams for many classes with a class size of thousand students. Main features: 
1. Open requested external text files with exception-handling
2. Scan each line of the exam answers for valid data and provide a corresponding report
3. Grade each exam based on the rubric provided and report
4. Generate an appropriately-named result file

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install NumPy.

```bash
pip install numpy
```
Another way and more details to install Numpy can be found here [Installing NumPy](https://numpy.org/install/)
## Usage

```bash
python khang_nguyen_grade_the_class.py
```
```bash
Enter a class to grade (i.e. class1 for class1.txt): class1
```
Sample output:
```bash
**** ANALYZING ****
No errors found!
**** REPORT ****
Total valid lines of data:20
......
```
If you want to continue using the program please type y
```bash
Continue[y/N]: N
Bye!
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)