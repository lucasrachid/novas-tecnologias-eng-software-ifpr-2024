from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "pages/index/index.html"
    
    
class AboutView(TemplateView):
    template_name = "pages/about/about.html"
    
    
class LoginView(TemplateView):
    template_name = "pages/authentication/login/login.html"
    
    
class RecoverPasswordView(TemplateView):
    template_name = "pages/authentication/recover_password/recover_password.html"
    
    
class RegisterView(TemplateView):
    template_name = "pages/authentication/register/register.html"
    

class DefaultView(TemplateView):
    template_name = "pages/default_html/default_html.html"

