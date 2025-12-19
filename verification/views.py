from rest_framework.generics import RetrieveAPIView
from .models import Certificate
from .serializers import CertificateSerializer

class CertificateVerifyView(RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    lookup_field = 'certificate_id'
