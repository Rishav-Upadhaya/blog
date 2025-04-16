from django import forms
from django.contrib import admin
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5, 'cols': 60}),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'created_at')
    search_fields = ('title', 'body')
    list_filter = ('created_at',)

admin.site.register(Post, PostAdmin)



# from django.contrib import admin
# from .models import Post
# # Register your models here.

# # admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'body', 'created_at')
#     search_fields = ('title', 'body')
#     list_filter = ('created_at',)

# admin.site.register(Post, PostAdmin)


# from django.contrib import admin
# from .models import Post

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')

#     def save_model(self, request, obj, form, change):
#         # Custom logic: print a message to the console
#         print(f"Post '{obj}' is being saved by {request.user}")
#         super().save_model(request, obj, form, change)

# admin.site.register(Post, PostAdmin)
