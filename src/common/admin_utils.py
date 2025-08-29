from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from markdown import markdown

class AdminImageMixin:
    """
    Миксин для добавления методов отображения изображений в админ-панель
    """
    image_field = 'image'
    default_image = 'img/elements/no_photo.webp'
    
    def image_tag(self, obj):
        """
        Генерирует HTML-тег изображения для отображения в админ-панели.
        """
        image = getattr(obj, self.image_field, None)
        if image and hasattr(image, 'url'):
            return format_html('<img id="image_tag" src="{}" />', image.url)
        else:
            default_image_url = static(self.default_image)
            return format_html('<img id="image_tag" src="{}" />', default_image_url)
    image_tag.short_description = 'Изображение'
    
    def image_thumbnail(self, obj):
        """
        Генерирует HTML-тег миниатюры изображения для отображения в админ-панели.
        """
        image = getattr(obj, self.image_field, None)
        if image and hasattr(image, 'url'):
            return format_html('<img id="image_thumbnail" src="{}" />', image.url)
        else:
            default_image_url = static(self.default_image)
            return format_html('<img id="image_thumbnail" src="{}" />', default_image_url)
    image_thumbnail.short_description = 'Изображение'

    def star_rating_display(self, obj):
        """Отображение рейтинга в виде Bootstrap звезд"""
        if obj.star_rating is None:
            return format_html(
                '<span class="text-muted">'
                '<i class="bi bi-star me-1"></i>Не оценен'
                '</span>'
            )
        
        stars = ''.join([
            '<i class="bi bi-star-fill text-warning"></i>' 
            if i < obj.star_rating else 
            '<i class="bi bi-star text-muted"></i>'
            for i in range(5)
        ])
        
        return mark_safe(
            f'<div class="text-warning">{stars}</div>'
        )
    star_rating_display.short_description = 'Рейтинг'

class AdminDisplayMixin:
    """
    Миксин для отображения иконок и контента в админке.
    Настройки по умолчанию можно переопределить в дочерних классах.
    """
    # Настройки по умолчанию
    icon_field = 'icon'
    content_field = 'content'
    icon_html_class = 'fs-3'
    content_preview_length = None  # Если нужно ограничить длину превью
    
    def get_icon_html(self, icon):
        """Генерация HTML для иконки (можно переопределить)"""
        return f'<span class="{self.icon_html_class}">{icon}</span>'
    
    def get_content_html(self, content):
        """Генерация HTML для контента (можно переопределить)"""
        if self.content_preview_length and len(content) > self.content_preview_length:
            content = content[:self.content_preview_length] + '...'
        return markdown(content)
    
    def display_icon(self, obj):
        """Метод для отображения в list_display"""
        icon = getattr(obj, self.icon_field, None)
        if icon:
            return mark_safe(self.get_icon_html(icon))
        return "-"
    display_icon.short_description = 'Иконка'
    display_icon.admin_order_field = 'icon'  # Добавляем возможность сортировки
    
    def display_content_preview(self, obj):
        """Метод для отображения в list_display"""
        content = getattr(obj, self.content_field, None)
        if content:
            return mark_safe(f'<div class="content-preview">{self.get_content_html(content)}</div>')
        return "-"
    display_content_preview.short_description = 'Содержание'
    
    def get_list_display(self, request):
        """Автоматическое добавление методов в list_display"""
        list_display = super().get_list_display(request)
        if not list_display:
            return list_display
        
        # Автоматически добавляем методы, если они не указаны явно
        methods_to_add = []
        if hasattr(self, 'display_icon') and 'display_icon' not in list_display:
            methods_to_add.append('display_icon')
        if hasattr(self, 'display_content_preview') and 'display_content_preview' not in list_display:
            methods_to_add.append('display_content_preview')
        
        if methods_to_add:
            return tuple(methods_to_add) + tuple(list_display)
        return list_display
    
