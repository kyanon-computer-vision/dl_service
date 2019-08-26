from apps.api.core.renderers import BaseJSONRenderer

class VisionDatasetJSONRenderer(BaseJSONRenderer):
    object_label = 'dataset'
    pagination_object_label = 'datasets'
    pagination_count_label = 'datasetsCount'
