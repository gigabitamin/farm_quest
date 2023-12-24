from django.contrib.auth.models import User
from django.db import models


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


class DailyHotel(models.Model):
    daily_hotel_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (daily_hotel_name, daily_hotel_address) found, that is not supported. The first column is selected.
    daily_hotel_address = models.CharField(max_length=255)
    daily_hotel_image_link = models.TextField(blank=True, null=True)
    daily_hotel_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_link = models.TextField(blank=True, null=True)
    daily_hotel_room_type = models.CharField(max_length=20, blank=True, null=True)
    daily_hotel_num = models.CharField(max_length=20, blank=True, null=True)
    daily_hotel_review_clear = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_review_location = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_review_service = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_review_facility = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_price = models.IntegerField(blank=True, null=True)
    daily_hotel_date = models.DateField(blank=True, null=True)
    daily_hotel_stay_date = models.DateField(blank=True, null=True)
    daily_hotel_discount_rate = models.IntegerField(blank=True, null=True)
    x_coordi = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    y_coordi = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_hotel'
        unique_together = (('daily_hotel_name', 'daily_hotel_address'),)


class DailyHotelMap(models.Model):
    daily_hotel_name = models.CharField(max_length=200)
    daily_hotel_address = models.CharField(max_length=255)
    daily_hotel_image_link = models.TextField(blank=True, null=True)
    daily_hotel_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_link = models.TextField(blank=True, null=True)
    daily_hotel_room_type = models.CharField(max_length=20, blank=True, null=True)
    daily_hotel_num = models.CharField(max_length=20, blank=True, null=True)
    daily_hotel_review_clear = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_review_location = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_review_service = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_review_facility = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_price = models.IntegerField(blank=True, null=True)
    daily_hotel_date = models.DateField(blank=True, null=True)
    daily_hotel_stay_date = models.DateField(blank=True, null=True)
    daily_hotel_discount_rate = models.IntegerField(blank=True, null=True)
    x_coordi = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    y_coordi = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    row_num = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'daily_hotel_map'

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


class Goodchoice(models.Model):
    acc_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (acc_name, acc_address) found, that is not supported. The first column is selected.
    acc_address = models.CharField(max_length=255)
    acc_image_link = models.TextField(blank=True, null=True)
    acc_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    acc_price = models.TextField(blank=True, null=True)
    acc_room_type = models.TextField(blank=True, null=True)
    acc_remain_room = models.TextField(blank=True, null=True)
    acc_link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodchoice'
        unique_together = (('acc_name', 'acc_address'),)


class NaverBlog(models.Model):
    naver_blog_id = models.CharField(primary_key=True, max_length=10)
    naver_blog_title = models.CharField(max_length=200)
    naver_blog_link = models.TextField(blank=True, null=True)
    naver_blog_image = models.TextField(blank=True, null=True)
    naver_blog_hashtag = models.TextField(blank=True, null=True)
    naver_bloger_name = models.CharField(max_length=100, blank=True, null=True)
    naver_blog_content_likeit_count = models.IntegerField(blank=True, null=True)
    naver_blog_content_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naver_blog'


class NearAttraction(models.Model):
    place = models.OneToOneField('Place', models.DO_NOTHING, primary_key=True)  # The composite primary key (place_id, visitkorea_id) found, that is not supported. The first column is selected.
    visitkorea = models.ForeignKey('Visitkorea', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'near_attraction'
        unique_together = (('place', 'visitkorea'),)


class NearRestaurant(models.Model):
    place = models.OneToOneField('Place', models.DO_NOTHING, primary_key=True)  # The composite primary key (place_id, restaurant_id) found, that is not supported. The first column is selected.
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'near_restaurant'
        unique_together = (('place', 'restaurant'),)


class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=200)
    place_address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'place'


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


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_link = models.TextField(blank=True, null=True)
    restaurant_image = models.TextField(blank=True, null=True)
    restaurant_hashtag = models.TextField(blank=True, null=True)
    restaurant_shop_name = models.TextField(blank=True, null=True)
    restaurant_content_likeit_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    restaurant_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    restaurant_review_num_count = models.IntegerField(blank=True, null=True)
    restaurant_avg_price = models.IntegerField(blank=True, null=True)
    restaurant_shop_category = models.TextField(blank=True, null=True)
    restaurant_map_x = models.IntegerField(blank=True, null=True)
    restaurant_map_y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Tripbtoz(models.Model):
    trip_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (trip_name, trip_address) found, that is not supported. The first column is selected.
    trip_address = models.CharField(max_length=255)
    trip_image_link = models.TextField(blank=True, null=True)
    trip_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    trip_link = models.TextField(blank=True, null=True)
    trip_date = models.DateField(blank=True, null=True)
    trip_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tripbtoz'
        unique_together = (('trip_name', 'trip_address'),)


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


class Visitkorea(models.Model):
    visitkorea_id = models.CharField(primary_key=True, max_length=20)
    visitkorea_title = models.CharField(max_length=255, blank=True, null=True)
    visitkorea_tel = models.CharField(max_length=50, blank=True, null=True)
    visitkorea_firstimage = models.CharField(max_length=255, blank=True, null=True)
    visitkorea_address = models.CharField(max_length=255, blank=True, null=True)
    visitkorea_mapx = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    visitkorea_mapy = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    visitkorea_mlevel = models.IntegerField(blank=True, null=True)
    visitkorea_overview = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitkorea'


class Yanolja(models.Model):
    yanolja_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (yanolja_name, yanolja_address) found, that is not supported. The first column is selected.
    yanolja_address = models.CharField(max_length=255)
    yanolja_image_link = models.TextField(blank=True, null=True)
    yanolja_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    yanolja_link = models.TextField(blank=True, null=True)
    yanolja_date = models.DateField(blank=True, null=True)
    yanolja_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yanolja'
        unique_together = (('yanolja_name', 'yanolja_address'),)


class Youtube(models.Model):
    youtube_id = models.CharField(primary_key=True, max_length=10)
    youtube_title = models.CharField(max_length=100, blank=True, null=True)
    youtube_link = models.CharField(max_length=100, blank=True, null=True)
    youtube_image = models.CharField(max_length=200, blank=True, null=True)
    youtube_name = models.CharField(max_length=50, blank=True, null=True)
    youtube_views = models.CharField(max_length=20, blank=True, null=True)
    youtube_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youtube'





class JejuPerformanceVenue(models.Model):
    연번 = models.IntegerField(blank=True, null=True)
    공연장명_개관일자_field = models.TextField(db_column='공연장명(개관일자)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    소재지 = models.TextField(blank=True, null=True)
    시설구분 = models.TextField(blank=True, null=True)
    비_고 = models.TextField(db_column='비 고', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    기준일자 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeju_performance_venue'


class JejuPlace(models.Model):
    장소_poi에_대한_id_구분_번호_체계 = models.IntegerField(db_column='장소 POI에 대한 ID 구분 번호 체계', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    위치좌표_x축값 = models.FloatField(db_column='위치좌표 X축값', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    위치좌표_y축값 = models.FloatField(db_column='위치좌표 Y축값', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    구분 = models.TextField(blank=True, null=True)
    장소명 = models.TextField(blank=True, null=True)
    소재지 = models.TextField(blank=True, null=True)
    데이터기준일자 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeju_place'


class AccomMap(models.Model):
    map_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    장소명 = models.TextField(blank=True, null=True)
    소재지 = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    위치좌표_x축값 = models.FloatField(db_column='위치좌표_X축값', blank=True, null=True)  # Field name made lowercase.
    위치좌표_y축값 = models.FloatField(db_column='위치좌표_Y축값', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accom_map'


