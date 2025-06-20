from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):
    GENDER_CHOICES = (
        ('male', 'Чоловічий'),
        ('female', 'Жіночий'),
        ('unisex', 'Унісекс'),
    )

    title = models.CharField(max_length=56, blank=True)
    description = models.TextField(max_length=512, blank=True)
    price = models.IntegerField()
    sizes = models.ManyToManyField(Size, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='items')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')

    def __str__(self):
        return self.title


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"Image for {self.item.title}"


class Order(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order.full_name} - {self.item.title} x{self.quantity}"

