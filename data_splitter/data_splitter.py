from os import listdir, mkdir, rmdir
from os.path import isfile, isdir, join
import sys
import random

import shutil
import click

@click.command()
@click.argument('folder')
@click.option('--train', default=80, help="Percentage of files for train set")
def data_splitter(folder, train):
  entries = [item for item in listdir(folder) if not item.startswith('.')]

  # Get all folders and files
  dirs = [d for d in entries if isdir(join(folder, d))]
  files = [f for f in entries if isfile(join(folder, f))]

  if dirs and files:
    print("Folder should contain either files or folders but not both.")
    sys.exit()

  mkdir(join(folder, 'train'))
  mkdir(join(folder, 'test'))

  if files:
    dirs = [""]

  for directory in dirs:
    # Items belonging to the current class
    items = [item for item in listdir(join(folder, directory)) if not item.startswith('.') and isfile(join(folder, directory, item))]

    if directory != "":
      mkdir(join(folder, 'train', directory))
      mkdir(join(folder, 'test', directory))

    # Shuffle and split dataset according to fractions
    random.shuffle(items)
    train_sel = int(len(items) * (train / 100))
    train_entries = items[0:train_sel]
    test_entries = items[train_sel:]

    for train_file in train_entries:
      shutil.move(join(folder, directory, train_file), join(folder, 'train', directory, train_file))
    for test_file in test_entries:
      shutil.move(join(folder, directory, test_file), join(folder, 'test', directory, test_file))

    if directory != "":
      rmdir(join(folder, directory))


if __name__ == '__main__':
  try:
    data_splitter()
  except FileNotFoundError as fnf_error:
    print(fnf_error)