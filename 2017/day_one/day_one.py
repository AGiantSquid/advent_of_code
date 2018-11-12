def captcha_sequence_solver(int_sequence):
  listified = list(str(int_sequence))
  listified.append(listified[0])
  prior_el = ''
  sum_of_sequences = 0
  for el in listified:
    if el == prior_el:
      sum_of_sequences += int(el)
    prior_el = el
  return sum_of_sequences
