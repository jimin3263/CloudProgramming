from django.contrib import admin

# Register your models here.
from markdownx.admin import MarkdownxModelAdmin

from algo_pages.models import Post, Tier, Tag

admin.site.register(Post, MarkdownxModelAdmin)


class TierAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tier, TierAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tag, TagAdmin)
