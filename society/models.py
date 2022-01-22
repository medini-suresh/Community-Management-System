from django.db import models

# Create your models here.

def society_image_upload_path(instance, filename):
    return ''.join(f'{instance.name}/{filename}')
    
class Society(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    image = models.ImageField(upload_to=society_image_upload_path, null=True, blank=True)
    owner_company = models.CharField(max_length=20, null=True , blank=True)
    secretary = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Societies'
    
    def __str__(self):
        return self.name

BHK_CHOICES = (
    ('1', 'One BHK'),
    ('1.5', '1.5 BHK'),
    ('2', 'Two BHK'),
    ('3', 'Three BHK'),
    ('4', 'Four BHK'),
)
class Flat(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    bhk = models.CharField(max_length=5, choices=BHK_CHOICES)
    number = models.PositiveIntegerField()
    floor_no = models.PositiveIntegerField()
    block = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): 
        return f'{self.society.name} - {self.block}-{self.number}'