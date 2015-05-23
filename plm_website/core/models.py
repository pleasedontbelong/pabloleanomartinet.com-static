from django.db import models

from .mixins import OnChangeMixin


class ModelBase(OnChangeMixin, models.Model):

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def reload(self):
        """Reloads the instance from the database."""
        from_db = self.__class__.objects.get(id=self.id)
        for field in self.__class__._meta.fields:
            setattr(self, field.name, getattr(from_db, field.name))
        return self
