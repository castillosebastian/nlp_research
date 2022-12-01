import numpy as np
 
 
def sigmoid(z): 
    '''
    Input:
        z: is the input (can be a scalar or an array)
    Output:
        h: the sigmoid of z
    '''
    
    ### START CODE HERE ###
    # calculate the sigmoid of z
    h = 1/(1 + np.exp(-z))
    ### END CODE HERE ###
    
    return h

# verify that when the model predicts close to 1, but the actual label is 0, the loss is a large positive value
-1 * (1 - 0) * np.log(1 - 0.9999) # loss is about 9.2


# Implementacion gradient descent logistic regresion
# Función de Perdida para Regresion Logística: Entropía cruzada: https://www.youtube.com/watch?v=sedrzwgC-1E
