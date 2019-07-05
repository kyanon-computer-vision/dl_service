'''All preprocessing'''

from abc import ABC

class BaseDataPreprocessing(ABC):
    '''Abstract class, BaseDataPreprocessing'''
    def __init__(self, **kwargs):
        '''init'''
        super(BaseDataPreprocessing, self).__init__(**kwargs)