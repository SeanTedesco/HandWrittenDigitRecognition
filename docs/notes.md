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

# Layers
## Design of Input and Output
The design of the input and output layers in a network is often straightforward. For example, suppose we're trying to determine whether a handwritten image depicts a "9" or not. A natural way to design the network is to encode the intensities of the image pixels into the input neurons. If the image is a 64 by 64 greyscale image, then we'd have 4,096=64×64 input neurons, with the intensities scaled appropriately between 0 and 1. The output layer will contain just a single neuron, with output values of less than 0.5 indicating "input image is not a 9", and values greater than 0.5 indicating "input image is a 9 ".

## Hidden Layer
- The middle layer is called a hidden layer, since the neurons in this layer are neither inputs nor outputs.

# Networks
## Feed-Forward Neural Networks
- neural networks where the output from one layer is used as input to the next layer.
- no loops in the network - information is always fed forward, never fed back. 
- if loops, we'd end up with situations where the input to the σ function depended on the output. 

# Recurrent Neural Networks
- neural networks in which feedback loops are possible.
- neurons which fire for some limited duration of time, before becoming quiescent. 
- firing can stimulate other neurons, which may fire a little while later, also for a limited duration.
- loops don't cause problems in such a model, since a neuron's output only affects its input at some later time, not instantaneously.
- recurrent neural nets have been less influential than feedforward networks:
    - learning algorithms for recurrent nets are (at least to date) less powerful.
    - they're much closer in spirit to how our brains work than feedforward networks.
    - possible that recurrent networks can solve important problems which can only be solved with great difficulty by feedforward networks.

# Cost Function
What we'd like is an algorithm which lets us find weights and biases so that the output from the network approximates y(x) for all training inputs x. To quantify how well we're achieving this goal we define a cost function.

Here, w denotes the collection of all weights in the network, b all the biases, n is the total number of training inputs, a is the vector of outputs from the network when x is input, and the sum is over all training inputs, x.

The notation ‖v‖ just denotes the usual length function for a vector v. We'll call C the quadratic cost function; it's also sometimes known as the mean squared error or just MSE. Inspecting the form of the quadratic cost function, we see that C(w,b) is non-negative, since every term in the sum is non-negative. Furthermore, the cost C(w,b) becomes small, i.e., C(w,b)≈0, precisely when y(x) is approximately equal to the output, a, for all training inputs, x. So our training algorithm has done a good job if it can find weights and biases so that C(w,b)≈0. By contrast, it's not doing so well when C(w,b) is large - that would mean that y(x) is not close to the output a for a large number of inputs. So the aim of our training algorithm will be to minimize the cost C(w,b) as a function of the weights and biases. In other words, we want to find a set of weights and biases which make the cost as small as possible.