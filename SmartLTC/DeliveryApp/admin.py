from django.contrib import admin

from .models import store,patient,home,driver,role_mst,user_driver_map,\
    user_pharmacy_map,user_home_map,user_patient_map,order_mst,order_packet_map\
    ,packet_mst,job_mst,job_packet_map,job_list,job_driver_map,vehical_type\
    ,driver_vehical,user_mst

admin.site.register(store)
admin.site.register(patient)
admin.site.register(home)
admin.site.register(driver)
admin.site.register(role_mst)
admin.site.register(user_driver_map)
admin.site.register(user_pharmacy_map)
admin.site.register(user_home_map)
admin.site.register(user_patient_map)
admin.site.register(order_mst)
admin.site.register(order_packet_map)
admin.site.register(packet_mst)
admin.site.register(job_mst)
admin.site.register(job_packet_map)
admin.site.register(job_list)
admin.site.register(job_driver_map)
admin.site.register(vehical_type)
admin.site.register(driver_vehical)
admin.site.register(user_mst)
