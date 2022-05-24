from django.contrib.auth import get_user_model
from django import template
# ---- Safe for Cross site Scripting ----
from django.utils.html import escape
from django.utils.safestring import mark_safe


user_model = get_user_model()
register = template.Library()



@register.filter(name="author_details")
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = escape(f"{author.first_name} {author.last_name}")
    else:
        name = escape(f"{author.username}")

    if author.email:
        email = escape(author.email)
        prefix = f'<a href="mailto:{email}">'
        suffix = "</a>"
    else:
        prefix = ""
        suffix = ""

    return mark_safe(f"{prefix}{name}{suffix}")