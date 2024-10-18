from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import MagicalCreature
from .serializers import MagicalCreatureSerializer

from .permissions import IsOwnerOrReadOnly

class MagicalCreaturePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.added_by

class MagicalCreatureViewSet(viewsets.ModelViewSet):
    queryset = MagicalCreature.objects.all()
    serializer_class = MagicalCreatureSerializer
    permission_classes = [MagicalCreaturePermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the creator/owner
        serializer.save(owner=self.request.user)
