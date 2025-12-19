from rest_framework import viewsets
from .models import Course, Advantage, Lead
from .serializers import *
from .telegram import send_telegram_message

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AdvantageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def perform_create(self, serializer):
        lead = serializer.save()
        send_telegram_message(
            f" 🎓 Новая заявка от студента\n"
            f"👤 Имя: {lead.full_name}\n"
            f"🎂 Возраст: {lead.age}\n"
            f"📘 Язык: {lead.language}\n"
            f"📞 Телефон: {lead.phone}"
        )
