from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import (MPTTModel,TreeForeignKey,TreeManyToManyField)

# Create your models here.
class Category(MPTTModel):
    """
    Product Category table implemented with MPTT for many to many to self 
    """
    name = models.CharField(max_length=100,null=False,unique=False,blank=False,verbose_name=_("category_name"),help_text=_("format: required,max length = 100"))
    slug = models.SlugField(max_length=150,null=False,blank=False,unique=False,verbose_name = _("category safe URL"))
    is_active = models.BooleanField(default =True)
    parent = TreeForeignKey("self",on_delete=models.PROTECT,related_name = "children", null = True,blank = True, verbose_name = _("parent of category"))

    class MPTTMeta:
        order_insertion_by = ["name"]


    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    web_id = models.CharField(max_length=50,unique = True,null=False,blank=False,verbose_name=_("product website ID"))
    slug = models.SlugField(max_length=255,unique=False,null=False,blank=False,verbose_name=_("Product safe URL"))
    name = models.CharField(max_length=255,unique=False,null=False,blank=False,verbose_name=_("product name"),help_text=_("format: required, max-255"))
    description = models.TextField(unique=False,null=False,blank=False,verbose_name=_("product description"),help_text=_("format: required"))
    category = TreeManyToManyField(Category)
    # can make it false by default
    is_active = models.BooleanField(unique=False,null=False,blank=False,default=True,verbose_name=_("product visibility"),help_text=_("format: true=product visible"))
    created_at = models.DateTimeField(auto_now_add=True,editable=False,verbose_name=_("date product created"),help_text=_("format: Y-m-d H:M:S"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("date product last updated"),help_text=_("format: Y-m-d H:M:S"))

    @property
    def product_category(self):
        catg = self.category.all()
        return(self.category.all())
    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    """
    Product attribute table attributes like Color, Shoe Size, Inches
    """
    name = models.CharField(max_length=255,unique=True,null=False,blank=False,verbose_name=_("product attribute name"),help_text=_("format: required, unique, max-255"))
    description = models.TextField(unique=False,null=False,blank=False,verbose_name=_("product attribute description"),help_text=_("format: required"))

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    Product type table eg Shoes,clothes,phones
    """
    name = models.CharField(max_length=255,unique=True,null=False,blank=False,verbose_name=_("type of product"),help_text=_("format: required, unique, max-255"))
    product_type_attribute = models.ManyToManyField(ProductAttribute,related_name="product_type_attributes",through="ProductTypeAttribute")

    def __str__(self):
        return self.name

    


class Brand(models.Model):
    """
    Product brand table
    """
    name = models.CharField(max_length=255,unique=True,null=False,blank=False,verbose_name=_("brand name"),help_text=_("format: required, unique, max-255"))

    def __str__(self):
        return str(self.name)


class ProductAttributeValue(models.Model):
    """
    Product attribute value table like "red", "7", "12 inches"
    """
    product_attribute = models.ForeignKey(ProductAttribute,related_name="product_attribute",on_delete=models.PROTECT)
    attribute_value = models.CharField(max_length=255,unique=False,null=False,blank=False,verbose_name=_("attribute value"),help_text=_("format: required, max-255"))

    def __str__(self):
        return (
            f"{self.product_attribute.name} : {self.attribute_value}"
        )


class ProductMeta(models.Model):
    """
    Product Meta table for every single product in store
    """
    sku = models.CharField(max_length=20,unique=True,null=False,blank=False,verbose_name=_("stock keeping unit"),help_text=_("format: required, unique, max-20"))
    upc = models.CharField(max_length=12,unique=True,null=False,blank=False,verbose_name=_("universal product code"),help_text=_("format: required, unique, max-12"))
    product_type = models.ForeignKey(ProductType,related_name="product_type",on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.PROTECT)
    attribute_values = models.ManyToManyField(ProductAttributeValue,related_name="product_attribute_values",through="ProductAttributeValues")
    is_active = models.BooleanField(default=True,verbose_name=_("product visibility"),help_text=_("format: true=product visible"))
    is_default = models.BooleanField(default=False,verbose_name=_("default selection"),help_text=_("format: true=sub product visible"))
    retail_price = models.DecimalField(max_digits=5,decimal_places=2,unique=False,null=True,blank=True,verbose_name=_("recommended retail price"),help_text=_("format: maximum price 999.99"),error_messages={"name": {"max_length": _("the price must be between 0 and 999.99."),},})
    store_price = models.DecimalField(max_digits=5,decimal_places=2,unique=False,null=False,blank=False,verbose_name=_("regular store price"),help_text=_("format: maximum price 999.99"),error_messages={    "name": {        "max_length": _(            "the price must be between 0 and 999.99."        ),    },})
    sale_price = models.DecimalField(max_digits=5,decimal_places=2,unique=False,null=True,blank=True,verbose_name=_("sale price"),help_text=_("format: maximum price 999.99"),error_messages={    "name": {        "max_length": _(            "the price must be between 0 and 999.99."        ),    },})
    weight = models.FloatField(unique=False,null=True,blank=True,verbose_name=_("product weight"))
    created_at = models.DateTimeField(auto_now_add=True,editable=False,verbose_name=_("date sub-product created"),help_text=_("format: Y-m-d H:M:S"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("date sub-product updated"),help_text=_("format: Y-m-d H:M:S"))

    @property
    def producttype(self):
        return str(self.producttype.name)

    @property
    def Brand(self):
        return str(self.brand.name)

    @property
    def Attributes(self):
        return(self.attribute_values.all())

    class Meta:
        verbose_name = str("Product Meta")
        verbose_name_plural = ("Product Meta")
        
    def __str__(self):
        return self.product.name


class Media(models.Model):
    """
    The product image table.
    """

    product_meta = models.ForeignKey(ProductMeta,on_delete=models.PROTECT,related_name="media_product_meta")
    image = models.ImageField(unique=False,null=False,blank=False,verbose_name=_("product image"),upload_to="images/products",default="images/products/default.png",help_text=_("format: required, default-default.png"))
    alt_text = models.CharField(max_length=255,unique=False,null=False,blank=False,verbose_name=_("alternative text"),help_text=_("format: required, max-255"))
    is_feature = models.BooleanField(default=False,verbose_name=_("product default image"),help_text=_("format: default=false, true=default image"))
    created_at = models.DateTimeField(auto_now_add=True,editable=False,verbose_name=_("product visibility"),help_text=_("format: Y-m-d H:M:S"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_("date sub-product created"),help_text=_("format: Y-m-d H:M:S"))

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")



class Stock(models.Model):
    product_meta = models.OneToOneField(ProductMeta,related_name="product_meta",on_delete=models.PROTECT)
    last_checked = models.DateTimeField(unique=False,null=True,blank=True,verbose_name=_("inventory stock check date"),help_text=_("format: Y-m-d H:M:S, null-true, blank-true"))
    units = models.IntegerField(default=0,unique=False,null=False,blank=False,verbose_name=_("units/qty of stock"),help_text=_("format: required, default-0"))
    units_sold = models.IntegerField(default=0,unique=False,null=False,blank=False,verbose_name=_("units sold to date"),help_text=_("format: required, default-0"))


class ProductAttributeValues(models.Model):
    """
    Product attribute values link table
    """

    attributevalues = models.ForeignKey("ProductAttributeValue",related_name="attributevaluess",on_delete=models.PROTECT)
    productmeta = models.ForeignKey(ProductMeta,related_name="productattributevaluess",on_delete=models.PROTECT)

    class Meta:
        unique_together = (("attributevalues", "productmeta"),)

    @property
    def AttributeValue(self):
        return(self.attributevalues.attribute_value)


class ProductTypeAttribute(models.Model):
    """
    Product type attributes link table
    """

    product_attribute = models.ForeignKey(ProductAttribute,related_name="productattribute",on_delete=models.PROTECT)
    product_type = models.ForeignKey(ProductType,related_name="producttype",on_delete=models.PROTECT)

    class Meta:
        unique_together = (("product_attribute", "product_type"),)

