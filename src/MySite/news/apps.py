from django.apps import AppConfig


class NewsConfig(AppConfig):
    # Тип поля, которое будет автоматически создаваться в качестве
    # первичного ключа (Primary Key) для моделей.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = 'Новости'
