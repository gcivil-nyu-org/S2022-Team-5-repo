from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Property", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userofapp",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]
