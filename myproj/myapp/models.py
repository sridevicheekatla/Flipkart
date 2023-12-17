# models.py
from django.db import models


class AllProducts(models.Model):
    uniq_id = models.CharField(max_length=1000)
    crawl_timestamp = models.CharField(max_length=1500)
    product_url = models.CharField(max_length=500)
    product_name = models.CharField(max_length=500)
    product_category_tree = models.CharField(max_length=1000)
    pid = models.CharField(max_length=2500)
    retail_price = models.CharField(max_length=1500)
    discounted_price = models.CharField(max_length=500)
    image = models.CharField(max_length=3000)
    is_fk_advantage_product = models.CharField(max_length=1500)
    description = models.TextField()
    product_rating = models.CharField(max_length=500)
    overall_rating = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)
    product_specifications = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "All Products"


class RelaxedFit(models.Model):
    fabric = models.CharField(max_length=255)
    ideal_for = models.CharField(max_length=255)


class RegularFit(models.Model):
    fabric = models.CharField(max_length=255)
    ideal_for = models.CharField(max_length=255)
