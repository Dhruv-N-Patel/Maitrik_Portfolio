from django.shortcuts import render
from .models import Blog, Project, Skill, Certification, Education, WorkExperience
from django.shortcuts import render, redirect
from .models import ContactForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ContactForm
import pycountry
from django.http import FileResponse
from django.conf import settings
import os

def home(request):
    skills = Skill.objects.all()
    achievements = Certification.objects.all()
    education = Education.objects.all()
    
    return render(request, 'home.html', context = {'skills': skills, 'achievements': achievements, 'education': education})

def work(request):
    professional = WorkExperience.objects.filter(type='professional')
    por = WorkExperience.objects.filter(type='POR')
    
    return render(request, 'work.html', context={'professional':professional,'por':por})

def blog_page(request):
    return render(request, 'blog_page.html')

def contact(request):
    COUNTRY_CODES = (
    ('+7', '+7 - Russia'),
    ('+20', '+20 - Egypt'),
    ('+27', '+27 - South Africa'),
    ('+30', '+30 - Greece'),
    ('+31', '+31 - Netherlands'),
    ('+32', '+32 - Belgium'),
    ('+33', '+33 - France'),
    ('+34', '+34 - Spain'),
    ('+36', '+36 - Hungary'),
    ('+39', '+39 - Italy'),
    ('+40', '+40 - Romania'),
    ('+41', '+41 - Switzerland'),
    ('+43', '+43 - Austria'),
    ('+44', '+44 - United Kingdom'),
    ('+45', '+45 - Denmark'),
    ('+46', '+46 - Sweden'),
    ('+47', '+47 - Norway'),
    ('+48', '+48 - Poland'),
    ('+49', '+49 - Germany'),
    ('+51', '+51 - Peru'),
    ('+52', '+52 - Mexico'),
    ('+53', '+53 - Cuba'),
    ('+54', '+54 - Argentina'),
    ('+55', '+55 - Brazil'),
    ('+56', '+56 - Chile'),
    ('+57', '+57 - Colombia'),
    ('+58', '+58 - Venezuela'),
    ('+60', '+60 - Malaysia'),
    ('+61', '+61 - Australia'),
    ('+62', '+62 - Indonesia'),
    ('+63', '+63 - Philippines'),
    ('+64', '+64 - New Zealand'),
    ('+65', '+65 - Singapore'),
    ('+66', '+66 - Thailand'),
    ('+81', '+81 - Japan'),
    ('+82', '+82 - South Korea'),
    ('+84', '+84 - Vietnam'),
    ('+86', '+86 - China'),
    ('+90', '+90 - Turkey'),
    ('+91', '+91 - India'),
    ('+92', '+92 - Pakistan'),
    ('+93', '+93 - Afghanistan'),
    ('+94', '+94 - Sri Lanka'),
    ('+95', '+95 - Myanmar'),
    ('+98', '+98 - Iran'),
    ('+212', '+212 - Morocco'),
    ('+213', '+213 - Algeria'),
    ('+216', '+216 - Tunisia'),
    ('+218', '+218 - Libya'),
    ('+220', '+220 - Gambia'),
    ('+221', '+221 - Senegal'),
    ('+222', '+222 - Mauritania'),
    ('+223', '+223 - Mali'),
    ('+224', '+224 - Guinea'),
    ('+225', '+225 - Ivory Coast'),
    ('+226', '+226 - Burkina Faso'),
    ('+227', '+227 - Niger'),
    ('+228', '+228 - Togo'),
    ('+229', '+229 - Benin'),
    ('+230', '+230 - Mauritius'),
    ('+231', '+231 - Liberia'),
    ('+232', '+232 - Sierra Leone'),
    ('+233', '+233 - Ghana'),
    ('+234', '+234 - Nigeria'),
    ('+235', '+235 - Chad'),
    ('+236', '+236 - Central African Republic'),
    ('+237', '+237 - Cameroon'),
    ('+238', '+238 - Cape Verde'),
    ('+239', '+239 - Sao Tome and Principe'),
    ('+240', '+240 - Equatorial Guinea'),
    ('+241', '+241 - Gabon'),
    ('+242', '+242 - Republic of the Congo'),
    ('+243', '+243 - Democratic Republic of the Congo'),
    ('+244', '+244 - Angola'),
    ('+245', '+245 - Guinea-Bissau'),
    ('+246', '+246 - British Indian Ocean Territory'),
    ('+247', '+247 - Ascension Island'),
    ('+248', '+248 - Seychelles'),
    ('+249', '+249 - Sudan'),
    ('+250', '+250 - Rwanda'),
    ('+251', '+251 - Ethiopia'),
    ('+252', '+252 - Somalia'),
    ('+253', '+253 - Djibouti'),
    ('+254', '+254 - Kenya'),
    ('+255', '+255 - Tanzania'),
    ('+256', '+256 - Uganda'),
    ('+257', '+257 - Burundi'),
    ('+258', '+258 - Mozambique'),
    ('+260', '+260 - Zambia'),
    ('+261', '+261 - Madagascar'),
    ('+262', '+262 - Reunion'),
    ('+263', '+263 - Zimbabwe'),
    ('+264', '+264 - Namibia'),
    ('+265', '+265 - Malawi'),
    ('+266', '+266 - Lesotho'),
    ('+267', '+267 - Botswana'),
    ('+268', '+268 - Swaziland'),
    ('+269', '+269 - Comoros'),
    ('+290', '+290 - Saint Helena'),
    ('+291', '+291 - Eritrea'),
    ('+297', '+297 - Aruba'),
    ('+298', '+298 - Faroe Islands'),
    ('+299', '+299 - Greenland'),
    ('+350', '+350 - Gibraltar'),
    ('+351', '+351 - Portugal'),
    ('+352', '+352 - Luxembourg'),
    ('+353', '+353 - Ireland'),
    ('+354', '+354 - Iceland'),
    ('+355', '+355 - Albania'),
    ('+356', '+356 - Malta'),
    ('+357', '+357 - Cyprus'),
    ('+358', '+358 - Finland'),
    ('+359', '+359 - Bulgaria'),
    ('+370', '+370 - Lithuania'),
    ('+371', '+371 - Latvia'),
    ('+372', '+372 - Estonia'),
    ('+373', '+373 - Moldova'),
    ('+374', '+374 - Armenia'),
    ('+375', '+375 - Belarus'),
    ('+376', '+376 - Andorra'),
    ('+377', '+377 - Monaco'),
    ('+378', '+378 - San Marino'),
    ('+380', '+380 - Ukraine'),
    ('+381', '+381 - Serbia'),
    ('+382', '+382 - Montenegro'),
    ('+385', '+385 - Croatia'),
    ('+386', '+386 - Slovenia'),
    ('+387', '+387 - Bosnia and Herzegovina'),
    ('+389', '+389 - North Macedonia'),
    ('+420', '+420 - Czech Republic'),
    ('+421', '+421 - Slovakia'),
    ('+423', '+423 - Liechtenstein'),
    ('+500', '+500 - Falkland Islands'),
    ('+501', '+501 - Belize'),
    ('+502', '+502 - Guatemala'),
    ('+503', '+503 - El Salvador'),
    ('+504', '+504 - Honduras'),
    ('+505', '+505 - Nicaragua'),
    ('+506', '+506 - Costa Rica'),
    ('+507', '+507 - Panama'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+509', '+509 - Haiti'),
    ('+590', '+590 - Guadeloupe'),
    ('+591', '+591 - Bolivia'),
    ('+592', '+592 - Guyana'),
    ('+593', '+593 - Ecuador'),
    ('+594', '+594 - French Guiana'),
    ('+595', '+595 - Paraguay'),
    ('+596', '+596 - Martinique'),
    ('+597', '+597 - Suriname'),
    ('+598', '+598 - Uruguay'),
    ('+599', '+599 - Caribbean Netherlands'),
    ('+670', '+670 - East Timor'),
    ('+672', '+672 - Norfolk Island'),
    ('+673', '+673 - Brunei'),
    ('+674', '+674 - Nauru'),
    ('+675', '+675 - Papua New Guinea'),
    ('+676', '+676 - Tonga'),
    ('+677', '+677 - Solomon Islands'),
    ('+678', '+678 - Vanuatu'),
    ('+679', '+679 - Fiji'),
    ('+680', '+680 - Palau'),
    ('+681', '+681 - Wallis and Futuna'),
    ('+682', '+682 - Cook Islands'),
    ('+683', '+683 - Niue'),
    ('+685', '+685 - Samoa'),
    ('+686', '+686 - Kiribati'),
    ('+687', '+687 - New Caledonia'),
    ('+688', '+688 - Tuvalu'),
    ('+689', '+689 - French Polynesia'),
    ('+690', '+690 - Tokelau'),
    ('+691', '+691 - Micronesia'),
    ('+692', '+692 - Marshall Islands'),
    ('+850', '+850 - North Korea'),
    ('+852', '+852 - Hong Kong'),
    ('+853', '+853 - Macao'),
    ('+855', '+855 - Cambodia'),
    ('+856', '+856 - Laos'),
    ('+880', '+880 - Bangladesh'),
    ('+886', '+886 - Taiwan'),
    ('+960', '+960 - Maldives'),
    ('+961', '+961 - Lebanon'),
    ('+962', '+962 - Jordan'),
    ('+963', '+963 - Syria'),
    ('+964', '+964 - Iraq'),
    ('+965', '+965 - Kuwait'),
    ('+966', '+966 - Saudi Arabia'),
    ('+967', '+967 - Yemen'),
    ('+968', '+968 - Oman'),
    ('+970', '+970 - Palestine'),
    ('+971', '+971 - United Arab Emirates'),
    ('+972', '+972 - Israel'),
    ('+973', '+973 - Bahrain'),
    ('+974', '+974 - Qatar'),
    ('+975', '+975 - Bhutan'),
    ('+976', '+976 - Mongolia'),
    ('+977', '+977 - Nepal'),
    ('+992', '+992 - Tajikistan'),
    ('+993', '+993 - Turkmenistan'),
    ('+994', '+994 - Azerbaijan'),
    ('+995', '+995 - Georgia'),
    ('+996', '+996 - Kyrgyzstan'),
    ('+998', '+998 - Uzbekistan'),
)
    context = {
               'COUNTRY_CODES': COUNTRY_CODES
               }
    return render(request, 'contact.html', context )

def content(request):
    blogs = Blog.objects.all()
    engineering = Blog.objects.filter(genre='engineering')
    personal = Blog.objects.filter(genre='personal')
    

    return render(request, "content.html", context={'blogs':blogs, 'engineering':engineering, 'personal':personal})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', context = {'projects': projects})

def contact_form_submit(request):
    COUNTRY_CODES = (
    ('+7', '+7 - Russia'),
    ('+20', '+20 - Egypt'),
    ('+27', '+27 - South Africa'),
    ('+30', '+30 - Greece'),
    ('+31', '+31 - Netherlands'),
    ('+32', '+32 - Belgium'),
    ('+33', '+33 - France'),
    ('+34', '+34 - Spain'),
    ('+36', '+36 - Hungary'),
    ('+39', '+39 - Italy'),
    ('+40', '+40 - Romania'),
    ('+41', '+41 - Switzerland'),
    ('+43', '+43 - Austria'),
    ('+44', '+44 - United Kingdom'),
    ('+45', '+45 - Denmark'),
    ('+46', '+46 - Sweden'),
    ('+47', '+47 - Norway'),
    ('+48', '+48 - Poland'),
    ('+49', '+49 - Germany'),
    ('+51', '+51 - Peru'),
    ('+52', '+52 - Mexico'),
    ('+53', '+53 - Cuba'),
    ('+54', '+54 - Argentina'),
    ('+55', '+55 - Brazil'),
    ('+56', '+56 - Chile'),
    ('+57', '+57 - Colombia'),
    ('+58', '+58 - Venezuela'),
    ('+60', '+60 - Malaysia'),
    ('+61', '+61 - Australia'),
    ('+62', '+62 - Indonesia'),
    ('+63', '+63 - Philippines'),
    ('+64', '+64 - New Zealand'),
    ('+65', '+65 - Singapore'),
    ('+66', '+66 - Thailand'),
    ('+81', '+81 - Japan'),
    ('+82', '+82 - South Korea'),
    ('+84', '+84 - Vietnam'),
    ('+86', '+86 - China'),
    ('+90', '+90 - Turkey'),
    ('+91', '+91 - India'),
    ('+92', '+92 - Pakistan'),
    ('+93', '+93 - Afghanistan'),
    ('+94', '+94 - Sri Lanka'),
    ('+95', '+95 - Myanmar'),
    ('+98', '+98 - Iran'),
    ('+212', '+212 - Morocco'),
    ('+213', '+213 - Algeria'),
    ('+216', '+216 - Tunisia'),
    ('+218', '+218 - Libya'),
    ('+220', '+220 - Gambia'),
    ('+221', '+221 - Senegal'),
    ('+222', '+222 - Mauritania'),
    ('+223', '+223 - Mali'),
    ('+224', '+224 - Guinea'),
    ('+225', '+225 - Ivory Coast'),
    ('+226', '+226 - Burkina Faso'),
    ('+227', '+227 - Niger'),
    ('+228', '+228 - Togo'),
    ('+229', '+229 - Benin'),
    ('+230', '+230 - Mauritius'),
    ('+231', '+231 - Liberia'),
    ('+232', '+232 - Sierra Leone'),
    ('+233', '+233 - Ghana'),
    ('+234', '+234 - Nigeria'),
    ('+235', '+235 - Chad'),
    ('+236', '+236 - Central African Republic'),
    ('+237', '+237 - Cameroon'),
    ('+238', '+238 - Cape Verde'),
    ('+239', '+239 - Sao Tome and Principe'),
    ('+240', '+240 - Equatorial Guinea'),
    ('+241', '+241 - Gabon'),
    ('+242', '+242 - Republic of the Congo'),
    ('+243', '+243 - Democratic Republic of the Congo'),
    ('+244', '+244 - Angola'),
    ('+245', '+245 - Guinea-Bissau'),
    ('+246', '+246 - British Indian Ocean Territory'),
    ('+247', '+247 - Ascension Island'),
    ('+248', '+248 - Seychelles'),
    ('+249', '+249 - Sudan'),
    ('+250', '+250 - Rwanda'),
    ('+251', '+251 - Ethiopia'),
    ('+252', '+252 - Somalia'),
    ('+253', '+253 - Djibouti'),
    ('+254', '+254 - Kenya'),
    ('+255', '+255 - Tanzania'),
    ('+256', '+256 - Uganda'),
    ('+257', '+257 - Burundi'),
    ('+258', '+258 - Mozambique'),
    ('+260', '+260 - Zambia'),
    ('+261', '+261 - Madagascar'),
    ('+262', '+262 - Reunion'),
    ('+263', '+263 - Zimbabwe'),
    ('+264', '+264 - Namibia'),
    ('+265', '+265 - Malawi'),
    ('+266', '+266 - Lesotho'),
    ('+267', '+267 - Botswana'),
    ('+268', '+268 - Swaziland'),
    ('+269', '+269 - Comoros'),
    ('+290', '+290 - Saint Helena'),
    ('+291', '+291 - Eritrea'),
    ('+297', '+297 - Aruba'),
    ('+298', '+298 - Faroe Islands'),
    ('+299', '+299 - Greenland'),
    ('+350', '+350 - Gibraltar'),
    ('+351', '+351 - Portugal'),
    ('+352', '+352 - Luxembourg'),
    ('+353', '+353 - Ireland'),
    ('+354', '+354 - Iceland'),
    ('+355', '+355 - Albania'),
    ('+356', '+356 - Malta'),
    ('+357', '+357 - Cyprus'),
    ('+358', '+358 - Finland'),
    ('+359', '+359 - Bulgaria'),
    ('+370', '+370 - Lithuania'),
    ('+371', '+371 - Latvia'),
    ('+372', '+372 - Estonia'),
    ('+373', '+373 - Moldova'),
    ('+374', '+374 - Armenia'),
    ('+375', '+375 - Belarus'),
    ('+376', '+376 - Andorra'),
    ('+377', '+377 - Monaco'),
    ('+378', '+378 - San Marino'),
    ('+380', '+380 - Ukraine'),
    ('+381', '+381 - Serbia'),
    ('+382', '+382 - Montenegro'),
    ('+385', '+385 - Croatia'),
    ('+386', '+386 - Slovenia'),
    ('+387', '+387 - Bosnia and Herzegovina'),
    ('+389', '+389 - North Macedonia'),
    ('+420', '+420 - Czech Republic'),
    ('+421', '+421 - Slovakia'),
    ('+423', '+423 - Liechtenstein'),
    ('+500', '+500 - Falkland Islands'),
    ('+501', '+501 - Belize'),
    ('+502', '+502 - Guatemala'),
    ('+503', '+503 - El Salvador'),
    ('+504', '+504 - Honduras'),
    ('+505', '+505 - Nicaragua'),
    ('+506', '+506 - Costa Rica'),
    ('+507', '+507 - Panama'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+509', '+509 - Haiti'),
    ('+590', '+590 - Guadeloupe'),
    ('+591', '+591 - Bolivia'),
    ('+592', '+592 - Guyana'),
    ('+593', '+593 - Ecuador'),
    ('+594', '+594 - French Guiana'),
    ('+595', '+595 - Paraguay'),
    ('+596', '+596 - Martinique'),
    ('+597', '+597 - Suriname'),
    ('+598', '+598 - Uruguay'),
    ('+599', '+599 - Caribbean Netherlands'),
    ('+670', '+670 - East Timor'),
    ('+672', '+672 - Norfolk Island'),
    ('+673', '+673 - Brunei'),
    ('+674', '+674 - Nauru'),
    ('+675', '+675 - Papua New Guinea'),
    ('+676', '+676 - Tonga'),
    ('+677', '+677 - Solomon Islands'),
    ('+678', '+678 - Vanuatu'),
    ('+679', '+679 - Fiji'),
    ('+680', '+680 - Palau'),
    ('+681', '+681 - Wallis and Futuna'),
    ('+682', '+682 - Cook Islands'),
    ('+683', '+683 - Niue'),
    ('+685', '+685 - Samoa'),
    ('+686', '+686 - Kiribati'),
    ('+687', '+687 - New Caledonia'),
    ('+688', '+688 - Tuvalu'),
    ('+689', '+689 - French Polynesia'),
    ('+690', '+690 - Tokelau'),
    ('+691', '+691 - Micronesia'),
    ('+692', '+692 - Marshall Islands'),
    ('+850', '+850 - North Korea'),
    ('+852', '+852 - Hong Kong'),
    ('+853', '+853 - Macao'),
    ('+855', '+855 - Cambodia'),
    ('+856', '+856 - Laos'),
    ('+880', '+880 - Bangladesh'),
    ('+886', '+886 - Taiwan'),
    ('+960', '+960 - Maldives'),
    ('+961', '+961 - Lebanon'),
    ('+962', '+962 - Jordan'),
    ('+963', '+963 - Syria'),
    ('+964', '+964 - Iraq'),
    ('+965', '+965 - Kuwait'),
    ('+966', '+966 - Saudi Arabia'),
    ('+967', '+967 - Yemen'),
    ('+968', '+968 - Oman'),
    ('+970', '+970 - Palestine'),
    ('+971', '+971 - United Arab Emirates'),
    ('+972', '+972 - Israel'),
    ('+973', '+973 - Bahrain'),
    ('+974', '+974 - Qatar'),
    ('+975', '+975 - Bhutan'),
    ('+976', '+976 - Mongolia'),
    ('+977', '+977 - Nepal'),
    ('+992', '+992 - Tajikistan'),
    ('+993', '+993 - Turkmenistan'),
    ('+994', '+994 - Azerbaijan'),
    ('+995', '+995 - Georgia'),
    ('+996', '+996 - Kyrgyzstan'),
    ('+998', '+998 - Uzbekistan'),
)
# Add more country codes as needed
    print("1")
    if request.method == 'POST':
        print("2jbn")
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new ContactForm instance with the submitted data
            instance = form.save(commit=False)
            instance.save()
            print("2")
            # Handle successful submission (e.g., show a success message or redirect)
            return redirect('/')
        else: 
            print("3jnfw")
            # Handle invalid form data (e.g., show error messages)
            pass
    else:
        print("3")
        # Handle other HTTP methods (e.g., GET for displaying the form)
        form = ContactForm()
    context = {'form': form,
               'COUNTRY_CODES': COUNTRY_CODES
               }
    print("here dekh")
    return render(request, 'contact.html', context )

def download_resume(request):
    resume_path = 'portfolio_app/static/resume.pdf'
    if os.path.exists(resume_path):
        return FileResponse(open(resume_path, 'rb'), as_attachment=True)
    else:
        pass
    return redirect('/contact')

def resume_contact(request):
    COUNTRY_CODES = (
    ('+7', '+7 - Russia'),
    ('+20', '+20 - Egypt'),
    ('+27', '+27 - South Africa'),
    ('+30', '+30 - Greece'),
    ('+31', '+31 - Netherlands'),
    ('+32', '+32 - Belgium'),
    ('+33', '+33 - France'),
    ('+34', '+34 - Spain'),
    ('+36', '+36 - Hungary'),
    ('+39', '+39 - Italy'),
    ('+40', '+40 - Romania'),
    ('+41', '+41 - Switzerland'),
    ('+43', '+43 - Austria'),
    ('+44', '+44 - United Kingdom'),
    ('+45', '+45 - Denmark'),
    ('+46', '+46 - Sweden'),
    ('+47', '+47 - Norway'),
    ('+48', '+48 - Poland'),
    ('+49', '+49 - Germany'),
    ('+51', '+51 - Peru'),
    ('+52', '+52 - Mexico'),
    ('+53', '+53 - Cuba'),
    ('+54', '+54 - Argentina'),
    ('+55', '+55 - Brazil'),
    ('+56', '+56 - Chile'),
    ('+57', '+57 - Colombia'),
    ('+58', '+58 - Venezuela'),
    ('+60', '+60 - Malaysia'),
    ('+61', '+61 - Australia'),
    ('+62', '+62 - Indonesia'),
    ('+63', '+63 - Philippines'),
    ('+64', '+64 - New Zealand'),
    ('+65', '+65 - Singapore'),
    ('+66', '+66 - Thailand'),
    ('+81', '+81 - Japan'),
    ('+82', '+82 - South Korea'),
    ('+84', '+84 - Vietnam'),
    ('+86', '+86 - China'),
    ('+90', '+90 - Turkey'),
    ('+91', '+91 - India'),
    ('+92', '+92 - Pakistan'),
    ('+93', '+93 - Afghanistan'),
    ('+94', '+94 - Sri Lanka'),
    ('+95', '+95 - Myanmar'),
    ('+98', '+98 - Iran'),
    ('+212', '+212 - Morocco'),
    ('+213', '+213 - Algeria'),
    ('+216', '+216 - Tunisia'),
    ('+218', '+218 - Libya'),
    ('+220', '+220 - Gambia'),
    ('+221', '+221 - Senegal'),
    ('+222', '+222 - Mauritania'),
    ('+223', '+223 - Mali'),
    ('+224', '+224 - Guinea'),
    ('+225', '+225 - Ivory Coast'),
    ('+226', '+226 - Burkina Faso'),
    ('+227', '+227 - Niger'),
    ('+228', '+228 - Togo'),
    ('+229', '+229 - Benin'),
    ('+230', '+230 - Mauritius'),
    ('+231', '+231 - Liberia'),
    ('+232', '+232 - Sierra Leone'),
    ('+233', '+233 - Ghana'),
    ('+234', '+234 - Nigeria'),
    ('+235', '+235 - Chad'),
    ('+236', '+236 - Central African Republic'),
    ('+237', '+237 - Cameroon'),
    ('+238', '+238 - Cape Verde'),
    ('+239', '+239 - Sao Tome and Principe'),
    ('+240', '+240 - Equatorial Guinea'),
    ('+241', '+241 - Gabon'),
    ('+242', '+242 - Republic of the Congo'),
    ('+243', '+243 - Democratic Republic of the Congo'),
    ('+244', '+244 - Angola'),
    ('+245', '+245 - Guinea-Bissau'),
    ('+246', '+246 - British Indian Ocean Territory'),
    ('+247', '+247 - Ascension Island'),
    ('+248', '+248 - Seychelles'),
    ('+249', '+249 - Sudan'),
    ('+250', '+250 - Rwanda'),
    ('+251', '+251 - Ethiopia'),
    ('+252', '+252 - Somalia'),
    ('+253', '+253 - Djibouti'),
    ('+254', '+254 - Kenya'),
    ('+255', '+255 - Tanzania'),
    ('+256', '+256 - Uganda'),
    ('+257', '+257 - Burundi'),
    ('+258', '+258 - Mozambique'),
    ('+260', '+260 - Zambia'),
    ('+261', '+261 - Madagascar'),
    ('+262', '+262 - Reunion'),
    ('+263', '+263 - Zimbabwe'),
    ('+264', '+264 - Namibia'),
    ('+265', '+265 - Malawi'),
    ('+266', '+266 - Lesotho'),
    ('+267', '+267 - Botswana'),
    ('+268', '+268 - Swaziland'),
    ('+269', '+269 - Comoros'),
    ('+290', '+290 - Saint Helena'),
    ('+291', '+291 - Eritrea'),
    ('+297', '+297 - Aruba'),
    ('+298', '+298 - Faroe Islands'),
    ('+299', '+299 - Greenland'),
    ('+350', '+350 - Gibraltar'),
    ('+351', '+351 - Portugal'),
    ('+352', '+352 - Luxembourg'),
    ('+353', '+353 - Ireland'),
    ('+354', '+354 - Iceland'),
    ('+355', '+355 - Albania'),
    ('+356', '+356 - Malta'),
    ('+357', '+357 - Cyprus'),
    ('+358', '+358 - Finland'),
    ('+359', '+359 - Bulgaria'),
    ('+370', '+370 - Lithuania'),
    ('+371', '+371 - Latvia'),
    ('+372', '+372 - Estonia'),
    ('+373', '+373 - Moldova'),
    ('+374', '+374 - Armenia'),
    ('+375', '+375 - Belarus'),
    ('+376', '+376 - Andorra'),
    ('+377', '+377 - Monaco'),
    ('+378', '+378 - San Marino'),
    ('+380', '+380 - Ukraine'),
    ('+381', '+381 - Serbia'),
    ('+382', '+382 - Montenegro'),
    ('+385', '+385 - Croatia'),
    ('+386', '+386 - Slovenia'),
    ('+387', '+387 - Bosnia and Herzegovina'),
    ('+389', '+389 - North Macedonia'),
    ('+420', '+420 - Czech Republic'),
    ('+421', '+421 - Slovakia'),
    ('+423', '+423 - Liechtenstein'),
    ('+500', '+500 - Falkland Islands'),
    ('+501', '+501 - Belize'),
    ('+502', '+502 - Guatemala'),
    ('+503', '+503 - El Salvador'),
    ('+504', '+504 - Honduras'),
    ('+505', '+505 - Nicaragua'),
    ('+506', '+506 - Costa Rica'),
    ('+507', '+507 - Panama'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+509', '+509 - Haiti'),
    ('+590', '+590 - Guadeloupe'),
    ('+591', '+591 - Bolivia'),
    ('+592', '+592 - Guyana'),
    ('+593', '+593 - Ecuador'),
    ('+594', '+594 - French Guiana'),
    ('+595', '+595 - Paraguay'),
    ('+596', '+596 - Martinique'),
    ('+597', '+597 - Suriname'),
    ('+598', '+598 - Uruguay'),
    ('+599', '+599 - Caribbean Netherlands'),
    ('+670', '+670 - East Timor'),
    ('+672', '+672 - Norfolk Island'),
    ('+673', '+673 - Brunei'),
    ('+674', '+674 - Nauru'),
    ('+675', '+675 - Papua New Guinea'),
    ('+676', '+676 - Tonga'),
    ('+677', '+677 - Solomon Islands'),
    ('+678', '+678 - Vanuatu'),
    ('+679', '+679 - Fiji'),
    ('+680', '+680 - Palau'),
    ('+681', '+681 - Wallis and Futuna'),
    ('+682', '+682 - Cook Islands'),
    ('+683', '+683 - Niue'),
    ('+685', '+685 - Samoa'),
    ('+686', '+686 - Kiribati'),
    ('+687', '+687 - New Caledonia'),
    ('+688', '+688 - Tuvalu'),
    ('+689', '+689 - French Polynesia'),
    ('+690', '+690 - Tokelau'),
    ('+691', '+691 - Micronesia'),
    ('+692', '+692 - Marshall Islands'),
    ('+850', '+850 - North Korea'),
    ('+852', '+852 - Hong Kong'),
    ('+853', '+853 - Macao'),
    ('+855', '+855 - Cambodia'),
    ('+856', '+856 - Laos'),
    ('+880', '+880 - Bangladesh'),
    ('+886', '+886 - Taiwan'),
    ('+960', '+960 - Maldives'),
    ('+961', '+961 - Lebanon'),
    ('+962', '+962 - Jordan'),
    ('+963', '+963 - Syria'),
    ('+964', '+964 - Iraq'),
    ('+965', '+965 - Kuwait'),
    ('+966', '+966 - Saudi Arabia'),
    ('+967', '+967 - Yemen'),
    ('+968', '+968 - Oman'),
    ('+970', '+970 - Palestine'),
    ('+971', '+971 - United Arab Emirates'),
    ('+972', '+972 - Israel'),
    ('+973', '+973 - Bahrain'),
    ('+974', '+974 - Qatar'),
    ('+975', '+975 - Bhutan'),
    ('+976', '+976 - Mongolia'),
    ('+977', '+977 - Nepal'),
    ('+992', '+992 - Tajikistan'),
    ('+993', '+993 - Turkmenistan'),
    ('+994', '+994 - Azerbaijan'),
    ('+995', '+995 - Georgia'),
    ('+996', '+996 - Kyrgyzstan'),
    ('+998', '+998 - Uzbekistan'),
)
    context = {
               'COUNTRY_CODES': COUNTRY_CODES
               }
    return render(request, 'resume_contact.html', context)

def download_resume_adv(request):
    COUNTRY_CODES = (
    ('+7', '+7 - Russia'),
    ('+20', '+20 - Egypt'),
    ('+27', '+27 - South Africa'),
    ('+30', '+30 - Greece'),
    ('+31', '+31 - Netherlands'),
    ('+32', '+32 - Belgium'),
    ('+33', '+33 - France'),
    ('+34', '+34 - Spain'),
    ('+36', '+36 - Hungary'),
    ('+39', '+39 - Italy'),
    ('+40', '+40 - Romania'),
    ('+41', '+41 - Switzerland'),
    ('+43', '+43 - Austria'),
    ('+44', '+44 - United Kingdom'),
    ('+45', '+45 - Denmark'),
    ('+46', '+46 - Sweden'),
    ('+47', '+47 - Norway'),
    ('+48', '+48 - Poland'),
    ('+49', '+49 - Germany'),
    ('+51', '+51 - Peru'),
    ('+52', '+52 - Mexico'),
    ('+53', '+53 - Cuba'),
    ('+54', '+54 - Argentina'),
    ('+55', '+55 - Brazil'),
    ('+56', '+56 - Chile'),
    ('+57', '+57 - Colombia'),
    ('+58', '+58 - Venezuela'),
    ('+60', '+60 - Malaysia'),
    ('+61', '+61 - Australia'),
    ('+62', '+62 - Indonesia'),
    ('+63', '+63 - Philippines'),
    ('+64', '+64 - New Zealand'),
    ('+65', '+65 - Singapore'),
    ('+66', '+66 - Thailand'),
    ('+81', '+81 - Japan'),
    ('+82', '+82 - South Korea'),
    ('+84', '+84 - Vietnam'),
    ('+86', '+86 - China'),
    ('+90', '+90 - Turkey'),
    ('+91', '+91 - India'),
    ('+92', '+92 - Pakistan'),
    ('+93', '+93 - Afghanistan'),
    ('+94', '+94 - Sri Lanka'),
    ('+95', '+95 - Myanmar'),
    ('+98', '+98 - Iran'),
    ('+212', '+212 - Morocco'),
    ('+213', '+213 - Algeria'),
    ('+216', '+216 - Tunisia'),
    ('+218', '+218 - Libya'),
    ('+220', '+220 - Gambia'),
    ('+221', '+221 - Senegal'),
    ('+222', '+222 - Mauritania'),
    ('+223', '+223 - Mali'),
    ('+224', '+224 - Guinea'),
    ('+225', '+225 - Ivory Coast'),
    ('+226', '+226 - Burkina Faso'),
    ('+227', '+227 - Niger'),
    ('+228', '+228 - Togo'),
    ('+229', '+229 - Benin'),
    ('+230', '+230 - Mauritius'),
    ('+231', '+231 - Liberia'),
    ('+232', '+232 - Sierra Leone'),
    ('+233', '+233 - Ghana'),
    ('+234', '+234 - Nigeria'),
    ('+235', '+235 - Chad'),
    ('+236', '+236 - Central African Republic'),
    ('+237', '+237 - Cameroon'),
    ('+238', '+238 - Cape Verde'),
    ('+239', '+239 - Sao Tome and Principe'),
    ('+240', '+240 - Equatorial Guinea'),
    ('+241', '+241 - Gabon'),
    ('+242', '+242 - Republic of the Congo'),
    ('+243', '+243 - Democratic Republic of the Congo'),
    ('+244', '+244 - Angola'),
    ('+245', '+245 - Guinea-Bissau'),
    ('+246', '+246 - British Indian Ocean Territory'),
    ('+247', '+247 - Ascension Island'),
    ('+248', '+248 - Seychelles'),
    ('+249', '+249 - Sudan'),
    ('+250', '+250 - Rwanda'),
    ('+251', '+251 - Ethiopia'),
    ('+252', '+252 - Somalia'),
    ('+253', '+253 - Djibouti'),
    ('+254', '+254 - Kenya'),
    ('+255', '+255 - Tanzania'),
    ('+256', '+256 - Uganda'),
    ('+257', '+257 - Burundi'),
    ('+258', '+258 - Mozambique'),
    ('+260', '+260 - Zambia'),
    ('+261', '+261 - Madagascar'),
    ('+262', '+262 - Reunion'),
    ('+263', '+263 - Zimbabwe'),
    ('+264', '+264 - Namibia'),
    ('+265', '+265 - Malawi'),
    ('+266', '+266 - Lesotho'),
    ('+267', '+267 - Botswana'),
    ('+268', '+268 - Swaziland'),
    ('+269', '+269 - Comoros'),
    ('+290', '+290 - Saint Helena'),
    ('+291', '+291 - Eritrea'),
    ('+297', '+297 - Aruba'),
    ('+298', '+298 - Faroe Islands'),
    ('+299', '+299 - Greenland'),
    ('+350', '+350 - Gibraltar'),
    ('+351', '+351 - Portugal'),
    ('+352', '+352 - Luxembourg'),
    ('+353', '+353 - Ireland'),
    ('+354', '+354 - Iceland'),
    ('+355', '+355 - Albania'),
    ('+356', '+356 - Malta'),
    ('+357', '+357 - Cyprus'),
    ('+358', '+358 - Finland'),
    ('+359', '+359 - Bulgaria'),
    ('+370', '+370 - Lithuania'),
    ('+371', '+371 - Latvia'),
    ('+372', '+372 - Estonia'),
    ('+373', '+373 - Moldova'),
    ('+374', '+374 - Armenia'),
    ('+375', '+375 - Belarus'),
    ('+376', '+376 - Andorra'),
    ('+377', '+377 - Monaco'),
    ('+378', '+378 - San Marino'),
    ('+380', '+380 - Ukraine'),
    ('+381', '+381 - Serbia'),
    ('+382', '+382 - Montenegro'),
    ('+385', '+385 - Croatia'),
    ('+386', '+386 - Slovenia'),
    ('+387', '+387 - Bosnia and Herzegovina'),
    ('+389', '+389 - North Macedonia'),
    ('+420', '+420 - Czech Republic'),
    ('+421', '+421 - Slovakia'),
    ('+423', '+423 - Liechtenstein'),
    ('+500', '+500 - Falkland Islands'),
    ('+501', '+501 - Belize'),
    ('+502', '+502 - Guatemala'),
    ('+503', '+503 - El Salvador'),
    ('+504', '+504 - Honduras'),
    ('+505', '+505 - Nicaragua'),
    ('+506', '+506 - Costa Rica'),
    ('+507', '+507 - Panama'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+508', '+508 - Saint Pierre and Miquelon'),
    ('+509', '+509 - Haiti'),
    ('+590', '+590 - Guadeloupe'),
    ('+591', '+591 - Bolivia'),
    ('+592', '+592 - Guyana'),
    ('+593', '+593 - Ecuador'),
    ('+594', '+594 - French Guiana'),
    ('+595', '+595 - Paraguay'),
    ('+596', '+596 - Martinique'),
    ('+597', '+597 - Suriname'),
    ('+598', '+598 - Uruguay'),
    ('+599', '+599 - Caribbean Netherlands'),
    ('+670', '+670 - East Timor'),
    ('+672', '+672 - Norfolk Island'),
    ('+673', '+673 - Brunei'),
    ('+674', '+674 - Nauru'),
    ('+675', '+675 - Papua New Guinea'),
    ('+676', '+676 - Tonga'),
    ('+677', '+677 - Solomon Islands'),
    ('+678', '+678 - Vanuatu'),
    ('+679', '+679 - Fiji'),
    ('+680', '+680 - Palau'),
    ('+681', '+681 - Wallis and Futuna'),
    ('+682', '+682 - Cook Islands'),
    ('+683', '+683 - Niue'),
    ('+685', '+685 - Samoa'),
    ('+686', '+686 - Kiribati'),
    ('+687', '+687 - New Caledonia'),
    ('+688', '+688 - Tuvalu'),
    ('+689', '+689 - French Polynesia'),
    ('+690', '+690 - Tokelau'),
    ('+691', '+691 - Micronesia'),
    ('+692', '+692 - Marshall Islands'),
    ('+850', '+850 - North Korea'),
    ('+852', '+852 - Hong Kong'),
    ('+853', '+853 - Macao'),
    ('+855', '+855 - Cambodia'),
    ('+856', '+856 - Laos'),
    ('+880', '+880 - Bangladesh'),
    ('+886', '+886 - Taiwan'),
    ('+960', '+960 - Maldives'),
    ('+961', '+961 - Lebanon'),
    ('+962', '+962 - Jordan'),
    ('+963', '+963 - Syria'),
    ('+964', '+964 - Iraq'),
    ('+965', '+965 - Kuwait'),
    ('+966', '+966 - Saudi Arabia'),
    ('+967', '+967 - Yemen'),
    ('+968', '+968 - Oman'),
    ('+970', '+970 - Palestine'),
    ('+971', '+971 - United Arab Emirates'),
    ('+972', '+972 - Israel'),
    ('+973', '+973 - Bahrain'),
    ('+974', '+974 - Qatar'),
    ('+975', '+975 - Bhutan'),
    ('+976', '+976 - Mongolia'),
    ('+977', '+977 - Nepal'),
    ('+992', '+992 - Tajikistan'),
    ('+993', '+993 - Turkmenistan'),
    ('+994', '+994 - Azerbaijan'),
    ('+995', '+995 - Georgia'),
    ('+996', '+996 - Kyrgyzstan'),
    ('+998', '+998 - Uzbekistan'),
)
# Add more country codes as needed

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new ContactForm instance with the submitted data
            instance = form.save(commit=False)
            instance.save()

            resume_path = 'portfolio_app/static/resume.pdf'
            if os.path.exists(resume_path):
                return FileResponse(open(resume_path, 'rb'), as_attachment=True)

            #print ("redirect karne wale hai")
            # Handle successful submission (e.g., show a success message or redirect)
            #return redirect('/')
        else:
            # Handle invalid form data (e.g., show error messages)
            pass
    else:
        # Handle other HTTP methods (e.g., GET for displaying the form)
        form = ContactForm()
    context = {'form': form,
               'COUNTRY_CODES': COUNTRY_CODES
               }
    print(context,"here dekh")
    return render(request, 'resume_contact.html', context)

def bosch(request):
    return render(request, 'bosch.html')