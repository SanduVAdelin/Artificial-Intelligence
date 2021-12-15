import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2, 2, 1

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_output_and = np.array([[0], [0], [0], [1]])
expected_output_or = np.array([[0], [1], [1], [1]])
expected_output_xor = np.array([[0], [1], [1], [0]])


hidden_weights = np.random.uniform(size=(inputLayerNeurons+1, hiddenLayerNeurons))
print(f'''
Ponderile primului neuron (w11, w12): {hidden_weights[0]}
Ponderile celui de-al doilea neuron (w21, w22) : {hidden_weights[1]}
Ponderile pentru stratul ascuns sunt : {hidden_weights[2]}''')


net_input = [] #z_vector
activation_values = [] #y
errors_values = [] #gamma
results = []


def backpropagation(ages, learning_rate, fun):
    global expected_output
    if fun == 1:
        expected_output = expected_output_and
    elif fun == 2:
        expected_output = expected_output_or
    elif fun == 3:
        expected_output = expected_output_xor
    for age in range(0, ages+1):
        for data_index in range(0, 4):
            net_input.clear()
            activation_values.clear()
            errors_values.clear()
            # Propagarea inainte
            for index in range(0, hiddenLayerNeurons):
                net_input.append(inputs[data_index][0] * hidden_weights[0][index] + inputs[data_index][1] * hidden_weights[1][index])
                activation_values.append(sigmoid(net_input[index]))

            net_input.append(activation_values[0] * hidden_weights[2][0] + activation_values[1] * hidden_weights[2][1])
            activation_values.append(sigmoid(net_input[2]))

            output_layer_error = activation_values[2] - expected_output[data_index][0]
            # print(activation_values[2])
            # print(expected_output[data_index][0])
            #
            # print(f'''
            # Output layer error : {output_layer_error}
            # ''')
            # print(f'''
            # Valoarea de activare in ultimul neuron este : {activation_values[2]}''')

            # Backpropagation
            for i in range(0, hiddenLayerNeurons):
                errors_values.append(
                    activation_values[i] * (1 - activation_values[i]) * (output_layer_error * hidden_weights[2][i]))

            for i in range(0, hiddenLayerNeurons):
                hidden_weights[2][i] = hidden_weights[2][i] - learning_rate * (output_layer_error * activation_values[i])

            for i in range(0, hiddenLayerNeurons):
                for j in range(0, hiddenLayerNeurons):
                    hidden_weights[i][j] = hidden_weights[i][j] - learning_rate * (errors_values[j] * activation_values[j])

            # print(f'''
            # Ponderile primului neuron (w11, w12): {hidden_weights[0]}
            # Ponderile celui de-al doilea neuron (w21, w22) : {hidden_weights[1]}
            # Ponderile pentru stratul ascuns sunt : {hidden_weights[2]}''')

            if age == ages:
                if activation_values[2] < 0.5:
                    results.append(0)
                else:
                    results.append(1)
    print(results)


if __name__ == '__main__':
    ages = int(input('Numarul de epoci : '))
    learning_rate = float(input('Rata de invatare : '))
    fun = int(input('''
    Selecteaza functia : 
    1.AND
    2.OR
    3.XOR
    '''))

    backpropagation(ages, learning_rate, fun)


