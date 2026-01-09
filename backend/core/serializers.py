from rest_framework import serializers
from .models import Company, Document, Signer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = '__all__'
        read_only_fields = ['document'] 

class DocumentSerializer(serializers.ModelSerializer):
    signers = SignerSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Document
        fields = [
            'id', 
            'name', 
            'status', 
            'open_id', 
            'token', 
            'external_id', 
            'company', 
            'created_at', 
            'last_updated_at',
            'summary', 
            'insights', 
            'signers'
        ]

    def create(self, validated_data):
        signers_data = validated_data.pop('signers', [])
        if signers_data is None:
            signers_data = []
            
        document = Document.objects.create(**validated_data)
        
        for signer_data in signers_data:
            
            Signer.objects.create(document=document, **signer_data)
            
        return document