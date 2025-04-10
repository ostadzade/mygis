from django.db import models
from djongo import models as djongo_models
from users.models import User
import uuid

class Shapefile(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    user = djongo_models.ForeignKey(User, on_delete=djongo_models.CASCADE)
    name = djongo_models.CharField(max_length=100)
    description = djongo_models.TextField(blank=True)
    upload_date = djongo_models.DateTimeField(auto_now_add=True)
    file_path = djongo_models.CharField(max_length=255)
    is_active = djongo_models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-upload_date']
        verbose_name = 'Shapefile'
        verbose_name_plural = 'Shapefiles'

    def __str__(self):
        return self.name

class Feature(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    shapefile = djongo_models.ForeignKey(Shapefile, on_delete=djongo_models.CASCADE)
    feature_id = djongo_models.CharField(max_length=50, default=uuid.uuid4)
    geometry_type = djongo_models.CharField(max_length=50)
    coordinates = djongo_models.JSONField()
    properties = djongo_models.JSONField()
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return f"{self.shapefile.name} - {self.feature_id}"

class UserMapSettings(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    user = djongo_models.OneToOneField(User, on_delete=djongo_models.CASCADE)
    default_latitude = djongo_models.FloatField(default=35.6892)
    default_longitude = djongo_models.FloatField(default=51.3890)
    default_zoom = djongo_models.IntegerField(default=10)
    last_viewed_layers = djongo_models.ArrayReferenceField(to=Shapefile, blank=True)
    
    def __str__(self):
        return f"Map settings for {self.user.username}"