from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from decimal import Decimal


# Create your models here.
from listing_api.models import BaseModel

class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = ('Категория')
        verbose_name_plural = ('Категории')

    def __str__(self):
        return self.name

class Tags(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = ('Tag')
        verbose_name_plural = ('Tags')

    def __str__(self):
        return self.name

class Amenities(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = ('Удобство')
        verbose_name_plural = ('Удобства')

    def __str__(self):
        return self.name

class Qualifications(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("Квалификация")
        verbose_name_plural = ("Квалификации")

class TechnicalSpecifications(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ('Техническая характеристика')
        verbose_name_plural = ('Технические характеристики')

    def __str__(self):
        return self.name

class VacancyType(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ('Тип вакансии')

    def __str__(self):
        return self.name

class SalonFeatures(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ('Особенности салона')

    def __str__(self):
        return self.name

class HealthAndSafetyMeasures(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ('Меры по охране здоровья и безопасности:')

    def __str__(self):
        return self.name

class Cinema_Features(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        verbose_name = ("Особенности кинотеатра")

    def __str__(self):
        return self.name


class Listing(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, default='listing_name')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    amenities = models.ForeignKey(Amenities, on_delete=models.SET_NULL, null=True, related_name='amenities')
    technical_specifications = models.ForeignKey(TechnicalSpecifications, on_delete=models.SET_NULL, null=True, related_name='technical_specifications')
    qualification = models.ForeignKey(Qualifications, on_delete=models.SET_NULL, null=True, related_name="qualification")
    vacancy_type = models.ForeignKey(VacancyType, on_delete=models.SET_NULL, null=True, related_name="vacancy_type")
    salon_features = models.ForeignKey(SalonFeatures, on_delete=models.SET_NULL, null=True, related_name= 'salon_features')
    health_and_safety_measures = models.ForeignKey(HealthAndSafetyMeasures, on_delete=models.SET_NULL, null=True, related_name="health_and_safety_measures")
    cinema_features = models.ForeignKey(Cinema_Features, on_delete=models.SET_NULL, null=True, related_name="cinema_features")
    slug = models.SlugField()
    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True, related_name='tags')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    social_networks = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=500, blank=True, null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2)


    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    class Meta:
        verbose_name = ('Объявление')
        verbose_name_plural = ('Объявления')

    def __str__(self):
        return self.name


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    listing = models.ForeignKey(Listing, verbose_name="фильм", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.listing}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"