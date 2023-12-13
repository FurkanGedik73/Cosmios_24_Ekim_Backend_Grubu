from rest_framework import serializers
from .models import Student, Path

class StudentSerializer(serializers.ModelSerializer):
    
    born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField()  #read_only #şeklinde yazarsak otomatik olarak pathin idsine karşılık gelen ismi vermiş olur. 
    path_id =serializers.IntegerField()
    class Meta:
        model = Student
        # fields = "_all_"
        fields = ["id","first_name", "last_name","number", "age", "born_year", "path", "path_id"]
        # exclude = ["number"]
        
    
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    
    
class PathSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Path
        fields = "__all__"