from django import forms
from . import models

class BasicInfoForm(forms.ModelForm):
    class Meta:
        fields =("name", "organizer", "venue", "date", "type","category", "image", "summary","details")
        model =models.BasicInfo
        TYPE_CHOICES =(
                       ("","Select Type"),
                       ('CAMP_RETREAT', 'Camp_Retreat'),
                       ('CLASS_TRAINING_WORKSHOP', 'Class_Training_Workshop'),
                       ('CONCERT_PERFORMANCE', 'Concert_Performance'),
                       ('CONFERENCE', 'Conference'),
                       ('CONVENTION', 'Convention'),
                       ('DINNER', 'Dinner'),
                       ('FESTIVAL', 'Festival'),
                       ('GAME_COMPETITION', 'Game_Competition'),
                       ('NETWORKING_EVENT', 'Networking_Event'),
                       ('OTHER', 'Other'),
                       ('SOCIAL_GATHERING', 'Social_Gathering'),
                       ('POLITICAL_RALLY', 'Political_Rally'),
                       ('SEMINAR', 'Seminar'),
                       )
        widget ={
            'type' : forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
        }
        CATEGORY_CHOICES = (
            ("SELECT CATEGORY", "Select Category"),
            ('BUSINESS_or_PROFESSIONAL', 'Business_or_Professional'),
            ('CHARITY', 'Charity'),
            ('COMMUNITY_or_CULTURE', 'Community_or_Culture'),
            ('FAMILY_or_EDUCATION', 'Family_or_Education'),
            ('FASHION_or_BEAUTY', 'Fashion_or_Beauty'),
            ('FILM_or_ENTERTAINMENT', 'Film_or_Entertainment'),
            ('FOOD_or_DRINKS', 'Food_or_Drinks'),
            ('GOVERNMENT_or_POLITICS', 'Government_or_Politics'),
            ('HEALTH_or_WELLNESS', 'Health_or_Wellness'),
            ('HOBBIES_or_HOLIDAY', 'Hobbies_or_Holiday'),
            ('MUSIC_or_LIFESTYLE', 'Music_or_Lifestyle'),
            ('RELIGION_or_SPIRITUALITY', 'Religion_or_Spirituality'),
            ('SCIENCE_or_TECH', 'Science_or_Tech'),
        )
        widget ={
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-control'}),
        }


class AddTicketsForm(forms.ModelForm):
    class Meta:
        fields = ("General_admission", "Available_Quantity","price")
        model = models.AddTickets