from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class AcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academy
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner_video
        fields = "__all__"


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class Stadium_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium_info
        fields = "__all__"


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = "__all__"


class CoachesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coaches
        fields = "__all__"


class ClubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class GoalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"


class RecommendationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = "__all__"


class TrainingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tims
        fields = "__all__"
