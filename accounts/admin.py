from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserSignupForm
from .models import CustomUser
from freelancers.models import Freelancer  # Import from freelancers app
from clients.models import Client  # Import from clients app

class FreelancerInline(admin.StackedInline):
    model = Freelancer
    can_delete = False
    verbose_name_plural = 'Freelancer Profile'
    fk_name = 'user'

class ClientInline(admin.StackedInline):
    model = Client
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

    # Only show the relevant inline based on user role
    def get_inline_instances(self, request, obj=None):
        if not obj:  # When creating a new user
            return []
        inlines = []
        if obj.role == 'freelancer':
            inlines.append(FreelancerInline(self.model, self.admin_site))
        elif obj.role == 'client':
            inlines.append(ClientInline(self.model, self.admin_site))
        return inlines

admin.site.register(CustomUser, CustomUserAdmin)
