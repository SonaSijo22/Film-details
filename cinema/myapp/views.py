from django.shortcuts import render,redirect   #djangoyil shortcutsil ahnu render define chaythirikkunnathu

from myapp.models import Movie    #myapp enna applictionil  modelsilae movieinae import chayyunnu

from django.views.generic import View

from myapp.forms import MovieForm

# Create your views here.
#     1.MOVIE
#     --------
# post: serverilekku submit chayyan
# get : ornam maathram kittan

# listing all movies
# url:localhost:8000/movies/all/
# Httpmethod:get()
# standards:camelCase===>ee case use chayyunnathu second word start uppercase ayeerikkum,snake_case(functions,variables)====>ethil underscore varunnathu,PascalCase(class name)====>ethil first word uppercase,kabab-case

# >>> view for listing all movies
# ---------------------------
# def movie_list_view(request,*args,**kwargs):    function based view
#   qs=Movie.objects.all()
#   return render(request,'movie_list.html',{'data':qs}) #render enna functonil 3 kaarangal ahnu ullathu 1.request=====>important,2.template name,3.dictionary context


# class based view for listing all movies
# ----------------------------------------
 
class MovieListView(View):
  def get(self,request,*args, **kwargs):
    qs=Movie.objects.all()
    return render(request,'movie_list.html',{'data':qs})


# >>> view for creating movie
# -----------------------
# url:localhost:8000/myapp/movies/add/
# method:get,post

class MovieCreateView(View):
  def get(self,request,*args, **kwargs):
    form=MovieForm()   #object create chaythekkunnu
    return render(request,"movie_add.html",{"form":form})

  def post(self,request,*args, **kwargs):   #movie cretae view methodilae post method work chayyan vendi
    form=MovieForm(request.POST,files=request.FILES)
    
    if form.is_valid():
              # form.save()
      data=form.cleaned_data
      Movie.objects.create(**data)
      return redirect("movie-list")   #redirect chayyan vendi use chayyunnu add movies pageil ninnu movies all pagesilekku ponam
    return render(request,"movie_add.html",{"form":form})


#>>> movie detail view
# --------------------
# localhost:8000/myapp/movies/{id}/
# method:get()
class MovieDetailView(View):
  def get(self,request,*args, **kwargs):
    print(kwargs)#kwargs={"pk":6}
    id=kwargs.get("pk")#pk for primary key
    qs=Movie.objects.get(id=id)
    return render(request,"movie_detail.html",{"data":qs})

# >>>movie delete view
# ---------------------
# localhost:8000/myapp/movies/{id}/remove
# method:get() 

class MovieDeleteView(View):
  def get(self,request,*args, **kwargs):
    id=kwargs.get("pk")  #urlinu id edukkanam aa id ulla movie ekete chayyanam
    Movie.objects.get(id=id).delete()#delete chayyan ulla orm query
    return redirect("movie-list")


# >>>update movie view
# ------------------
# localhost:8000/myapp/movies/{id}/update
# method:get()

class MovieUpdateView(View):
  def get(self,request,*args, **kwargs):
    id=kwargs.get("pk") #id extract chaythu
    movie_object=Movie.objects.get(id=id)#ee id ulla movie object edukanam
    form=MovieForm(instance=movie_object)  #movies add il ulla athe form thannae ahnu nammukku avashyam athu kodnu form=movie form ennu koudtu and ee object movie_object vechu initialize chayyanam
    return render(request,"movie_edit.html",{"form":form}) #ee forminae kondu oru templateilekku ponam athinu edit template create chayynam
  # for updatiung we use post method

  def post(self,request,*args, **kwargs):
    # data=request.POST
    id=kwargs.get("pk")
    movie_object=Movie.objects.get(id=id)
    form=MovieForm(request.POST,files=request.FILES,instance=movie_object)
    if form.is_valid():
      form.save()
      # data=form.cleaned_data
      # Movie.objects.filter(id=id).update(**data)
      return redirect("movie-list")
    else:
      return render(request,"movie_edit.html",{"form":form})

