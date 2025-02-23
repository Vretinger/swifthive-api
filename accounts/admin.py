from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserSignupForm
from .models import CustomUser, FreelancerProfile, ClientProfile, Skill, Company, category

class FreelancerInline(admin.StackedInline):
    model = FreelancerProfile
    can_delete = False
    verbose_name_plural = 'Freelancer Profile'
    fk_name = 'user'

class ClientInline(admin.StackedInline):
    model = ClientProfile
    can_delete = False
    verbose_name_plural = 'Client Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserSignupForm
    model = CustomUser
    list_display = ('email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_staff', 'is_active')},
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FreelancerProfile)
admin.site.register(ClientProfile)
admin.site.register(category)
admin.site.register(Skill)
admin.site.register(Company)
