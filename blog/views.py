from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.models import User 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django import forms
from .forms import CommentForm

#--------------------------------------------------------------------------------------------------------------------------------------

from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from .models import Category
#--------------------------------------------------------------------------------------------------------------------------------------

def home(request):
	context = {
		"posts": Post.objects.all()
	}
	return render(request, 'blog/home.html', context)



"""
from django.views.generic.edit import UpdateView
from .models import Post

class AuthorUpdate(UpdateView):
    model = Post
	fields = ['title', 'content']
    template_name_suffix = '_update_form'

"""



#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
"""

class TagMixin(objects):
	def get_context_data(self, **kwargs):
		context = super(TagMixin, self).get_context_data(**kwargs)
		context["tags"] = Tag.objects.all()
		return context

"""

#--------------------------------------------------------------------------------------------------------------------------------------


"""

"""

"""

class TagIndexView(ListView):
	model = Post
	paginate_by = 10
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-date_posted')
"""

"""
"""

"""

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------
"""




#--------------------------------------------------------------------------------------------------------------------------------------


def LikeView(request, pk):
	post = get_object_or_404(Post, id= request.POST.get('post_id')) #post id bc we named our in postdetail button name postid. so were saying grabb that and look  that up in Post table. and than assign all of that to post variable in the beginnig of this line.
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('blog-home'))



#--------------------------------------------------------------------------------------------------------------------------------------
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 99
"""

def filter(request):
	    qs = Post.objects.all()
	    categories = Category.objects.all()
	    id_exact_query = request.GET.get('id_exact')
	    title_or_author_query = request.GET.get('title_or_author')
	    category = request.GET.get('category')
	    
	    if is_valid_queryparam(category) and category != 'Choose...':
	      qs = qs.filter(categories__name=category)

"""
"""
def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'categories': Category.objects.all()
    }
    return render(request, "bootstrap_form.html", context)

"""
"""
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 199

"""    
"""
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('category'):
            return qs.filter(categories__name=self.request.GET['category'])
        return qs
"""
"""
    def get_context_data(self, *args, **kwargs):
        context = super().get_queryset(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context

"""


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 199

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		#email = get_object_or_404(User, email=self.kwargs.get('email'))
		return Post.objects.filter(author = user).order_by('-date_posted')

#--------------------------------------------------------------------------------------------------------------------------------------
class LocationPostListView(ListView):
	model = Post
	template_name = 'blog/location_posts.html'
	context_object_name = 'posts'
	paginate_by = 199

	def get_queryset(self):
		user = get_object_or_404(User, loc = self.kwargs.get('loc'))
		return Post.objects.filter(location = user).order_by('-date_posted')
#--------------------------------------------------------------------------------------------------------------------------------------
class TagIndexView(ListView):
	template_name = 'blog/locations.html'
	model = Post
	paginate_by = 99
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-date_posted')

		#tagy = get_object_or_404(Post, tags=self.kwargs.get('tags'))
		#return Post.objects.filter(tags=tagy).order_by('-date_posted')

		#tagy yi slug yap alttakini aç da dene bide



#--------------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------

class PostDetailView(DetailView):
	model = Post


	def get_context_data(self, *args, **kwargs):
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()


		context["total_likes"] = total_likes

		return context
#--------------------------------------------------------------------------------------------------------------------------------------

class PostCreateView(LoginRequiredMixin, CreateView): #inhertttnig from createview
	model = Post
	fields = ['title', 'content', 'tags']  ##bunları models dan çekiyor direk.
	success_url = '/'


	def form_valid(self,form):
		form.instance.author = self.request.user #current logged in user can post it only the post ure trying to post
		return super().form_valid(form)



#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
	model = Post
	fields = ['title', 'content', 'tags']  ##bunları models dan çekiyor direk.
	

	def form_valid(self,form):
		form.instance.author = self.request.user #current logged in user can post it only the post ure trying to post
		return super().form_valid(form)


	def test_func(self): #UserPassesTestMixin için. to make sure current post has the authot of the current logged im user-- listen again--
		post = self.get_object() #gets the post were currently ttrying to update
		if self.request.user == post.author: #gets thte current loggid in user and checks if this is equal to the author were trying to update
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'
	def test_func(self): #UserPassesTestMixin için
		post = self.get_object() #gets the post were currently ttrying to update
		if self.request.user == post.author: #gets thte current loggid in user and checks if this is equal to the author were trying to update
			return True
		return False


#--------------------------------------------------------------------------------------------------------------------------------------


def about(request):
	return render(request, 'blog/about.html', {'title': 'hakkinda'})



def duyuru(request):
	return render(request, 'blog/duyuru.html', {'title': 'duyuru'})


#--------------------------------------------------------------------------------------------------------------------------------------

class AddCommentView(CreateView): #inhertttnig from createview
	model = Comment
	form_class = CommentForm
	template_name = 'blog/add_comment.html'
	#fields = '__all__'  ##bunları models dan çekiyor direk.
	success_url = reverse_lazy('blog-home')


	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)


#--------------------------------------------------------------------------------------------------------------------------------------











