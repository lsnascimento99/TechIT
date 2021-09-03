import numpy as np

memoization = {}
def visualize_neuron(neural_network, layer, selected_neuron):

	# 
	try:
		return memoization[str(layer+selected_neuron)]
	except:
		pass
		
	number_input_neurons = neural_network["weights"][0].shape[0]
	weights = neural_network['weights'].flatten()
	biases = neural_network['biases'].flatten()

	if layer==0: return np.ones(number_input_neurons) # Input layer - no need to make a linear combination

	prev_weight_layer = weights[layer-1]
	vector = []
	# Get all incoming connections in previous layer to make the vector
	for n in xrange(len(prev_weight_layer)):
		connection_strength = prev_weight_layer[n][selected_neuron] # Weight from this neuron to selected
		incoming_weight = connection_strength*get_neuron(layer-1, n)
		vector.append(incoming_weight)
	vector = np.array(vector)
	if layer==1:
		vector= np.array(vector.diagonal())
	else:
		vector = np.sum(vector, axis=0)
	vector+=biases[layer-1][selected_neuron] # Add the bias from previous weight layer
	memoization[str(layer)+str(selected_neuron)]=vector
	return vector