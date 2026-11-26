from django.db import models

# Create your models here.
class AssetRegistration(models.Model):
    assetId=models.CharField(max_length=15,primary_key=True,unique=True, blank=True)
    asset_name=models.CharField(max_length=50)
    category=models.CharField(max_length=30)
    purchase_date=models.DateField()
    purchase_cost=models.FloatField()
    supplier_name=models.CharField(max_length=80)
    asset_location=models.CharField(max_length=50)
    asset_condition=models.CharField(max_length=15)
    asset_status=models.CharField(max_length=15)
    asset_description=models.TextField(max_length=250)
# Auto id generation
    def save(self, *args, **kwargs):
        if not self.assetId:
            last_asset = AssetRegistration.objects.order_by('-id').first()

            if last_asset:
                last_number = int(last_asset.assetId.replace("AST", ""))
                new_number = last_number + 1
            else:
                new_number = 1

            self.assetId = f"AST{new_number:03d}"

        super().save(*args, **kwargs)
