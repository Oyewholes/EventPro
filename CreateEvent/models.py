from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import misaka
# Create your models here.

class BasicInfo(models.Model):
    name =models.CharField(max_length=255 , unique=True, blank=False)
    organizer =models.CharField(max_length=255, unique=True, blank=False)
    venue= models.CharField(max_length=255, blank=False)
    date = models.DateTimeField()
    image = models.ImageField(default='default_image.jpg', upload_to='Event_Image')
    summary = models.CharField(blank=False, max_length=255)
    details = models.TextField(max_length=500)

    CAMP_RETREAT = 'CR'
    CLASS_TRAINING_WORKSHOP = 'CTW'
    CONCERT_PERFORMANCE = 'CP'
    CONFERENCE = 'CF'
    CONVENTION = 'CV'
    DINNER = 'DN'
    FESTIVAL = 'FST'
    GAME_COMPETITION = 'GC'
    NETWORKING_EVENT = ''
    OTHER = 'OTH'
    SOCIAL_GATHERING = 'SG'
    POLITICAL_RALLY = 'PR'
    SEMINAR = 'SM'

    TYPE_CHOICES = [
        ("SELECT TYPE", "Select Type"),
        ('CAMP_RETREAT','Camp_Retreat'),
        ('CLASS_TRAINING_WORKSHOP','Class_Training_Workshop'),
        ('CONCERT_PERFORMANCE','Concert_Performance'),
        ('CONFERENCE','Conference'),
        ('CONVENTION', 'Convention'),
        ('DINNER', 'Dinner'),
        ('FESTIVAL','Festival'),
        ('GAME_COMPETITION','Game_Competition'),
        ('NETWORKING_EVENT','Networking_Event'),
        ('OTHER', 'Other'),
        ('SOCIAL_GATHERING','Social_Gathering'),
        ('POLITICAL_RALLY', 'Political_Rally'),
        ('SEMINAR', 'Seminar'),
    ]
    type = models.CharField(choices=TYPE_CHOICES, default="Type", max_length=25)

    BUSINESS_or_PROFESSIONAL = 'BR'
    CHARITY = 'CH'
    COMMUNITY_or_CULTURE ='CC'
    FAMILY_or_EDUCATION = 'FE'
    FASHION_or_BEAUTY = 'FB'
    FILM_or_ENTERTAINMENT = 'FET'
    FOOD_or_DRINKS = 'FD'
    GOVERNMENT_or_POLITICS = 'GP'
    HEALTH_or_WELLNESS = 'HW'
    HOBBIES_or_HOLIDAY = 'HH'
    MUSIC_or_LIFESTYLE = 'ML'
    RELIGION_or_SPIRITUALITY = 'RS'
    SCIENCE_or_TECH = 'ST'

    CATEGORY_CHOICES = [
        ("SELECT CATEGORY", "Select Category"),
        ('BUSINESS_or_PROFESSIONAL', 'Business_or_Professional'),
        ('CHARITY','Charity'),
        ('COMMUNITY_or_CULTURE', 'Community_or_Culture'),
        ('FAMILY_or_EDUCATION', 'Family_or_Education'),
        ('FASHION_or_BEAUTY', 'Fashion_or_Beauty'),
        ('FILM_or_ENTERTAINMENT', 'Film_or_Entertainment'),
        ('FOOD_or_DRINKS', 'Food_or_Drinks'),
        ('GOVERNMENT_or_POLITICS', 'Government_or_Politics'),
        ('HEALTH_or_WELLNESS','Health_or_Wellness'),
        ('HOBBIES_or_HOLIDAY','Hobbies_or_Holiday'),
        ('MUSIC_or_LIFESTYLE','Music_or_Lifestyle'),
        ('RELIGION_or_SPIRITUALITY','Religion_or_Spirituality'),
        ('SCIENCE_or_TECH', 'Science_or_Tech'),
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=25, default="Category")


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.name)
        # self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)


class AddTickets(models.Model):
    General_admission = models.CharField(max_length=50, blank=False)
    Available_Quantity = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self):
        return self.General_admission

    def save(self, *args, **kwargs):
        self.slug = slugify(self.General_admission)
        super().save(*args, **kwargs)







# class Dashboard(models.Model):
#     name =models.CharField(max_length=255)
#     slug = models.SlugField(allow_unicode=True)
#     member = models.ManyToManyField(User, through='GroupMember')

