from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User
import uuid

class Shapefile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-upload_date']
        verbose_name = 'Shapefile'
        verbose_name_plural = 'Shapefiles'

    def __str__(self):
        return self.name

class Feature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shapefile = models.ForeignKey(Shapefile, on_delete=models.CASCADE)
    feature_id = models.CharField(max_length=50, default=uuid.uuid4)
    geometry_type = models.CharField(max_length=50)
    coordinates = models.JSONField()
    properties = models.JSONField()
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return f"{self.shapefile.name} - {self.feature_id}"

class UserMapSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_latitude = models.FloatField(default=35.6892)
    default_longitude = models.FloatField(default=51.3890)
    default_zoom = models.IntegerField(default=10)
    last_viewed_layers = ArrayField(
        models.UUIDField(),
        blank=True,
        default=list
    )
    
    def __str__(self):
        return f"Map settings for {self.user.username}"