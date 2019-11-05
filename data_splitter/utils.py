def split_array(data, val_perc, test_perc):
  """
  Returns a tuple of sliced parts of data corresponding to the percentages given in perc

  Keyword arguments:
    data -- list to be split
    val_perc -- proportion of validation set
    test_perc -- proportion of test set
  """
  val_idx = int(val_perc * len(data))
  test_idx = int(test_perc * len(data))
  val_data = data[0:val_idx]
  test_data = data[val_idx:(val_idx+test_idx)]
  train_data = data[(val_idx+test_idx):]

  return((train_data, val_data, test_data))



