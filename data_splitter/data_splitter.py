from os import listdir, mkdir
from os.path import isfile, isdir, join
import sys
import random

from shutil import move, rmtree
import click

from .utils import split_array

@click.command()
@click.argument('folder')
@click.option('--val' , default=20, help="Percentage of files for validation set")
@click.option('--test', default=20, help="Percentage of files for test set")
def data_splitter(folder, val, test):
  entries = [item for item in listdir(folder) if not item.startswith('.')]

  # Get all folders and files
  dirs = [d for d in entries if isdir(join(folder, d))]
  files = [f for f in entries if isfile(join(folder, f))]

  if dirs and files:
    print("Folder should contain either files or folders but not both.")
    sys.exit()

  mkdir(join(folder, 'train'))
  mkdir(join(folder, 'validation'))
  mkdir(join(folder, 'test'))

  if files:
    dirs = [""]

  for directory in dirs:
    # Items belonging to the current class
    items = [item for item in listdir(join(folder, directory)) if not item.startswith('.') and isfile(join(folder, directory, item))]

    if directory != "":
      mkdir(join(folder, 'train', directory))
      mkdir(join(folder, 'validation', directory))
      mkdir(join(folder, 'test', directory))

    # Shuffle and split dataset according to fractions
    random.shuffle(items)
    train_entries, val_entries, test_entries = split_array(items, val, test)

    for train_file in train_entries:
      move(join(folder, directory, train_file), join(folder, 'train', directory, train_file))
    for val_file in val_entries:
      move(join(folder, directory, val_file), join(folder, 'validation', directory, val_file))
    for test_file in test_entries:
      move(join(folder, directory, test_file), join(folder, 'test', directory, test_file))

    if directory != "":
      rmtree(join(folder, directory))


if __name__ == '__main__':
  try:
    data_splitter()
  except FileNotFoundError as fnf_error:
    print(fnf_error)