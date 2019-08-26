from rest_framework.permissions import BasePermission

class UserIsOwnerDataset(BasePermission):
    def has_object_permission(self, request, view, dataset):
        return request.user.id == dataset.user.id
