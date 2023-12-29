from django.db import models
from django.contrib.auth.models import AbstractUser


# DRF
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    subjects = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile/', default='default.png')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




#


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersAppUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PreferredAccommodationType(models.Model):
    preferred_accommodation_type_no = models.CharField(primary_key=True, max_length=45, default=1)
    preferred_accommodation_type = models.CharField(max_length=45)


    def __str__(self):
        return self.preferred_accommodation_type

    class Meta:
        managed = False
        db_table = 'preferred_accommodation_type'


class PreferredRegion(models.Model):
    preferred_region_no = models.CharField(primary_key=True, max_length=45, default=1)
    preferred_region = models.CharField(max_length=45)

    def __str__(self):
        return self.preferred_region
    
    class Meta:
        managed = False
        db_table = 'preferred_region'
        

class PreferredTourThemeType(models.Model):
    preferred_tour_theme_type_no = models.CharField(primary_key=True, max_length=45, default=1)
    preferred_tour_theme_type = models.CharField(max_length=45)

    def __str__(self):
        return self.preferred_tour_theme_type

    class Meta:
        managed = False
        db_table = 'preferred_tour_theme_type'



class User(AbstractUser):
    # pass # 기본 auth_user 테이블과 동일
    
    # 새로운 필드 추가 
    
    # 장고
    # user_name = models.CharField(max_length=30)
    # user_phone = models.CharField(max_length=20)
    # user_address = models.CharField(max_length=200)
    # preferred_region_no = models.ForeignKey(PreferredRegion, models.DO_NOTHING, db_column='preferred_region_no')
    # preferred_accommodation_type_no = models.ForeignKey(PreferredAccommodationType, models.DO_NOTHING, db_column='preferred_accommodation_type_no')
    # preferred_tour_theme_type_no = models.ForeignKey(PreferredTourThemeType, models.DO_NOTHING, db_column='preferred_tour_theme_type_no')
    
    # 리액트
    # email = models.EmailField(unique=True)
     email = models.CharField(max_length=254, unique=True)  





class UsersAppUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    user_name = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=200)
    preferred_region_no = models.ForeignKey(PreferredRegion, models.DO_NOTHING, db_column='preferred_region_no', blank=True, null=True)
    preferred_accommodation_type_no = models.ForeignKey(PreferredAccommodationType, models.DO_NOTHING, db_column='preferred_accommodation_type_no', blank=True, null=True)
    preferred_tour_theme_type_no = models.ForeignKey(PreferredTourThemeType, models.DO_NOTHING, db_column='preferred_tour_theme_type_no', blank=True, null=True)
    profile_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_app_user'


class UsersAppUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersAppUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_app_user_groups'
        unique_together = (('user', 'group'),)


class UsersAppUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersAppUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_app_user_user_permissions'
        unique_together = (('user', 'permission'),)