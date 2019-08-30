from apps.api.core.renderers import BaseJSONRenderer

class VisionDatasetJSONRenderer(BaseJSONRenderer):
    object_label = 'dataset'
    pagination_object_label = 'datasets'
    pagination_count_label = 'datasetsCount'

class VisionDLModelJSONRenderer(BaseJSONRenderer):
    object_label = 'model'
    pagination_object_label = 'models'
    pagination_count_label = 'modelsCount'
