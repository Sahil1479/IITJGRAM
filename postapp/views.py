from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .forms import CreateUserForm
from .models import Post, Comment, Profile, Postlink, Postvideo, Postdocument
from django.contrib.auth.models import User

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form':form}
        return(render(request, 'postapp/register.html', context))

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return(render(request, 'postapp/login.html', context))
@login_required(login_url = 'login')
def user_logout(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url = 'login')
def home(request):
   
    return render(request, 'postapp/home2.html')

@login_required(login_url = 'login')
def post(request):
    if request.method == "POST":
        image_ = request.FILES['image']
        caption_ = request.POST.get('captions', '')
       
        user_ = request.user

        post_obj = Post(author=user_, image=image_, caption=caption_)
        post_obj.save()

        return(redirect('/viewimages'))

@login_required(login_url = 'login')
def postlink(request):
    if request.method == "POST":
        caption_ = request.POST.get('captions', '')
        link_ = request.POST.get('link', '')
        user_ = request.user

        postlink_obj = Postlink(author=user_,link=link_, caption=caption_)
        postlink_obj.save()

        return(redirect('/viewlinks'))

@login_required(login_url = 'login')
def postvideo(request):
    if request.method == "POST":
        caption_ = request.POST.get('captions', '')
        video_ = request.FILES['video']
        user_ = request.user

        postvideo_obj = Postvideo(author=user_,video=video_, caption=caption_)
        postvideo_obj.save()

        return(redirect('/viewvideos'))

@login_required(login_url = 'login')
def postdocument(request):
    if request.method == "POST":
        caption_ = request.POST.get('captions', '')
        pdf_ = request.FILES['document']
        user_ = request.user

        postdocument_obj = Postdocument(author=user_,pdf=pdf_, caption=caption_)
        postdocument_obj.save()

        return(redirect('/viewdocuments'))


@login_required(login_url = 'login')
def editprofile(request):
    users = request.user
    previous_profile = Profile.objects.filter(author=users)
    previous_profile.delete()
    if request.method == "POST":
        
        profileimage_ = request.FILES['profileimage']
        
        about_ = request.POST.get('about', '')
        branch_ = request.POST.get('branch', '')
        location_ = request.POST.get('location', '')
        facebooklink_ = request.POST.get('facebookaccount', '')
        instagramlink_ = request.POST.get('instagramaccount', '')
        twitterlink_ = request.POST.get('twitteraccount', '')
        linkedinlink_ = request.POST.get('linkedinaccount', '')
        phone_ = request.POST.get('phone', '')
        dob_ = request.POST.get('dob', '')
        professional_skills_ = request.POST.get('professional_skills', '')
        
        users = request.user
        pro_id = users.id
        profile_obj = Profile(author=users,dob=dob_,professional_skills=professional_skills_, location=location_ ,phone=phone_,twitterlink=twitterlink_, instagramlink=instagramlink_, facebooklink=facebooklink_ ,profileimage=profileimage_, about=about_, pro_id=pro_id, branch=branch_)
        profile_obj.save()

        return(redirect('/'))



@login_required(login_url = 'login')
def viewprofile(request):
    users = request.user
    userid = users.id
    
    profile = Profile.objects.get(author=users)
    
    skills = profile.professional_skills
    if skills is not None:
        list_of_skills = skills.split(',')
        context = {'profile':profile, 'list_of_skills':list_of_skills}

    else:
        context = {'profile':profile}
    return render(request, 'postapp/userprofile.html', context)

@login_required(login_url = 'login')
def viewprofile1(request,person_id):

    
    profile = Profile.objects.get(pro_id=person_id)
    
    skills = profile.professional_skills
    if skills is not None:
        list_of_skills = skills.split(',')
        context = {'profile':profile, 'list_of_skills':list_of_skills}

    else:
        context = {'profile':profile}
    return render(request, 'postapp/userprofile2.html', context)

@login_required(login_url = 'login')
def delete_post(request, postid):
    if request.method == 'POST':
        post_ = Post.objects.filter(id=postid)
        post_.delete()
    

    return redirect('/viewimages')

@login_required(login_url = 'login')
def delete_postlink(request, postid1):
    if request.method == 'POST':
        postlink_ = Postlink.objects.filter(id=postid1)
        postlink_.delete()

    return redirect('/viewlinks')

@login_required(login_url = 'login')
def delete_postvideo(request, postid2):
    if request.method == 'POST':
        postvideo_ = Postvideo.objects.filter(id=postid2)
        postvideo_.delete()

    return redirect('/viewvideos')

@login_required(login_url = 'login')
def delete_postdocument(request, postid2):
    if request.method == 'POST':
        postdocument_ = Postdocument.objects.filter(id=postid2)
        postdocument_.delete()

    return redirect('/viewdocuments')

@login_required(login_url = 'login')
def comment(request,post_id):

    if request.method == "POST":
        author_ = request.user
        id_p_ = post_id
        comments_ = request.POST.get('comment', '')

        comment_obj = Comment(author=author_, comments=comments_, id_p=id_p_)
        comment_obj.save()

        return(redirect('/comment/'+ str(id_p_)))
    p_id = post_id
    comment_objects = Comment.objects.filter(id_p = post_id)
    context = {'comment_objects':comment_objects, 'p_id':p_id}
    return render(request, 'postapp/comments.html', context)

# view posts
@login_required(login_url = 'login')
def viewimages(request):
    posts = Post.objects.all().order_by('-id')
    context = {'posts':posts}
    return render(request, 'postapp/viewimages.html', context)

@login_required(login_url = 'login')
def viewlinks(request):
    postlinks = Postlink.objects.all().order_by('-id')
    context = {'postlinks':postlinks}
    return render(request, 'postapp/viewlinks.html', context)

@login_required(login_url = 'login')
def viewvideos(request):
    postvideos = Postvideo.objects.all().order_by('-id')
    context = {'postvideos':postvideos}
    return render(request, 'postapp/viewvideos.html', context)

@login_required(login_url = 'login')
def viewdocuments(request):
    postdocuments = Postdocument.objects.all().order_by('-id')
    context = {'postdocuments':postdocuments}
    return render(request, 'postapp/viewdocuments.html', context)


