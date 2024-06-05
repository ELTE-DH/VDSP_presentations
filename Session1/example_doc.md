# Deep Neural Networks

## Backpropagation

Backpropagation is a method used to calculate the gradient of a loss function with respect to the weights of a neural network. It is widely used in training deep neural networks. By calculating the gradient we can update the weights of the network in the opposite direction of the gradient to minimize the loss function, thus we get more accurate predictions.

$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial z} \frac{\partial z}{\partial w} $$

Where:
- $L$ is the loss function
- $w$ is the weight
- $y$ is the output of the neuron
- $z$ is the input of the neuron

The weight update formula in backpropagation is given by:

$$ \Delta w = -\eta \frac{\partial L}{\partial w} $$

Where:
- $\Delta w$ is the change in weight
- $\eta$ is the learning rate

This formula calculates the change in weight by multiplying the negative learning rate ($-\eta$) with the gradient of the loss function with respect to the weight ($\frac{\partial L}{\partial w}$). The negative sign is used to update the weight in the opposite direction of the gradient, aiming to minimize the loss function.

By updating the weights in the direction that reduces the loss, the neural network can improve its predictions over time.