import datetime

from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    born_years = serializers.SerializerMethodField() # read only

    class Meta:
        model = Student
        fields = "__all__"
        # exclude = ["number"]
        # fields = ("id", "first_name", "last_name", "age", "number")
        read_only_fields = ["id"]

    def get_born_years(self, student):
        current_time = datetime.datetime.now()
        return current_time.year - student.age
        

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance
    
# validated_data = {
#     "first_name" : "Ali",
#     "last_name":"Veli",
#     "number": 1,
#     "age": 34,
# }