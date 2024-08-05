distort = np.random.randint(0, 7)
# distort = 5
if distort == 0:
    # Normal
    final_array = [float(val) / 255 for val in line[2:].split(',')]
    final_matrix = np.reshape(final_array, (784, 1))
elif distort == 1:
    # Shift Right
    input_array = line[2:].strip().split(',')
    final_array = list()
    for x in range(28):
        row_list = np.array([float(i) / 255 for i in input_array[28 * x: 28 * (x + 1)]])
        row_list = np.roll(row_list, 1)
        final_array.append(row_list)
    final_matrix = np.array(final_array)
    final_matrix = np.reshape(final_matrix, (784, 1))
elif distort == 2:
    # Shift Left
    input_array = line[2:].strip().split(',')
    final_array = list()
    for x in range(28):
        row_list = np.array([float(i) / 255 for i in input_array[28 * x: 28 * (x + 1)]])
        row_list = np.roll(row_list, -1)
        final_array.append(row_list)
    final_matrix = np.array(final_array)
    final_matrix = np.reshape(final_matrix, (784, 1))
elif distort == 3:
    # Shift Up
    input_array = line[2:].strip().split(',')
    final_array = list()
    for x in range(28):
        row_list = np.array([float(i) / 255 for i in input_array[28 * x: 28 * (x + 1)]])
        final_array.append(row_list)
    final_matrix = np.array(final_array)
    final_matrix = np.roll(final_matrix, -1, 0)
    final_matrix = np.reshape(final_matrix, (784, 1))
elif distort == 4:
    # Shift Down
    input_array = line[2:].strip().split(',')
    final_array = list()
    for x in range(28):
        row_list = np.array([float(i) / 255 for i in input_array[28 * x: 28 * (x + 1)]])
        final_array.append(row_list)
    final_matrix = np.array(final_array)
    final_matrix = np.roll(final_matrix, 1, 0)
    final_matrix = np.reshape(final_matrix, (784, 1))
elif distort == 5:
    # Rotate Right 15 Degrees
    input_array = line[2:].strip().split(',')
    final_array = list()
    for x in range(28):
        row_list = np.array([float(i) / 255 for i in input_array[28 * x: 28 * (x + 1)]])
        final_array.append(row_list)
    final_matrix = ndimage.rotate(final_array, 15, reshape=False)
    final_matrix = np.array(final_matrix)
    final_matrix = np.reshape(final_matrix, (784, 1))
elif distort == 6:
    # Rotate Left 15 Degrees
    input_array = line[2:].strip().split(',')
    final_array = list()
    for x in range(28):
        row_list = np.array([float(i) / 255 for i in input_array[28 * x: 28 * (x + 1)]])
        final_array.append(row_list)
    final_matrix = ndimage.rotate(final_array, -15, reshape=False)
    final_matrix = np.array(final_matrix)
    final_matrix = np.reshape(final_matrix, (784, 1))
normed_data_set.append((final_matrix, output))