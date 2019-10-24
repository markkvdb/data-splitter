import os
import random

import shutil
import click

@click.command()
@click.argument('folder')
@click.option('--train', default=80, help="Percentage of files for train set")
def data_splitter(folder, train):
  entries = os.listdir(folder)

  os.mkdir(folder + '/train/')
  os.mkdir(folder + '/test/')

  random.shuffle(entries)

  train_sel = int(len(entries) * (train / 100))
  train_entries = entries[0:train_sel]
  test_entries = entries[train_sel:]

  for train_file in train_entries:
    shutil.move(folder + '/' + train_file, folder + '/train/' + train_file)
  for test_file in test_entries:
    shutil.move(folder + '/' + test_file, folder + '/test/' + test_file)

if __name__ == '__main__':
    data_splitter()