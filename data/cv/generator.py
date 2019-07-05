'''All generators for computer vision task are implemented here'''


from abc import ABC

class BaseDataGenerator(ABC):
    '''Abstract class, BaseDataGenertor'''

    def __init__(self, **kwargs):
        '''init'''
        super(BaseDataGenerator, self).__init__(**kwargs)