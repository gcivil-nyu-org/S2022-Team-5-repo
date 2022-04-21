from django.core.exceptions import ValidationError


def file_size(value):
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(
            "Image size should not exceed 3 MiB. Please upload a smaller photo."
        )
    else:
        return value
