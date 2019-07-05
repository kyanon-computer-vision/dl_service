'''All preprocessing'''

from abc import ABC

class BaseDataPreprocessing(ABC):
    '''Abstract class, BaseDataPreprocessing'''
    def __init__(self, **kwargs):
        '''init'''
        super(BaseDataPreprocessing, self).__init__(**kwargs)

    def load_image(self, **kwargs):
        pass

    def resize(self, **kwargs):
        pass

    def reshape(self, **kwargs):
        pass

    def normalize(self, **kwargs):
        pass

    def preprocess(self, **kwargs):
        pass