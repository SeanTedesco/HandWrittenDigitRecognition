# Chapter 1

## Sigmoid Neurons Simulating Perceptrons, Part I 

**Q:** Suppose we take all the weights and biases in a network of perceptrons, and multiply them by a positive constant, c>0. Show that the behaviour of the network doesn't change.

**A:** 

## Sigmoid Neurons Simulating Perceptrons, Part II

**Q:** Suppose we have the same setup as the last problem - a network of perceptrons. Suppose also that the overall input to the network of perceptrons has been chosen. We won't need the actual input value, we just need the input to have been fixed. Suppose the weights and biases are such that w⋅x+b≠0 for the input x to any particular perceptron in the network. Now replace all the perceptrons in the network by sigmoid neurons, and multiply the weights and biases by a positive constant c>0. Show that in the limit as c→∞ the behaviour of this network of sigmoid neurons is exactly the same as the network of perceptrons. How can this fail when w⋅x+b=0 for one of the perceptrons?

**A:** 

## Bitwise Representation

**Q:** There is a way of determining the bitwise representation of a digit by adding an extra layer to the three-layer network above. The extra layer converts the output from the previous layer into a binary representation, as illustrated in the figure below. Find a set of weights and biases for the new output layer. Assume that the first 3 layers of neurons are such that the correct output in the third layer (i.e., the old output layer) has activation at least 0.99, and incorrect outputs have activation less than 0.01.

## Optimization through Gradient Descent

**Q:** Prove the assertion of the last paragraph. Hint: If you're not already familiar with the Cauchy-Schwarz inequality, you may find it helpful to familiarize yourself with it. *Let's suppose that we're trying to make a move Δv in position so as to decrease C as much as possible. This is equivalent to minimizing ΔC≈∇C⋅Δv. We'll constrain the size of the move so that ‖Δv‖=ϵ for some small fixed ϵ>0. In other words, we want a move that is a small step of a fixed size, and we're trying to find the movement direction which decreases C as much as possible. It can be proved that the choice of Δv which minimizes ∇C⋅Δv is Δv=−η∇C, where η=ϵ/‖∇C‖ is determined by the size constraint ‖Δv‖=ϵ. So gradient descent can be viewed as a way of taking small steps in the direction which does the most to immediately decrease C.*

**A:** 

## One-Dimensional Cost Function

**Q:** I explained gradient descent when C is a function of two variables, and when it's a function of more than two variables. What happens when C is a function of just one variable? Can you provide a geometric interpretation of what gradient descent is doing in the one-dimensional case?

**A:** 

1. ΔC ≈ ∇C⋅Δv
    ∇C = dC / dv1
    v = v1, thus Δv = Δv1, but Δv = −η∇C
    Δv1 = −η(dC / dv1)
2. ΔC ≈ (dC / dv1)⋅ −η(dC / dv1)
    ΔC ≈ (dC / dv1)⋅ −η(dC / dv1)
    ΔC ≈ −η (dC / dv1)⋅ (dC / dv1)
    ΔC ≈ −η (d^2 C/ dv1^2)

So the acceleration is constantly decreasing. 

## Online / Incremental Learning

**Q:** An extreme version of gradient descent is to use a mini-batch size of just 1. That is, given a training input, x, we update our weights and biases according to the rules wk→w′k=wk−η∂Cx/∂wk and bl→b′l=bl−η∂Cx/∂bl. Then we choose another training input, and update the weights and biases again. And so on, repeatedly. This procedure is known as online, on-line, or incremental learning. In online learning, a neural network learns from just one training input at a time (just as human beings do). Name one advantage and one disadvantage of online learning, compared to stochastic gradient descent with a mini-batch size of, say, 20.

**A:** 