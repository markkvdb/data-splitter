# data-splitter

Simple command line program that splits folder in train and test set. The user provides a folder with files and the program will split the files over a train and test folder within the given folder.

## Installation

```pip install git+https://github.com/markkvdb/data-splitter.git#egg=data-splitter```

The installer will place the executables **data_splitter** in your $PATH.

## Usage

Call the script from the command line. The help page is as follows.

```bash
Usage: data_splitter.py [OPTIONS] FOLDER

Options:
  --train INTEGER  Percentage of files for train set.
  --help           Show this message and exit.
```

If you specify the *--train* flag between 0 and 100 you can set the percentage of files that should go into the train folder.