from django.contrib import admin
from .models import Article, Scope, Relationship
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        error_status = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                error_status += 1
        if error_status == 0:
            raise ValidationError('Укажите основной раздел!')
        elif error_status > 1:
            raise ValidationError('Основной раздел должен быть один!')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 0
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']