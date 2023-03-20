from io import BytesIO
from django.core.files.base import File

from allauth.account.models import EmailAddress
from PIL import Image

from home.models import CustomUser


def create_user(cls) -> CustomUser:
    cls.user = CustomUser.objects.create_user(
        email="jackdoe@test.com", password="testpassword", is_active=True,
    )

    EmailAddress.objects.create(
        user=cls.user, email=cls.user.email, verified=True, primary=True
    )


def generate_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)
