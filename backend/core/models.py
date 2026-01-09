from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    
    open_id = models.IntegerField(default=0)
    
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50, default='pending')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    
    
    summary = models.TextField(blank=True, null=True)
    insights = models.TextField(blank=True, null=True)

class Signer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    token = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50, default='pending')
    document = models.ForeignKey(Document, related_name='signers', on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255, blank=True, null=True)