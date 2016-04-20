from django.db import models

# Create your models here.
class categories(models.Model):
	c_id=models.AutoField(primary_key=True)
	c_name=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.c_name

class subcategories(models.Model):
	s_id=models.AutoField(primary_key=True)
	sc_id=models.ForeignKey(categories,on_delete=models.CASCADE)
	s_name=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.s_name

class alphasubcat(models.Model):
	a_id=models.AutoField(primary_key=True)
	as_id=models.ForeignKey(subcategories,on_delete=models.CASCADE)
	as_name=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.as_name

class product(models.Model):
	p_id=models.AutoField(primary_key=True)
	ps_id=models.ForeignKey(alphasubcat,on_delete=models.CASCADE)
	p_name=models.CharField(max_length=100,null=True,blank=True)
	p_discription=models.CharField(max_length=400,null=True,blank=True)
	photo = models.ImageField(upload_to='productimage',blank=True)
	photo2= models.ImageField(upload_to='productimage',blank=True)
	price=models.IntegerField()
	def thumb(self):
		if self.photo:
			return u'<img src="/static/%s" alt="not found" width="120" height="120" />' % (self.photo)
		else:
			return u'No image file found'
	thumb.short_description = 'Thumb'
	thumb.allow_tags = True
	def __str__(self):
		return self.p_name
class imagee(models.Model):
	p_id=models.AutoField(primary_key=True)
	photo = models.ImageField(upload_to='productimage',blank=True)
	pp_id=models.ForeignKey(product,on_delete=models.CASCADE)
	def thumb(self):
		if self.photo:
			return u'<img src="/static/%s" alt="not found" width="100" height="200" />' % (self.photo)
		else:
			return u'No image file found'
	thumb.short_description = 'Thumb'
	thumb.allow_tags = True
	def __int__(self):
		return self.p_id

class metadetails(models.Model):
	m_id=models.AutoField(primary_key=True)
	mp_id=models.ForeignKey(product,on_delete=models.CASCADE)
	meta_tag=models.CharField(max_length=100,null=True,blank=True)
	meta_detail=models.CharField(max_length=100,null=True,blank=True)
	def hellosplit(self):
		return self.meta_detail.split(',')
	def __str__(self):
		return self.meta_tag

class userac(models.Model):
	u_id=models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=100,unique=True)
	user_surname=models.CharField(max_length=100,unique=True)
	user_email=models.CharField(max_length=100,unique=True)
	user_password=models.CharField(max_length=100,null=True,blank=True)
	user_s_address=models.CharField(max_length=500,null=True,blank=True)
	user_b_address=models.CharField(max_length=500,null=True,blank=True)
	user_m_number=models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.user_name


class order(models.Model):
	o_id=models.AutoField(primary_key=True)
	ou_id=models.ForeignKey(userac,on_delete=models.CASCADE)
	op_id=models.ForeignKey(product,on_delete=models.CASCADE)
	qty=models.IntegerField()
	def __int__(self):
		return self.o_id
class order_user(models.Model):
	o_user_id=models.AutoField(primary_key=True)
	user=models.ForeignKey(userac,on_delete=models.CASCADE)
	o_order_id=models.ManyToManyField(order)
	total=models.IntegerField()
	def o_p_n(self):
		return ",".join([str(p.op_id.p_name) for p in self.o_order_id.all()])
	def __str__(self):
		return self.user.user_name

class cart(models.Model):
	cart_id=models.AutoField(primary_key=True)
	ou_id=models.ForeignKey(userac,on_delete=models.CASCADE)
	op_id=models.ForeignKey(product,on_delete=models.CASCADE)
	qty=models.IntegerField()
	def __int__(self):
		return self.cart_id
class wishlist(models.Model):
	wish_id=models.AutoField(primary_key=True)
	ou_id=models.ForeignKey(userac,on_delete=models.CASCADE)
	op_id=models.ForeignKey(product,on_delete=models.CASCADE)
	qty=models.IntegerField()
	def __int__(self):
		return self.cart_id

class user_log(models.Model):
	log_id=models.AutoField(primary_key=True)
	produ=models.OneToOneField(product,on_delete=models.CASCADE)
	user=models.ManyToManyField(userac)
	count=models.PositiveSmallIntegerField(default=0)
	def usr_ll(self):
		return ",".join([str(p.user_name) for p in self.user.all()])


class home_page_slider(models.Model):
	slider=models.IntegerField()
	photo = models.ImageField(upload_to='productimage',blank=True)
	cat=models.ForeignKey(categories,on_delete=models.CASCADE)
	sub=models.ForeignKey(subcategories,on_delete=models.CASCADE)
	alpha=models.ForeignKey(alphasubcat,on_delete=models.CASCADE)
	def thumb(self):
		if self.photo:
			return u'<img src="/static/%s" alt="not found" width="200" height="87" />' % (self.photo)
		else:
			return u'No image file found'
	thumb.short_description = 'Thumb'
	thumb.allow_tags = True
	def __int__(self):
		return self.slider

class add(models.Model):
	prod=models.ForeignKey(product,on_delete=models.CASCADE)
	def __str__(self):
		return self.prod.p_name

class pro_display(models.Model):
	subcat=models.ForeignKey(alphasubcat,on_delete=models.CASCADE)
	prod=models.ForeignKey(product,on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='productimage',blank=True)
	def __str__(self):
		return self.subcat.as_name