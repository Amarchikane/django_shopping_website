from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import contact,Product,Category,Customer
 # https://www.youtube.com/playlist?list=PLK8cqdr55Tsv-D2HMdrnD32oOVBNvmxjr
#  https://www.youtube.com/watch?v=YcwEmCoFEW8&list=PLdBwVRHjcI__NWxctXUSLz1Gg2Mb-B-O-&index=46
# Create your views here.

def main(request):
    products = Product.getAllCategory()
    Categorys= Category.getAllCategory()
    subcategorys= Category.getsubCategory('other')
    distcategorys=Category.getdistinctCategory()
    print(distcategorys)
    # print(" king")
    # print(product.image.url)
    # request.session.set_expiry()
    context={"Products":products,'Category':{"Category":Categorys,"subCategory":distcategorys},'Customer':""}

    if request.session.get('customer'):
        print('costomer id',request.session.get('customer'))
        cstid=request.session.get('customer')
        context['customer']= Customer.getCustomerByid(cstid)[0]
        qurry=Customer.getCustomerByid(cstid)
        print(qurry[0])
        # if not cstid:
        #     Customer=Customer.getCustomerByid(cstid)
        #     context['Customer']= Customer
    if request.method=="GET":
       
        if request.GET.get('category_id'):
            cart = request.session.get('cart')
            if not cart:
             request.session['cart'] = {}
            filterProduct = Product.getProductByFilter(request.GET['category_id'])
            context["Products"]=filterProduct
            return render(request,'main.html',context)
    if request.method=="POST":
        product = request.POST.get('product')
        print(" king1")
        print(product) 
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        print(" king2")
        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('/')
    return render(request,'main.html',context)
def allproducts(request):
    
    products = Product.getAllCategory()
    # print(" king")
    # print(product.image.url)
    # request.session.set_expiry()
    context={"Products":products,'Customer':""}

    if request.session.get('customer'):
        print('costomer id',request.session.get('customer'))
        cstid=request.session.get('customer')
        context['customer']= Customer.getCustomerByid(cstid)[0]
        qurry=Customer.getCustomerByid(cstid)
        print(qurry[0])
        # if not cstid:
        #     Customer=Customer.getCustomerByid(cstid)
        #     context['Customer']= Customer
    if request.method=="GET":
       
        if request.GET.get('category_id'):
            cart = request.session.get('cart')
            if not cart:
             request.session['cart'] = {}
            filterProduct = Product.getProductByFilter(request.GET['category_id'])
            context["Products"]=filterProduct
            return render(request,'allproducts.html',context)
    if request.method=="POST":
        product = request.POST.get('product')
        print(" king1")
        print(product) 
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        print(" king2")
        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('allproducts')
    return render(request,'allproducts.html',context)
def home(request):
    context={'name':'Name',"lastname":"lastname123"}
    return render(request,'home.html',context)
    # return HttpResponse("<h1>this</h1> <h2>home<h2> <h3>the data<h3>")
 
def offer(request):
    return render(request,'offer.html')
    # return HttpResponse("<center><h1>offer</h1><center>")
def delivery(request):
    return render(request,'delivery.html')
    # return HttpResponse("<center><h1>delivery</h1><center>")
def about(request):
    
    return render(request,'about.html')

def cantact(request):
    products = Product.getAllCategory()
    Categorys= Category.getAllCategory()
    # print(" king")
    # print(product.image.url)
    # request.session.set_expiry()
    context={'name':'Name',"lastname":"lastname123"
    ,"Products":products,"Category":Categorys}
    if request.method=="POST":
        name= request.POST['first']
        print(name,"return some thing")
    return render(request,'cantact.html',context)
    # return HttpResponse("<center><h1>cantact</h1><center>")
def login(request):
    context={'error':"",'emailerror':{'error':"",'button':""}}
    if request.method=="POST":
        email= request.POST['Email']
        password= request.POST['password']
        customerEmail = Customer.emailExits(email)
        # print(email,password,customerEmail.password)
        if customerEmail:
            # print("login success")
            if password==customerEmail.password:
                request.session["customer"] = customerEmail.id
                # print("login success")
                # context['error']="login success"
                return redirect('/')
            else:
                print("login not success")
                context['error']="pssword is not correct"
        else:
            context['emailerror']['error']="Invalid Email id"
            context['emailerror']['button']="btn-outline-danger "
        # else:
        #      context[error]="invalid"

        # ins=contact(email=email)
        # ins.save()
    
    return render(request,'login.html',context)
    # return HttpResponse("<center><h1>login</h1><center>")
def checkoutpage(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    ids = list(request.session.get('cart').keys())
    products = Product.getProductById(ids)
    print(len(products))
    
    return render(request,'checkoutpage.html',{"products":products})
def cart(request):
        pId = request.GET.get('increase')
        pidd = request.GET.get('decrease')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(pId)
            if quantity:
                if  request.GET.get('increase'):
                    cart[pId]  = quantity+1
                if request.GET.get('decrease'):
                    if quantity<=1:
                        cart.pop(pidd)
                    else:
                        cart[pidd]  = quantity-1
            quantity = cart.get(pidd)
            if quantity:
                if request.GET.get('decrease'):
                    if quantity<=1:
                        cart.pop(pidd)
                    else:
                        cart[pidd]  = quantity-1
        else:
            cart = {}

        request.session['cart'] = cart
        if not cart:
            request.session['cart'] = {}
        if request.method=="GET":
            if 'cart' not in request.session:
                return render(request , 'cart.html' , {'products' :""} )

            ids = list(request.session.get('cart').keys())
            products = Product.getProductById(ids)
            #  print(products)
            return render(request , 'cart.html' , {'products' : products} )
def addproduct(request):
    Categorys= Category.getAllCategory()
    context={"Category":Categorys}
    if request.method=="POST":
        # print(request.POST)
        product_name = request.POST.get('product_name')
        product_categorie = request.POST.get('product_categorie')
        product_description = request.POST.get('product_description')
        enable_display = request.POST.get('enable_display')
        context['product_name']=product_name
        context['product_categorie']=product_categorie
        context['product_description']=product_description
        context['enable_display']=enable_display
        input_file=False;

        try:
            input_file = request.FILES['filebutton']
            context['input_file']=input_file
            # print(input_file)
        except:
            # print("file error")
            context['fileerror']="Choese a valid image" 
            pass
  
        # print("file error 1")
        if product_name and product_categorie and product_description  and input_file:
            # print("file error 2")
            category=Category.objects.get(name=product_categorie)
            ins=Product(name=product_name,price=1,category=category,description=product_description,image=input_file)
            ins.save()
            context={}
            return redirect('/')
        # return render(request,'addproducct.html',context)
    # print(context)
    return render(request,'addproducct.html',context)  
def logout(request):
	request.session.clear()
	return redirect('/')
def signup(request):
    context={}
    if request.method=="POST":
        # print("signin post methord");
        # print(request.POST)
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        Password = request.POST.get('Password')
        conform_Password = request.POST.get('conform-Password')
        zipcode = request.POST.get('zip')
        address=request.POST.get('address')
        address2=request.POST.get('address2')
        customerEmail = Customer.emailExits(email)
        if customerEmail:
            context['firstName'] = firstName
            context['lastName'] =lastName
            context['zipcode'] = zipcode
            context['address'] = address
            context['address2'] =address2
            context['erremail']="Customer with this Email already exists"
            print(context['erremail'])
            return render(request , 'signup.html' ,context )
        if Password!=conform_Password:
            context['errPassword']="Password missmatch"
            print(context['errPassword'])
            return render(request , 'signup.html' ,context )
        else:
            context['Password'] = Password
            context['conform_Password'] = conform_Password
        
       
        name=firstName+" "+lastName
        ins=Customer(name=name,email=email,password=Password)
        ins.save()
        customerEmail1 = Customer.emailExits(email)
        
        if customerEmail1:
            request.session["customer"] = customerEmail1.id
            return redirect('/')
    return render(request , 'signup.html' ,context )