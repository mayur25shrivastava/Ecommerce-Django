from django.contrib import admin

# from .views import contact

# Register your models here.

from . models import product,Contact,Orders,OrderUpdate

admin.site.register(product)


#to registrer contact modals 
admin.site.register(Contact)


#to registrer Orders modals 
admin.site.register(Orders)



#to registrer Orders modals 
admin.site.register(OrderUpdate)










