import uuid
from django.core.exceptions import ValidationError

def image_path(instance, filename):
    extension = filename.split('.')[1]
    if len(filename.split('.')) != 2:
        raise ValidationError("image seems currupted...")
    if extension not in ['jpg', 'jpeg', 'png', 'PNG']:
        raise ValidationError("we currently accept jpg/jpeg formats only.")
    unique_name = uuid.uuid4().hex
    return 'uploads/' + unique_name + '.' + extension