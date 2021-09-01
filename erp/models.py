from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    unit = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class MaterialStock(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return "{}: {} {}".format(self.material.name, self.quantity, self.material.unit)


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    unit = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class ProductStock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return "{}: {} {}".format(self.product.name, self.quantity, self.product.unit)


class ProductRequirement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)

    class Meta:
        unique_together = [['product', 'material']]
