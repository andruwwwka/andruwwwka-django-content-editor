Приложение для редактирования контента с учетом прав пользователя на изменение содержания.

## Установка.

Для установки требуется скопировать приложение в свой проект и подключить его.
settings.py
```python
INSTALLED_APPS = (
    ...
    'editor',
)

MIDDLEWARE_CLASSES = (
    ...
    'content.middleware.content.Content',
)
```

## Использование.

base.html
```html
{% load editable_text %}
<link rel="stylesheet"  href="{{STATIC_URL}}css/my_css.css"/>
<script type="text/javascript" src="{{STATIC_URL}}ckeditor/ckeditor.js"></script>
<script type="text/javascript" src="{{STATIC_URL}}js/ckeditor_post.js"></script>
...
{% editable_text model=shop property='title' permission=user.is_admin %}
...
```
