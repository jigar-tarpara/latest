from django.shortcuts import render,HttpResponse
from adminpanel.models import add,pro_display,cart,user_log,wishlist,home_page_slider,imagee,order_user,categories,subcategories,alphasubcat,product,metadetails,userac,order
import os
from django.core.mail import send_mail
import threading
# Create your views here.
def is_login(request):
	if request.session.get('u_id',False):
		return True
	else: 
		return False
def cart_refresh(request):
	return render(request,"cart_refresh.html",{})
def home(request):
	if is_login(request):
		pass
	else:
		request.session['u_name']="Guest"
		request.session['u_surname']="Session"
	param=dict()
	cat=categories.objects.all()
	param['cat']=cat
	sub=subcategories.objects.all()
	param['sub']=sub
	alpha=alphasubcat.objects.all()
	param['alphasubcat']=alpha
	apple=home_page_slider.objects.filter(slider=1)
	samsung=home_page_slider.objects.filter(slider=2)
	fashion=home_page_slider.objects.filter(slider=3)
	try:
		recent_view=user_log.objects.filter(user=userac.objects.get(u_id=request.session['u_id']))[0:]
		past_view=user_log.objects.filter(user=userac.objects.get(u_id=request.session['u_id']))[:4]	
		param['recent']=recent_view
		param['pre']=past_view
	except:
		pass
	param['most1']=user_log.objects.all().order_by("-count")[0:4]
	param['addsss']=add.objects.all()	
	param['slider1']=apple
	param['slider2']=samsung
	param['slider3']=fashion
	param['request']=request
	param['prodisplay_apple']=pro_display.objects.filter(subcat=alphasubcat.objects.get(as_name="Apple"))
	param['prodisplay_women']=pro_display.objects.filter(subcat=alphasubcat.objects.get(as_name="Dresses"))
	param['men']=pro_display.objects.filter(subcat=alphasubcat.objects.get(as_name="Formal Shoes"))	
	if is_login(request):
		ab=render(request,"index.html",param)
		ab.delete_cookie('product')
		return ab
	return render(request,"index.html",param)
def payment(request):
	if is_login(request):
		obj=userac.objects.get(u_id=request.session['u_id'])
	else:
		obj=userac()
	if request.method=="POST":
		obj.user_name=request.POST['firstname']
		obj.user_surname=request.POST['lastname']
		obj.user_email=request.POST['emailid']
		obj.user_s_address=request.POST['saddress']
		obj.user_b_address=request.POST['baddress']
		obj.user_m_number=request.POST['mnumber']
		obj.save()
		request.session['mail']=request.POST['emailid']
	return render(request,"payment.html",{})


	# "<order_user: order_user object>" needs to have a value for field "order_user" before this many-to-many relationship can be used.
def mail_thread(msg,id):
	send_mail('You Order Confirmation',msg,"lanetteam.jigar@gmail.com",[id],html_message=msg)
def orderconfirm(request):
	msg="<strong><h1>Succesfully Place Your Main Order Id: "
	try:
		o_c=order_user.objects.get(user=userac.objects.get(u_id=request.session['u_id']))
		o_c.total=o_c.total+int(request.session['total'])
	except: 
		o_c=order_user()
		try:
			o_c.user=userac.objects.get(u_id=request.session['u_id'])
		except:
			o_c.user=userac.objects.get(user_email=request.session['mail'])
		o_c.total=request.session['total']
	o_c.save()	
	if is_login(request):
		cart_it=cart.objects.filter(ou_id=userac.objects.get(u_id=request.session['u_id']))
		o_c=order_user.objects.get(user=userac.objects.get(u_id=request.session['u_id']))
		msg+=" "+str(o_c.o_user_id)+"</h1> </strong><br>"
		for c in cart_it:		
			obje=order()
			obje.ou_id=c.ou_id
			obje.op_id=c.op_id
			obje.qty=c.qty
			obje.save()
			msg+=" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<h4>sub order id "+str(obje.o_id)+" "+str(obje.op_id.p_name)+" price= "+str(obje.op_id.price)+"</h4>"
			c.delete()
			o_c.o_order_id.add(obje)
		o_c.save()
		msg+="<br>Total= "+request.session['total']
		msg+="<br><h3>Thank You For Ordering</h3>"
		t=threading.Thread(target=mail_thread, args=(msg,(userac.objects.get(u_id=request.session['u_id'])).user_email, ))
		t.start()
		#mail sending
		return render(request,"temp.html",{})
	else:
		o_c=order_user.objects.get(user=userac.objects.get(user_email=request.session['mail']))
		msg+=" "+str(o_c.o_user_id)+"</h1> </strong><br>"
		obj=request.COOKIES['product'].split(',')
		for n in obj:
			po=order()
			po.ou_id=userac.objects.get(user_email=request.session['mail'])
			po.op_id=product.objects.get(p_id=int(n))
			po.qty=1
			po.save()
			msg+=" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<h4>sub order id "+str(po.o_id)+" "+str(po.op_id.p_name)+" price= "+str(po.op_id.price)+"</h4>"
			o_c.o_order_id.add(po)
		o_c.save()
		msg+="<br>Total= "+request.session['total']
		msg+="<br><h3>Thank You For Ordering</h3>"
		t=threading.Thread(target=mail_thread, args=(msg,(userac.objects.get(user_email=request.session['mail']).user_email, )))
		t.start()
		abde=render(request,"temp.html",{})
		abde.delete_cookie('product')
		#mail sending
		return abde
def total(request):
	request.session['total']=request.GET['t']
	return HttpResponse("jigar")
def refresh(request):
	param=dict()
	u=request.session['u_id']
	obj=cart.objects.filter(ou_id=userac.objects.get(u_id=u))
	param['cartproduct']=obj
	return render(request,"refresh.html",param)
def delete_product(request):
	obj=cart.objects.get(cart_id=request.GET['cid'])
	obj.delete()
	return HttpResponse("done")
def checkout(request):
	param=dict()
	cat=categories.objects.all()
	sub=subcategories.objects.all()
	alpha=alphasubcat.objects.all()
	param['cat']=cat
	param['sub']=sub
	param['alphasubcat']=alpha
	if is_login(request):
		obj=userac.objects.get(u_id=request.session['u_id'])
		param['user']=obj	
	return render(request,"checkout.html",param)
def count(request):
	try:
		u=request.session['u_id']
		obj=cart.objects.filter(ou_id=userac.objects.get(u_id=u))
		tot=0;
		for p in obj:
			tot=tot+(p.qty*p.op_id.price)					
		return HttpResponse(tot)
	except:
		try:
			obj=request.COOKIES['product'].split(',')
			tot=0
			for n in obj:
				a=product.objects.get(p_id=int(n))
				tot=tot+(1*a.price)
		except:
			return HttpResponse("0")	
		return HttpResponse(tot)
def qtykart(request):
	try:
		u=request.session['u_id']
		obj=cart.objects.filter(ou_id=userac.objects.get(u_id=u))
		tot=0;
		for p in obj:
			tot=tot+1					
		return HttpResponse(tot)
	except:
		try:
			obj=request.COOKIES['product'].split(',')
			tot=0
			for n in obj:
				a=product.objects.get(p_id=int(n))
				tot=tot+1
		except:
			return HttpResponse("0")	
		return HttpResponse(tot)
def cartpage(request):
	if is_login(request):
		param=dict()
		cat=categories.objects.all()
		sub=subcategories.objects.all()
		alpha=alphasubcat.objects.all()
		param['cat']=cat
		param['sub']=sub
		param['alphasubcat']=alpha
		u=request.session['u_id']
		obj=cart.objects.filter(ou_id=userac.objects.get(u_id=u))
		param['cartproduct']=obj
		return render(request,"cart.html",param)
	else:
		param=dict()
		cat=categories.objects.all()
		sub=subcategories.objects.all()
		alpha=alphasubcat.objects.all()
		param['cat']=cat
		param['sub']=sub
		param['alphasubcat']=alpha
		try:
			obj=request.COOKIES['product'].split(',')
			prrr=[]
			for n in obj:
				prrr.append(product.objects.get(p_id=int(n)))
			param['cartproduct']=prrr
			print("$%$%$%$%$#$#$%#$*******************")
		except:
			print("$%$%$%$%$#$#$%#$")
			return render(request,"cart.html",param)	
		return render(request,"cart.html",param)

def order_display(request):
	param=dict()
	u=request.session['u_id']
	obj=order.objects.filter(ou_id=userac.objects.get(u_id=u))
	param['cartproduct']=obj
	return render(request,"order.html",param)
def cartadd(request):
	if is_login(request):
		obj=cart()
		obj.ou_id=userac.objects.get(u_id=request.GET['u'])
		obj.op_id=product.objects.get(p_id=request.GET['p'])
		obj.qty=1
		obj.save()
		return HttpResponse("ok cart added "+request.GET['p']+" "+request.GET['u'])
	else:
		obj=HttpResponse("ok cart added "+request.GET['p']+" "+request.GET['u'])
		if "product" in request.COOKIES:
			pr=request.COOKIES['product']
			pr+=","+request.GET['p']
		else:
			pr=""+request.GET['p']
		obj.set_cookie("product",pr)
		return obj
	
def wish(request):
	if is_login(request):
		obj=wishlist()
		obj.ou_id=userac.objects.get(u_id=request.GET['u'])
		obj.op_id=product.objects.get(p_id=request.GET['p'])
		obj.qty=1
		obj.save()
		return HttpResponse("ok wishlist added "+request.GET['p']+" "+request.GET['u'])
	else:
		obj=HttpResponse("ok wishlist added "+request.GET['p']+" "+request.GET['u'])
		if "wishitem" in request.COOKIES:
			pr=request.COOKIES['wishitem']
			pr+=","+request.GET['p']
		else:
			pr=""+request.GET['p']
		obj.set_cookie("wishitem",pr)
		return obj
def updateqty(request):
	obj=cart.objects.get(cart_id=request.GET['cid'])
	obj.qty=request.GET['qty']
	obj.save()
	return HttpResponse("ok updated "+request.GET['qty'])
def logout(request):
	request.session.flush()
	return home(request)
def login(request):
	param=dict()
	if request.method=="POST":
		if request.POST['passs']==(userac.objects.get(user_email=request.POST['emailid'])).user_password:
			request.session['u_id']=(userac.objects.get(user_email=request.POST['emailid'])).u_id
			request.session['u_name']=(userac.objects.get(user_email=request.POST['emailid'])).user_name
			request.session['u_surname']=(userac.objects.get(user_email=request.POST['emailid'])).user_surname
			cat=categories.objects.all()
			sub=subcategories.objects.all()
			alpha=alphasubcat.objects.all()
			param['cat']=cat
			param['sub']=sub
			param['alphasubcat']=alpha
			responsee=render(request,"temp.html",{})
			responsee.delete_cookie('product')
			return responsee
		else:
			return HttpResponse("wrong username or password")			
	return render(request,"temp.html",{})
def register(request):
	param=dict()
	param['request']=request
	if request.method=="POST":
		if request.POST['passs']==request.POST['confirmpass']:
			obj=userac()
			obj.user_name=request.POST['username']
			obj.user_surname=request.POST['usersurname']
			obj.user_email=request.POST['useremail']
			obj.user_password=request.POST['passs']
			obj.save()
		else:
			param['message']="password and confirm password not matched"
	cat=categories.objects.all()
	sub=subcategories.objects.all()
	param['cat']=cat
	param['sub']=sub
	return render(request,"register.html",param)

def single(request):
	param=dict()
	if is_login(request):
		log_prod=user_log.objects.all()
		for log in log_prod:
			if log.produ==product.objects.get(p_name=request.GET['p']):
				temp=user_log.objects.get(produ=product.objects.get(p_name=request.GET['p']))
				temp.count=temp.count+1
				temp.save()
				temp=user_log.objects.get(produ=product.objects.get(p_name=request.GET['p']))
				temp.user.add(userac.objects.get(u_id=request.session['u_id']))
				temp.save()
				break
		else:
			temp=user_log()
			temp.produ=product.objects.get(p_name=request.GET['p'])
			temp.count=temp.count+1
			temp.save()
			temp=user_log.objects.get(produ=product.objects.get(p_name=request.GET['p']))
			temp.user.add(userac.objects.get(u_id=request.session['u_id']))
			temp.save()
	else:
		log_prod=user_log.objects.all()
		for log in log_prod:
			if log.produ==product.objects.get(p_name=request.GET['p']):
				temp=user_log.objects.get(produ=product.objects.get(p_name=request.GET['p']))
				temp.count=temp.count+1
				temp.save()
				break
		else:
			temp=user_log()
			temp.produ=product.objects.get(p_name=request.GET['p'])
			temp.count=temp.count+1
			temp.save()

	param['request']=request
	cat=categories.objects.all()
	sub=subcategories.objects.all()
	temp=request.GET['p']
	prod=product.objects.get(p_name=temp)
	meta=metadetails.objects.filter(mp_id=prod)
	img=imagee.objects.filter(pp_id=prod)
	flag="none"
	abc2="none"
	for m in meta:
		if m.meta_tag=="size":
			abc2="size"
	for m in meta:
		if m.meta_tag=="color":
			flag="color"
	param['img']=img
	param['prod']=prod
	param['cat']=cat
	param['sub']=sub
	param['meta']=meta
	param['flag']=flag
	param['abc2']=abc2
	alpha=alphasubcat.objects.all()
	param['alphasubcat']=alpha
	recom=product.objects.filter(ps_id=((product.objects.get(p_name=temp)).ps_id))[:2]
	param['recom']=recom
	return render(request,"details.html",param)
def subcat(request):
	sub=request.GET['subca']
	cate=request.GET['cat']
	cat=alphasubcat.objects.filter(as_id=subcategories.objects.get(sc_id=categories.objects.get(c_name=cate),s_name=sub))
	param=dict()
	param['request']=request
	param['alphasub']=cat
	param['cat']=cate
	param['sub']=sub
	return render(request,"alphasubcat.html",param)

def produc(request):
	param=dict()
	param['request']=request
	cat=categories.objects.all()
	sub=subcategories.objects.all()
	temp=request.GET['p']
	cate=request.GET['cat']
	alpha=alphasubcat.objects.all()
	param['alphasubcat']=alpha
	prod=product.objects.filter(ps_id=alphasubcat.objects.get(as_name=temp,as_id=subcategories.objects.get(s_name=cate,sc_id=categories.objects.get(c_name=request.GET['mcat']))))
	param['page']=prod
	param['cat']=cat
	param['sub']=sub
	return render(request,"product.html",param)

def emptycart(request):
	if is_login(request):
		usr=userac.objects.get(u_id=request.session['u_id'])
		p=cart.objects.filter(ou_id=usr)
		for pr in p:
			pr.delete()
	else:
		ab=render(request,"index.html",{})
		ab.delete_cookie('product')
		return ab
	return HttpResponse("done")