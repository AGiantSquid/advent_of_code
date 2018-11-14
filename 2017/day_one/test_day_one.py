from day_one import captcha_sequence_solver

def test_captcha_sequence_solver():
  cases = [
    {
      'multidigit_int': 1122,
      'expected_result': 3,
    },
    {
      'multidigit_int': 1111,
      'expected_result': 4,
    },
    {
      'multidigit_int': 1234,
      'expected_result': 0,
    },
    {
      'multidigit_int': 91212129,
      'expected_result': 9,
    },
  ]
  for case in cases:
    assert captcha_sequence_solver(case['multidigit_int']) == case['expected_result']
