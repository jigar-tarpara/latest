from django.contrib import admin
from .models import add,user_log,pro_display,order_user,home_page_slider,imagee,wishlist,categories,subcategories,product,metadetails,userac,order,cart,alphasubcat
# Register your models here.
class prod(admin.ModelAdmin):
	model=metadetails
	list_display=['pname_get','mp_id','meta_tag','meta_detail']
	def pname_get(self, obj):
		return obj.mp_id.p_name
class slide_class(admin.ModelAdmin):
	model=home_page_slider
	list_display=['slider','thumb','cat','sub','alpha']
class cat(admin.ModelAdmin):
	model=categories
	list_display=['c_id','c_name']

class wish_ex(admin.ModelAdmin):
	model=wishlist
	list_display=['wish_id','ou_id','op_id']

class subcat(admin.ModelAdmin):
	model=subcategories
	list_display=['s_id','sc_id','s_name']
class prodc(admin.ModelAdmin):
	model=product
	list_display=['p_id','ps_id','p_name','thumb','price']
class imgggg(admin.ModelAdmin):
	model=imagee
	list_display=['pp_id','thumb']
class usea(admin.ModelAdmin):
	model=userac
	list_display=['u_id','user_name']
class ordr(admin.ModelAdmin):
	model=order
	list_display=['o_id','ou_id','op_id']
class alpha(admin.ModelAdmin):
	model=alphasubcat
	list_display=['a_id','as_id','as_name']
class car(admin.ModelAdmin):
	model=cart
	list_display=['cart_id','ou_id','op_id']

class orde_ex(admin.ModelAdmin):
	model=order_user
	list_display=['user','o_p_n','total']
class log(admin.ModelAdmin):
	model=user_log
	list_display=['produ','usr_ll','count']
admin.site.register(user_log,log)

admin.site.register(home_page_slider,slide_class)
admin.site.register(categories,cat)
admin.site.register(subcategories,subcat)
admin.site.register(product,prodc)
admin.site.register(metadetails,prod)
admin.site.register(userac,usea)
admin.site.register(order,ordr)
admin.site.register(cart,car)
admin.site.register(alphasubcat,alpha)
admin.site.register(order_user,orde_ex)
admin.site.register(wishlist,wish_ex)
admin.site.register(imagee,imgggg)
admin.site.register(add)
admin.site.register(pro_display)