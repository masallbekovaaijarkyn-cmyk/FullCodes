from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File


class Certificate(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="ФИО"
    )

    certificate_id = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Номер сертификата"
    )

    course = models.CharField(
        max_length=100,
        verbose_name="Курс"
    )

    start_date = models.DateField(
        verbose_name="Дата начала курса"
    )

    end_date = models.DateField(
        verbose_name="Дата окончания курса"
    )

    issue_date = models.DateField(
        verbose_name="Дата выдачи"
    )

    is_valid = models.BooleanField(
        default=True,
        verbose_name="Сертификат действителен"
    )

    qr_code = models.ImageField(
        upload_to='certificates/qr/',
        blank=True,
        null=True,
        verbose_name="QR-код"
    )

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr = qrcode.make(
                f"https://fullcode.kg/api/certificates/verify/{self.certificate_id}/"
            )
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            self.qr_code.save(
                f"{self.certificate_id}.png",
                File(buffer),
                save=False
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} — {self.certificate_id}"

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
