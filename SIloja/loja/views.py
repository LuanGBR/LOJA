from django.shortcuts import redirect, render

from loja.models import Produto,Carrinho,ItemCarrinho


# Create your views here.
def Home(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        resp = render(request, "home.html",{"produtos": produtos} )
        print(resp)
        return render(request, "home.html",{"produtos": produtos} )
    elif request.method == "POST":
        product_id = request.POST["produto"]
        carrinho,_= Carrinho.objects.get_or_create(usuario_id=request.user.id)
        item,_ = ItemCarrinho.objects.get_or_create(carrinho=carrinho,produto_id=product_id)
        item.quantidade += 1
        item.save()
        carrinho.items.add(item)
        return redirect("/home")

def Cart(request):
    if request.method == "GET":
        user = request.user
        print(user.id)
        items = Carrinho.objects.get(usuario_id=user.id).items.all()
        return render(request, 'shopping_cart.html',{"items": items})
    elif request.method == "POST":
        try:
            item_id = request.POST["mais"]
            k = 1
        except KeyError:
            item_id = request.POST["menos"]
            k = -1
        item = ItemCarrinho.objects.get(id=item_id)
        item.quantidade += k
        item.save()
        if item.quantidade <=0:
            item.delete()
        return redirect( "/cart")

        

def checkout(request):
    return