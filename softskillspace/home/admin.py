from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from home.models import (CustomUser, MailingList, MailingListCategory,
                         ProfileSetting, UserStatistic)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            _("Personal info"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "about",
                    "email",
                    "country",
                    "mobile_no",
                    "gender",
                    "date_of_birth",
                    "profile_pic",
                    "verified",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",), "fields": (
                "password1", "password2"), },), )
    list_display = [
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_superuser",
    ]
    ordering = ("first_name", "last_name")
    list_display_links = ["first_name", "email"]
    autocomplete_fields = ["country"]
    list_filter = ["verified", "created_at", "gender"]


@admin.register(MailingListCategory)
class MailingListCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    ordering = ["name"]
    search_fields = ["name"]


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ["email", "created_at"]
    ordering = ["-created_at"]
    list_filter = ["categories"]
    filter_horizontal = ["categories"]


@admin.register(UserStatistic)
class UserStatisticAdmin(admin.ModelAdmin):
    list_display = ["user", "skill_point", "wallet_amount"]
    ordering = ["user"]
    autocomplete_fields = ["user"]


@admin.register(ProfileSetting)
class ProfileSettingsAdmin(admin.ModelAdmin):
    ordering = ["user"]
