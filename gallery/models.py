from django.db import models
from django.utils import timezone
# 2. Необхідно додати в аплікації gallery модель для категорії зображень.
#  - назва моделі: Category
#  - атрибути: name (CharField)
# 3. Необхідно додати в аплікації gallery модель для зображення.
#  - назва моделі: Image
#  - атрибути: title (CharField), 
# image (ImageField), 
# categories (ManyToManyField),
#  created_date (DateField), 
# age_limit (PositiveIntegerField)
# 4. Написати unit-тести, які протестують роботу із створеними моделями.

class Category(models.Model):
    name = models.CharField(max_length=200)

class Image(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    created_date = models.DateField()
    age_limit = models.PositiveIntegerField()

    # def __str__(self):
    #     return title