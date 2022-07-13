from django.http import Http404
from rest_framework.permissions import BasePermission

from music.models import Selection


class SelectionEditPermission(BasePermission):
    message = "You don't have permissions for that :("

    def has_permission(self, request, view):
        try:
            select_object = Selection.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            raise Http404

        if select_object.owner_id == request.user.id:
            return True
        return False
