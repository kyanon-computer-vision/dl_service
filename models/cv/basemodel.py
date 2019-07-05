
from abc import ABC
from utils.thread_utils import TrainingThread

class BaseModel(ABC):
    '''Base model, most of functions use Keras API'''
    def __init__(self, **kwargs):
        '''init'''
        super(BaseModel,self).__init__(**kwargs)

    def compile(self, loss, optimizer, metrics):
        '''compile model'''

        pass

    def fit_generator(self, generator, batch_size, epochs, validation_generator=None, callbacks=None, verbose=1, **kwargs):
        '''
        train model with a generator
        ----------------------------------
        generator: train generator for training model, Keras ImageDataGenerator is also approved
        batch_size: batch of size
        epochs
        validation_generator: wheather use validation or not, Keras ImageDataGenerator is also approved
        callbacks: list, callable functions
        -----------------------------------
        Return:
        history
        '''
        
        pass
    
    def evaluate_generator(self, generator, batch_size, verbose=0, **kwargs):
        '''
        evaluate model
        return score which has loss and accuracy
        '''
        pass

    def predict_generator(self, generator, batch_size=1, **kwargs):

        pass

    def single_predict(self, item, **kwargs):

        pass
        

class BaseModelBuilder(ABC):
    def __init__(self, **kwargs):
        super(BaseModelBuilder, **kwargs).__init__(**kwargs)

    def build(self, **kwargs):
        ''''''
        pass

class SkippedVGGBuilder(BaseModel):
    def __init__(self, **kwargs):
        super(SkippedVGGBuilder, self).__init__(**kwargs)

    def build(self, nb_blocks, input_shape, num_classes, nb_layers, nb_neurons, include_top=True, verbose=1, **kwargs):
        '''
        Build Skipped VGG model
        ----------------------------------
        nb_blocks: number of block in model
        input_shape: tuple, size of 3, not include batch size
        num_classes: number of model output
        nb_layers:  list, nb of conv layer in each block; 
                    if scalar, then all blocks are used the same number of conv layer
        nb_neurons: list, nb of conv neuron in each block
        include_top: wheather the model include classifier or not
        -----------------------------------
        Return: Keras model
        '''
        pass

    def _define_block(self, input_layer, nb_layers, nb_neurons, kernel_size=(3,3), batch_normalization=True, activation='relu', **kwargs):
        pass

    def _define_skipped_connection(self, src_layer, dst_layer):
        pass
    


    