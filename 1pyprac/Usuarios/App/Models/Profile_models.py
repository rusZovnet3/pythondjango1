from ..models import Profile

class Profile_models():
    
    def getProfile(idUser):
        profile = Profile.objects.select_related().filter(user_id=idUser).first()
        return profile