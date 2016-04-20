jQuery(document).ready(function($){

				$(".cart").click(function(){
					//alert("this is cart page");
					window.location.replace("/cartpage");
				});

				$("#checkout").click(function(){
					$.ajax({
 					 	type:"get",
 					 	url:"/total/",
 					 	data:"t="+$("#totala").text(),
 					 	success:function(data){
 					 		alert("ok amout save");
 					 	}
 					 });					
					window.location.replace("/checkout");
				});

				function count()
				{

					$.ajax({
 					 	type:"get",
 					 	url:"/count/",
 					 	success:function(data){
 					 		$("#totala").text(data);
 					 	}
 					 });
					
					
				}
				

				jQuery('.qty_btn').click(function(){
 					 var a=$(this).parent().find('input[type=text]').val();
 					 var b=$(this).parent().find('input[type=text]').attr("data-a");
 					 $.ajax({
 					 	type:"get",
 					 	url:"/updateqty/",
 					 	data:"qty="+a+"&cid="+b,
 					 	success:function(data){
 					 		
 					 		count();
 					 	}
 					 });
				});


				jQuery('.delete_btn').click(function(){
					alert("delete");
 					  var b=$(this).attr("data-a");
 					
 					 $.ajax({
 					 	type:"get",
 					 	url:"/delete_product/",
 					 	data:"cid="+b,
 					 	success:function(data){
 					 		
 					 		count();
 					 		$.ajax({
					 					 	type:"get",
					 					 	url:"/refresh/", 					 	
					 					 	success:function(data){
					 					 		
					 					 		$("#refresh").html(data);
					 					 		//$("#hello").html(data);
					 					 	}
 					 				});
 					 	}
 					 });
				});

				
				$('#etalage').etalage({
					thumb_image_width: 300,
					thumb_image_height: 400,
					source_image_width: 900,
					source_image_height: 1200,
					show_hint: true,
					click_callback: function(image_anchor, instance_id){
						alert('Callback example:\nYou clicked on an image with the anchor: "'+image_anchor+'"\n(in Etalage instance: "'+instance_id+'")');
					}
				});

			});