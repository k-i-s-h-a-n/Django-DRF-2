from rest_framework import serializers
from drfApi.models import Person, Color



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']
               



class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    country = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = "__all__"
        # depth = 1    #It will show all the fields which is map with foreign key no need to write serializer

    def get_country(self,obj):
        return "INDIA"

    def validate(self, data):
        specialCharacters = "!@#$%^&*()_+=./><,][}{\|`~]"
        if any(char in specialCharacters for char in data['name']):
            raise serializers.ValidationError('name cannot contain special characters')

        if data['age'] < 18:
            raise serializers.ValidationError("Age must be greater than or equal to 18")
        return data

    # Can also be written
    # def validate_age(self,age):
    #     print(age)
    #     if age < 18:
    #         raise serializers.ValidationError("NN Age must be greater than or equal to 18")
    #     return age



