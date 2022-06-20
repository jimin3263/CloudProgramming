from django.contrib import admin

# Register your models here.
from markdownx.admin import MarkdownxModelAdmin

from algo_pages.models import Post, Tag
from algo_today.models import Problem, TodayProblem

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Problem)
admin.site.register(TodayProblem)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tag, TagAdmin)
