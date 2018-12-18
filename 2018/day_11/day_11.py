import pprint
pp = pprint.PrettyPrinter(indent=4, width=180).pprint

GRID_SIZE = 300
SERIAL_NUMBER = 1955


def power_level(x, y, serial_number=SERIAL_NUMBER):
  rack_id = x + 10
  power_level_start = rack_id * y
  power_level_plus_serial = power_level_start + serial_number
  power_level_multiplied_by_rack_id = power_level_plus_serial * rack_id
  hundreds_level_of_power_id = power_level_multiplied_by_rack_id // 100 % 10
  final_power = hundreds_level_of_power_id - 5
  return final_power


def get_upper_left_coords_of_max_power(serial_number=SERIAL_NUMBER, grid_size=3):
  power_dict = {
    (x, y): power_level(x, y, serial_number) for x in range(1, GRID_SIZE + 1) for y in range(1, GRID_SIZE + 1)
  }
  # pp(power_dict)

  three_by_three = {
    (x, y): sum([power_dict[(x + i, y + j)] for i in range(grid_size) for j in range(grid_size)
                ]) for x, y in power_dict if x + 2 <= GRID_SIZE and y + 2 <= GRID_SIZE
  }
  # pp(three_by_three)

  result = max(three_by_three, key=three_by_three.get)
  return '{},{}'.format(result[0], result[1])



def get_largest_submatrix_by_coords_and_size():
  power_grid = [[0 for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]

  for x in range(1, GRID_SIZE + 1):
    for y in range(1, GRID_SIZE + 1):
      power_grid[x][y] = power_level(x, y)

  # pp(power_grid)

  running_sum_power_grid = power_grid[:]

  for x in range(1, GRID_SIZE + 1):
    for y in range(1, GRID_SIZE + 1):
      running_sum_power_grid[x][y] = power_grid[x][y] \
                                     + power_grid[x - 1][y] \
                                     + power_grid[x][y - 1] \
                                     - power_grid[x - 1][y - 1]

  # pp(running_sum_power_grid)
  result = (0, (0, 0))

  for block_size in range(1, GRID_SIZE):
    for x in range(1, GRID_SIZE - block_size + 1):
      for y in range(1, GRID_SIZE - block_size + 1):
        tot = running_sum_power_grid[x + block_size][y + block_size] \
              - running_sum_power_grid[x][y + block_size] \
              - running_sum_power_grid[x + block_size][y] \
              + running_sum_power_grid[x][y]

        result = max(result, (tot, (x + 1, y + 1, block_size)))

  return result  # (171, (231, 108, 14))


if __name__ == '__main__':
  assert power_level(3, 5, 8) == 4
  assert power_level(217, 196, 39) == 0
  assert power_level(122, 79, 57) == -5
  assert power_level(101, 153, 71) == 4

  assert get_upper_left_coords_of_max_power(18) == '33,45'
  assert get_upper_left_coords_of_max_power(42) == '21,61'

  print(get_upper_left_coords_of_max_power())
  print(get_largest_submatrix_by_coords_and_size())
