from django.contrib import admin

from tasks.models import CustomUser, Habit, Task


admin.site.register(CustomUser)
admin.site.register(Habit)
admin.site.register(Task)
