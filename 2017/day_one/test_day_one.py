def test_captcha_sequence_solver():
  cases = [
    {
      'multidigit_int': 1122,
      'expected_result': 3,
    },
  ]
  for case in cases:
    assert captcha_sequence_solver(case['multidigit_int']) == case['expected_result']
