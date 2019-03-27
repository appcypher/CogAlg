from Operations import Compare as comp

input_ = [(0, 0, 15), (0, 1, 18), (0, 2, 5),
          (1, 0, 19), (1, 1, 20), (1, 2, 18),
          (2, 0, 25), (2, 1, 35), (2, 2, 32)]

output_ = comp(input_, offset=(1, 0))

for i in range(0, len(output_), 3):
    print(output_[i:i+3])

print('\n')

input_ = [(0, 0, 0, 15), (0, 0, 1, 18), (0, 0, 2, 5),
          (0, 1, 0, 19), (0, 1, 1, 20), (0, 1, 2, 18),
          (0, 2, 0, 25), (0, 2, 1, 35), (0, 2, 2, 32),

          (1, 0, 0, 25), (1, 0, 1, 28), (1, 0, 2, 15),
          (1, 1, 0, 19), (1, 1, 1, 20), (1, 1, 2, 28),
          (1, 2, 0, 35), (1, 2, 1, 45), (1, 2, 2, 42),

          (2, 0, 0, 35), (2, 0, 1, 38), (2, 0, 2, 25),
          (2, 1, 0, 39), (2, 1, 1, 40), (2, 1, 2, 38),
          (2, 2, 0, 55), (2, 2, 1, 55), (2, 2, 2, 52)]

output_ = comp(input_, offset=(1, -1, 1), comparand=3, axes=(0, 1, 2))

for i in range(0, len(output_), 3):
    print(output_[i:i+3])
    if i % 9 == 6:
        print('\n')