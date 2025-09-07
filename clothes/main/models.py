from django.db import models
from django.urls import reverse 


class Category(models.Model):
    name = models.CharField(max_length=255,
                            unique=True)
    slug = models.SlugField(max_length=255,
                            unique=True)
    

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=255,
                            unique=True)
    slug = models.SlugField(max_length=255,
                            unique=True)
    category = models.ForeignKey(Category,
                                 related_name='subcategories',
                                 on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


    def get_absolute_url(self):
        return reverse("main:subcategory", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(SubCategory,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['created'])
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse("main:product_info", args=[self.id])
    

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    SIZE_CHOICES = [
        ("XS", "Extra Small"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size} ({self.stock} шт.)"
    

class Order(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    flat = models.IntegerField()
    email = models.EmailField(max_length=255)

    paid = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product_size = models.ForeignKey(ProductSize, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)

