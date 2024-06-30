from django.db import models

# Create your models here.


class ModelName(models.Model):
    '''Model definition for ModelName.'''
    name = models.CharField(max_length = 150 ,blank=True, null=True,default='')
    namess = models.CharField(max_length = 150 ,blank=True, null=True,default='')
    
    class Meta:
        '''Meta definition for ModelName.'''

        verbose_name = 'مودل دجانحو '
        verbose_name_plural = 'مودل دجانحو s'

    def __str__(self):
        return self.name