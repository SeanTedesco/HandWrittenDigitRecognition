# Stochastic Gradient Descent

# Perceptron Neuron
Definition: an artificial neuron, A perceptron takes several binary inputs, x1, x2, ..., and produces a single binary output.

- The perceptron's output, 0 or 1, is determined by whether the weighted sum ∑jwjxj is less than or greater than some threshold value.
- A way you can think about the perceptron is that it's a device that makes decisions by weighing up evidence.

# Sigmoid Neuron
- similar to perceptrons, but modified so that small changes in their weights and bias cause only a small change in their output.
- Just like a perceptron, the sigmoid neuron has inputs, x1,x2, ..., but instead of being just 0 or 1, these inputs can also take on any values between 0 and 1. So, for instance, 0.638... is a valid input for a sigmoid neuron.
- Also just like a perceptron, the sigmoid neuron has weights for each input, w1,w2,…, and an overall bias, b. But the output is not 0 or 1. Instead, it's σ(w⋅x+b), where σ is called the sigmoid function*

# Weights
Definition: a real number expressing the importance of the respective inputs to the output.

# Bias
Definition: a real number that indicates a measure of how easy it is to get the perceptron to output a 1