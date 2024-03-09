from django.contrib import admin
from .models import *

# Models registration for backend.
admin.site.register(Contact)
admin.site.register(Blogs)


class TrainingAdmin(admin.ModelAdmin):
  list_display = ('fullname',
  'usn',
  'email',
  'highest_qualification',
  'offers_status',
  'start_date',
  'end_date',
  'proj_report',
  'timeStamp',)
  search_fields=('fullname','usn','email')
  list_filter=['highest_qualification', 'proj_report', 'offers_status']
  
admin.site.register(Training,TrainingAdmin)
  
