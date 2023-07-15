from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(["GET"])
def get_banner_view(request):
    return Response(BannerSerializer(Banner.objects.all().order_by('-id')[:3], many=True).data)


@api_view(["GET"])
def get_banner_video_view(request):
    return Response(BannerSerializer(Banner_video.objects.all().order_by('-id')[:3], many=True).data)


@api_view(["GET"])
def get_players_view(request):
    return Response(PlayersSerializer(Players.objects.all(), many=True).data)


@api_view(["GET"])
def get_shop_view(request):
    return Response(ShopSerializer(Players.objects.all(), many=True).data)


@api_view(['GET'])
def get_stadium_info_view(request):
    return Response(Stadium_infoSerializer(Stadium_info.objects.all(), many=True).data)


@api_view(['GET'])
def get_logo_view(request):
    return Response(LogoSerializer(Logo.objects.all(), many=True).data)


@api_view(['GET'])
def get_information_view(request):
    return Response(InformationSerializer(Information.objects.all(), many=True).data)


@api_view(["GET"])
def get_administrator_view(request):
    return Response(AdministratorSerializer(Administrator.objects.all(), many=True).data)


@api_view(['GET'])
def get_coaches_view(request):
    return Response(CoachesSerializers(Coaches.objects.all(), many=True).data)


@api_view(['GET'])
def get_history_view(request):
    return Response(HistorySerializers(History.objects.all(), many=True).data)


@api_view(["GET"])
def get_goal_view(request):
    return Response(GoalSerializers(Goal.objects.all(), many=True).data)


@api_view(["GET"])
def get_recommendations_view(request):
    return Response(RecommendationsSerializers(Recommendations.objects.all(), many=True).data)


@api_view(["GET"])
def get_Training_view(request):
    return Response(TrainingSerializers(Training.objects.all(), many=True).data)


@api_view(["GET"])
def tables(request):
    return Response(TableSerializers(Tims.objects.all().order_by("-o"), many=True).data)


