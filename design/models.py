from django.db import models


class Design(models.Model):
    design_img=models.ImageField(upload_to='designs/')
    d_height=models.IntegerField(null=True)
    d_width=models.IntegerField(null=True)
    used_colors = models.JSONField(null=True)
    content_list=models.JSONField(null=True)
    weft_seq=models.TextField(null=True)
    warp_seq=models.TextField(null=True)
    weft_rolls=models.JSONField(null=True)
    warp_rolls=models.JSONField(null=True)

class Combined_Weave(models.Model):
    design=models.ForeignKey(Design,on_delete=models.CASCADE)
    color=models.IntegerField()
    image_array=models.JSONField(default=[[1]])
class Simple_Weave(models.Model):
    weave_image=models.ImageField(upload_to='weaves/')
    dm=models.JSONField()
    combined_w=models.ForeignKey(Combined_Weave,on_delete=models.CASCADE)
    weave_list=models.JSONField(default=[[1]])
class Images_Library(models.Model):
    image_file=models.ImageField(upload_to='weaves/')
    cat=models.CharField(max_length=100)




