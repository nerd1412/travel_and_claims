from django.db import models
import datetime
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.conf import settings
from django.db.models import Max
from datetime import datetime, timedelta
from django.utils import timezone


# from django.core.validators import RegexValidator

class Basecostcenter(models.Model):
    BCCINTRID = models.AutoField(primary_key=True,unique=True)
    BCCDTLE = models.CharField(null=True,max_length=100,unique=True)
    BCCDESP = models.CharField(null=True,max_length=100)
    BCCEXPCSTCNTR = models.IntegerField(null=True)
    BCCCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_userid',null=True, on_delete=models.SET_NULL)
    BCCCREAON = models.DateTimeField(auto_now_add=True,null=True)
    BCCMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    BCCMODION = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "BCC"
    def __str__(self) -> str:

        return f'{self.BCCDESP}'

class UserroleModel(models.Model):
    URINTRID = models.AutoField(primary_key=True,unique=True)
    URROLTLE = models.CharField(null=True,max_length=100,unique=True,error_messages ={
                    "unique":"Role already exists."
                    })
    res_choices= (
    ('Yes','Yes'),
    ('No', 'No'),
    )
    URRESP = models.CharField(max_length=30,choices=res_choices,null=True)
    URROLDESP = models.CharField(null=True,max_length=100)
    URCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    URCREAON = models.DateTimeField(auto_now_add=True,null=True)
    URMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_role',null=True, on_delete=models.SET_NULL)
    URMODION = models.DateTimeField(auto_now=True,null=True)
    

    class Meta:
        db_table = "UR"
    def __str__(self) -> str:

        return f'{self.URROLTLE}'

class GradeModel(models.Model):
    GDINTRID = models.AutoField(primary_key=True,unique=True)
    GDGRD = models.CharField(null=True,max_length=100,unique=True,error_messages ={
                    "unique":"This Grade already exists."
                    })
    GDGRDDESP = models.CharField(null=True,max_length=100)
    GDCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    GDCREAON = models.DateTimeField(auto_now_add=True,null=True)
    GDMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_user',null=True, on_delete=models.SET_NULL)
    GDMODION = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "GD"
    def __str__(self) -> str:

        return f'{self.GDGRD}'

class WorkcenterModel(models.Model):
    WCINTRID = models.AutoField(primary_key=True,unique=True)
    WCWRKCNTR = models.CharField(null=True,max_length=100,unique=True,error_messages ={
                    "unique":"This Workcentre already exists."
                    })
    status_choices= (
    ('Active','Active'),
    ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=30,choices=status_choices,default='Active')
    WCWRKCNTRDESP = models.CharField(null=True,max_length=100)
    WCCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    WCCREAON = models.DateTimeField(auto_now_add=True,null=True)
    WCMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_user',null=True, on_delete=models.SET_NULL)
    WCMODION = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "WC"

    def __str__(self) -> str:

        return f'{self.WCWRKCNTR}'
    
class ProfileModel(models.Model):
    TPFCINTID = models.AutoField(primary_key=True,unique=True)
    TPFCLSEQ = models.IntegerField(null=True)
    TPFCNAME = models.CharField(null=True,max_length=100)
    TPFCMANID = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_pcre',null=True, on_delete=models.SET_NULL)
    TPFCCREBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_pcby',null=True, on_delete=models.SET_NULL)
    TPFCCREON = models.DateTimeField(auto_now_add=True,null=True)
    TPFCMODBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_pmod',null=True, on_delete=models.SET_NULL)
    TPFCMODON = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "TPFC"

    def __str__(self) -> str:

        return f'{self.TPFCNAME}'
    
class AssignProfileModel(models.Model):
    TPFAINTID = models.AutoField(primary_key=True,unique=True)
    TPFAEMPID = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_asi',null=True, on_delete=models.SET_NULL)
    TPFAPRNAME = models.ForeignKey(ProfileModel,null=True,related_name='%(class)s_pname', on_delete=models.SET_NULL)
    TPFAFROMD = models.DateField(null=True) 
    TPFATODATE = models.DateField(null=True) 
    TPFACREDBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_asic',null=True, on_delete=models.SET_NULL)
    TPFACREON = models.DateTimeField(auto_now_add=True,null=True)
    TPFAMODBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_assim',null=True, on_delete=models.SET_NULL)
    TPFAMODON = models.DateTimeField(auto_now=True,null=True)
    status= (
    ('Active','Active'),
    ('Disable', 'Disable'),
    )
    TPFASTATUS = models.CharField(max_length=30,choices=status,default='Active')
    
    class Meta:
        db_table = "TPFA"

    def __str__(self) -> str:
        return f'{self.TPFAPRNAME}'
    
    
    


class DepartmentModel(models.Model):
    DDINTRID = models.AutoField(primary_key=True,unique=True)
    DDDEPRT = models.CharField(null=True,max_length=100,unique=True,error_messages ={
                    "unique":"This Department already exists."
                    })
    DDDEPRTDESP = models.CharField(null=True,max_length=100)
    DDCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    DDCREAON = models.DateTimeField(auto_now_add=True,null=True)
    DDMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_dept',null=True, on_delete=models.SET_NULL)
    DDMODION = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "DD"

    def __str__(self) -> str:

        return f'{self.DDDEPRT}'

class MyUserManager(BaseUserManager):
    
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError('Please provide Email')
        email = self.normalize_email(email)
        user = self.model(email=email,password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password,**other_fields):
        user = self.create_user(email,password,**other_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=30,unique=True)
    user_name = models.CharField(max_length=150,unique=True)
    emp_id = models.CharField(max_length=150,unique=True)
    emp_type_choices = (
    ('Permanant','Permanant'),
    ('Contract','Contract'),  
    ('Project Trainee','Project Trainee'),   

    )
    emp_type = models.CharField(max_length=30, choices=emp_type_choices,null=True)
    role = models.ForeignKey(UserroleModel,null=True, on_delete=models.SET_NULL)
    cost_center = models.ForeignKey(Basecostcenter,null=True, on_delete=models.SET_NULL)
    grade = models.ForeignKey(GradeModel,null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(DepartmentModel,null=True, on_delete=models.SET_NULL)
    workcenter = models.ForeignKey(WorkcenterModel,null=True, on_delete=models.SET_NULL)
    status_choices= (
    ('Active','Active'),
    ('Inactive', 'Inactive'),
    )
    emp_status = models.CharField(max_length=30,choices=status_choices,default='Active')
    auth_choices = (
    ('Unlocked','Unlocked'),
    ('Locked', 'Locked'),
    )
    auth = models.CharField(max_length=30,choices=auth_choices,default='Unlocked')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobileno = models.BigIntegerField(null=True)
    address = models.CharField(max_length=300)
    dob = models.DateField(null=True)
    joining_date = models.DateField(null=True)
    efforts = models.IntegerField(null=True)
    profile = models.ForeignKey(AssignProfileModel,null=True,related_name='%(class)s_pname',on_delete=models.SET_NULL)
    objects = MyUserManager()
    emp_created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    emp_created_on = models.DateField(null=True,max_length=100,auto_now_add=True)
    emp_mod_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_user',null=True, on_delete=models.SET_NULL)
    emp_mod_on = models.DateField(null=True,max_length=100,auto_now=True)
    password_status = models.CharField(max_length=10,default='N')
    pass_date_changed = models.DateField(null=True)
    USERNAME_FIELD  = 'user_name'
    REQUIRED_FIELDS = ['first_name','email']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    # def set_password(self, *args, **kwargs):
    #     # Update the password_change_date field when the password is changed
    #     self.pass_date_changed = datetime.now().date()
    #     super().set_password(*args, **kwargs)
    #     self.save()
    
    def save(self, *args, **kwargs):
        if self.pk:
            # Check if the password field has been modified
            orig = MyUser.objects.get(pk=self.pk)
            if orig.password != self.password:
                self.pass_date_changed = timezone.now().date()
                self.password_status = 'Y'

        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.password_status




class Expenseheadmaster(models.Model):
    EXHINTRID = models.AutoField(primary_key=True,unique=True)
    EXHEXPHEDID = models.IntegerField()
    EXHHEDTLE = models.CharField(null=True,max_length=100)
    EXHHEDDESP = models.CharField(null=True,max_length=100)
    EXHCREABY = models.CharField(null=True,max_length=100)
    EXHCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    EXHMODIBY = models.CharField(null=True,max_length=100)
    EXHMODION = models.DateField(null=True,max_length=100,auto_now=True)

    class Meta:
        db_table = "EXH"
    def __str__(self) -> str:

        return f'{self.EXHHEDTLE}'





class Expensesubheadmaster(models.Model):
    EXSINTRID = models.AutoField(primary_key=True,unique=True)
    EXSEXPID = models.IntegerField(unique=True)
    EXSTLE = models.CharField(null=True,max_length=100)
    EXSDESP = models.CharField(null=True,max_length=100)
    EXSEXHID = models.ForeignKey(Expenseheadmaster,unique=True,null=True, on_delete=models.SET_NULL)
    EXSCREABY = models.CharField(null=True,max_length=100)
    EXSCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    EXSMODIBY = models.CharField(null=True,max_length=100)
    EXSMODION = models.DateField(null=True,max_length=100,auto_now=True)

    class Meta:
        db_table = "EXS"
    def __str__(self) -> str:

        return f'{self.EXSTLE}'



# class Expensesubheadmaster(models.Model):
#     EXSINTRID = models.AutoField(primary_key=True,unique=True)
#     EXSTLE = models.CharField(null=True,max_length=100,unique=True)
#     EXSDESP = models.CharField(null=True,max_length=100)
#     EXSEXHID = models.ForeignKey(Expenseheadmaster, null=True, on_delete=models.SET_NULL)
#     EXSCREABY = models.CharField(null=True,max_length=100)
#     EXSCREAON = models.DateField(null=True,max_length=100)
#     EXSMODIBY = models.CharField(null=True,max_length=100)
#     EXSMODION = models.DateField(null=True,max_length=100)

#     class Meta:
#         db_table = "EXS"
#     def __str__(self) -> str:

#         return f'{self.EXSTLE}'



class Projectmaster(models.Model):
    PMINTRID = models.AutoField(primary_key=True,unique=True)
    PMPROJID = models.IntegerField(unique=True)
    PMEXCSTCNTR = models.ForeignKey(Basecostcenter,null=True,on_delete=models.SET_NULL)
    type_choices = (
    ('Active','Active'),
    ('Inactive','Inactive'),   
    )
    PMSTUS = models.CharField(max_length=30, choices=type_choices,null=True)
    PMDESP = models.CharField(null=True,max_length=100)
    PMCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    PMCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    PMMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_user',null=True, on_delete=models.SET_NULL)
    PMMODION = models.DateField(null=True,max_length=100,auto_now=True)
    
    

    class Meta:
        db_table = "PM"
    def __str__(self) -> str:

        return f'{self.PMDESP}'




class Internalorder(models.Model):
    IODAUTOINTRID = models.AutoField(primary_key=True,unique=True)
    IODINTRID = models.IntegerField(null=True)
    IODEXPCSTCNTR = models.ForeignKey(Basecostcenter, null=True, on_delete=models.SET_NULL)
    type_choices = (
    ('Completed','Completed'),
    ('Pending','Pending'),   
    )
    IODSTUS = models.CharField(max_length=30, choices=type_choices)
    IODDESP = models.CharField(null=True,max_length=100)
    IODCREABY = models.CharField(max_length=100,null=True)
    IODCREAON = models.DateTimeField(auto_now_add=True,null=True)
    IODMODIBY = models.CharField(null=True,max_length=100)
    IODMODION = models.DateTimeField(auto_now=True,null=True)
    
   
    class Meta:
        db_table = "IOD"
    def __str__(self) -> str:

        return f'{self.IODDESP}'


class EmployeeMaster(models.Model):
    EMINTRID = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    EMEMPCOD = models.IntegerField()
    EMEMLID = models.CharField(null=True,max_length=100)
    EMGRD = models.ForeignKey(GradeModel,null=True, on_delete=models.SET_NULL)  
    EMDESG = models.CharField(null=True,max_length=100)
    EMMOBLNO = models.CharField(null=True,max_length=100)
    EMDEPRT = models.ForeignKey(DepartmentModel,null=True, on_delete=models.SET_NULL)
    EMWRKCNTR = models.ForeignKey(WorkcenterModel,null=True, on_delete=models.SET_NULL)
    EMCOMPNAM = models.CharField(null=True,max_length=100)
    EMCREABY = models.CharField(null=True,max_length=100)
    EMCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    EMMODIBY = models.CharField(null=True,max_length=100)
    EMMODION = models.DateField(null=True,max_length=100,auto_now=True)
    class Meta:
        db_table = "EM"




class Advancerequesthead(models.Model):
    ARHINTRID = models.AutoField(primary_key=True,unique=True)
    ARHEMPCOD = models.ForeignKey(EmployeeMaster, null=True, on_delete=models.SET_NULL)
    ARHMNT = models.CharField(null=True,max_length=100)
    type_choices = (
    ('Completed','Completed'),
    ('Pending','Pending'),   
    )
    ARHSTUS = models.CharField(null=True,max_length=100)
    ARHASIGD = models.CharField(null=True,max_length=100)
    ARHPYMTDTE = models.DateField(null=True,max_length=100)   
    ARHCREABY = models.CharField(max_length=100,null=True)
    ARHCREAON = models.DateTimeField(auto_now_add=True,null=True)
    ARHMODIBY = models.CharField(null=True,max_length=100)
    ARHMODION = models.DateTimeField(auto_now=True,null=True)
    
   
    class Meta:
        db_table = "ARH"
    def __str__(self) -> str:

        return f'{self.ARHINTRID}'


class Advancerequestsubheadmaster(models.Model):
    ARSMINTRID = models.AutoField(primary_key=True,unique=True)
    ARSMID = models.IntegerField(null=True,unique=True)
    ARSMTLE = models.CharField(null=True,max_length=100,unique=True)
    ARSMDESP = models.CharField(null=True,max_length=100)
    ARSMEXSEXHID = models.ForeignKey(Expenseheadmaster, null=True, on_delete=models.SET_NULL)
    ARSMCREABY = models.CharField(max_length=100,null=True)
    ARSMCREAON = models.DateTimeField(auto_now_add=True,null=True)
    ARSMMODIBY = models.CharField(null=True,max_length=100)
    ARSMMODION = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "ARSM"
    def __str__(self) -> str:

        return f'{self.ARSMTLE}'

def ids():
    no = DivmasterModel.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class DivmasterModel(models.Model):
    DIVINTID = models.IntegerField(('Code'), default=ids, unique=True, editable=False)
    DIVMID = models.CharField(primary_key=True, editable=False, max_length=30)
    DIVMTLE = models.CharField(null=True,max_length=100,unique=True)
    DIVMDESP = models.CharField(null=True,max_length=100)
    DIVMCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    DIVMCREAON = models.DateTimeField(auto_now_add=True,null=True)
    DIVMMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_div',null=True, on_delete=models.SET_NULL)
    DIVMMODION = models.DateTimeField(auto_now=True,null=True)

    objects = models.Manager()

    def save(self, **kwargs):
        if not self.DIVMID:
            self.DIVMID = "{}{:04d}".format('D', self.DIVINTID)
        super().save(*kwargs)

    class Meta:
        db_table = "DIVM"
    def __str__(self) -> str:
        return f'{self.DIVMID} - {self.DIVMTLE}'
        # return f'{self.DIVMTLE}'

def tids():
    no = TitledetailsModel.objects.count()
    if no == None:
        return 1
    else:
        return no + 1



class TitledetailsModel(models.Model):
    TITDINTRID = models.AutoField(primary_key=True,default=tids,unique=True)
    TITDID= models.CharField(null=True,max_length=100)
    TITDTLTLE = models.CharField(null=True,max_length=100,unique=True)
    TITDDESP = models.CharField(null=True,max_length=100)
    TITDURL = models.CharField(null=True,max_length=100)
    TITDCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    TITDCREAON = models.DateTimeField(auto_now_add=True,null=True)
    TITDMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tile',null=True, on_delete=models.SET_NULL)
    TITDMODION = models.DateTimeField(auto_now=True,null=True)

    def save(self, **kwargs):
        if not self.TITDID:
            self.TITDID = "{}{:04d}".format('T', self.TITDINTRID)
        super().save(*kwargs)
    
    class Meta:
        db_table = "TITD"
    def __str__(self) -> str:

        return f'{self.TITDTLTLE}'



# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         TravelModel.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.form.save()

class TravelStatus(models.Model):
    TSID = models.AutoField(primary_key=True, unique=True)
    TSCODE = models.CharField(null=True,max_length=100)
    TSDESC = models.CharField(null=True,max_length=100)
    TSCREBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_created',null=True, on_delete=models.SET_NULL)
    TSCREON = models.DateField(null=True,max_length=100,auto_now_add=True)
    TSMODBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_modified',null=True, on_delete=models.SET_NULL)
    TSMODON = models.DateField(null=True,max_length=100,auto_now=True)

    class Meta:
        db_table = "TS"

    def __str__(self) -> str:
        return f'{self.TSDESC}'
    
class BookingStatus(models.Model):
    status = models.CharField(max_length=50)
    status_createdby = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_screated',null=True, on_delete=models.SET_NULL)
    status_createdon = models.DateField(null=True,max_length=100,auto_now_add=True)
    status_modiby = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_smodified',null=True, on_delete=models.SET_NULL)
    status_modon = models.DateField(null=True,max_length=100,auto_now=True)

    def __str__(self):
        return self.status
    
class ProgressStatus(models.Model):
    status = models.CharField(max_length=100)
    pstatus_createdby = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_pcreated',null=True, on_delete=models.SET_NULL)
    pstatus_createdon = models.DateField(null=True,max_length=100,auto_now_add=True)
    pstatus_modiby = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_pmodified',null=True, on_delete=models.SET_NULL)
    pstatus_modon = models.DateField(null=True,max_length=100,auto_now=True)

    def __str__(self):
        return self.status


class Travelrequestheader(models.Model):
    THINTRID = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    type_choices = (
    ('Domestic','Domestic travel'),
    ('International', 'International travel'),
    # ('Car booking','Car booking'),
    )
    THTRVTYP = models.CharField(max_length=30, choices=type_choices,null=True)
    THTRPNAME = models.CharField(null=True,max_length=100)
    THPURPOSE = models.CharField(null=True,max_length=100)
    status_choices= (
    ('Applied','Applied'),
    ('Approved', 'Approved'),
    ('Decline','Decline'),
    ('Completed','Completed'),
    )
    THSTUSTYP = models.CharField(max_length=30,choices=status_choices,default='Applied',null=True)
    THLEVELC = models.IntegerField(null=True,default=0)
    THBOOKSTA = models.ForeignKey(BookingStatus, on_delete=models.SET_NULL, null=True)
    THTASTATUS = models.ForeignKey(TravelStatus, on_delete=models.SET_NULL, null=True)
    THPROJ = models.ForeignKey(Projectmaster,null=True, on_delete=models.SET_NULL)
    THRCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_created',null=True, on_delete=models.SET_NULL)
    THRCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    THRMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_modified',null=True, on_delete=models.SET_NULL)
    THRMODION = models.DateField(null=True,max_length=100,auto_now=True)
    THAPPROVEDBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_approved_by',null=True, on_delete=models.SET_NULL)

    
    class Meta:
        db_table = "THR"

    def __str__(self) -> str:
        return f'{self.THTRPNAME}'

    

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    message = models.CharField(max_length=255)
    travel_request = models.ForeignKey(Travelrequestheader, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            # If the notification is being updated, set the updated_at field
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
class ApproverStatus(models.Model):
    ACTION_CHOICES = [
        ('approve', 'Approve'),
        ('reject', 'Reject'),
    ]

    THAINTID = models.AutoField(primary_key=True, unique=True)
    travel_request = models.ForeignKey(Travelrequestheader, on_delete=models.CASCADE)
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TAS"




class Travelflightdetails(models.Model):  
    TFLDINTRID =  models.AutoField(primary_key=True, unique=True)
    TFLDTRPNAME = models.ForeignKey(Travelrequestheader, null=True, on_delete=models.SET_NULL)
    # TFLDPRJTRF = models.ForeignKey(Projectmaster,null=True, on_delete=models.SET_NULL)
    trip_choices= (
    ('One Way','One Way'),
    ('Round Trip', 'Round Trip'),
    ('Multi-city','Multi-city'),
    )
    TFLDTRPTYP = models.CharField(max_length=30,choices=trip_choices,default='One Way')
    TFLDPREF = models.CharField(max_length=100,null=True)
    TFLDPREFAIR = models.CharField(max_length=40,null=True)
    TFLDDTEOFTRV = models.DateField(null=True)    
    TFLDFRMPLC = models.CharField(max_length=100,null=True)    
    TFLDTOPLC = models.CharField(max_length=100)  
    TFLDPROGSTA = models.ForeignKey(ProgressStatus, on_delete=models.SET_NULL, null=True)
    TFLDREM = models.CharField(max_length=200,null=True)
    TFLDRETURN = models.DateField(null=True)
    TFLDCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tcreated',null=True, on_delete=models.SET_NULL)
    TFLDCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    TFLDMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tmodified',null=True, on_delete=models.SET_NULL)
    TFLDMODION = models.DateField(null=True,max_length=100,auto_now=True)
    

    class Meta:
        db_table = "TFLD"

class MulticityDetails(models.Model):
    MULFLTID = models.ForeignKey(Travelrequestheader,null=True, blank=True,on_delete=models.CASCADE)
    MULFLTFP = models.CharField(max_length=100)
    MULFLTTP = models.CharField(max_length=100)
    MULFLPRST = models.ForeignKey(ProgressStatus, on_delete=models.SET_NULL, null=True)
    MULFLTDT = models.DateField(null=True)
    MULFTCRB = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_mtcreated',null=True, on_delete=models.SET_NULL)
    MULFTCRO = models.DateField(null=True,max_length=100,auto_now_add=True)
    MULFTMDB = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_mtmodified',null=True, on_delete=models.SET_NULL)
    MULFTMDO = models.DateField(null=True,max_length=100,auto_now=True)

    class Meta:
        db_table = "MULTC"

class Travelvisadetails(models.Model):    
    TVDINTRID =  models.AutoField(primary_key=True, unique=True)
    TVDTRAVEL = models.ForeignKey(Travelrequestheader,null=True, on_delete=models.SET_NULL)
    TVDTRAVDTE = models.DateField(null=True)
    visa_type = (
        ('Business Type','Business Type'),
        ('Project Visa','Project Visa'),
        ('Conference Visa','Conference Visa'),
        ('Research Visa','Research Visa'),
    )
    TVDVISTYPE = models.CharField(max_length=30, choices=visa_type,null=True)
    TVDVISTGCOUN = models.CharField(null=True,max_length=100)
    TVDVSAFES = models.CharField(null=True,max_length=100)
    TVDREMK = models.CharField(null=True,max_length=100)
    TVDPROGSTA = models.ForeignKey(ProgressStatus, on_delete=models.SET_NULL, null=True)
    TVDCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tdvcreated',null=True, on_delete=models.SET_NULL)
    TVDCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    TVDMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tdmodified',null=True, on_delete=models.SET_NULL)
    TVDMODION = models.DateField(null=True,max_length=100,auto_now=True)

    class Meta:
        db_table = "TVD"

class Travelforexdetails(models.Model):  
    TFDINTRID =  models.AutoField(primary_key=True, unique=True)
    TFDTRVTID = models.ForeignKey(Travelrequestheader,null=True, on_delete=models.SET_NULL)
    TFDTRAVDTE = models.DateField(null=True)
    TFDAMNT = models.CharField(null=True,max_length=100)
    curr_type = (
        ('USD','US Dollar(USD)'),
        ('EUR','Euro(EUR)'),
        ('GBP','Pound Sterling(GBP)'),
    )
    TFDCURR = models.CharField(max_length=30, choices=curr_type,null=True)
    csh_type = (
        ('Card','Card'),
        ('Cash','Cash'),
    )
    TFDCSHTYPE = models.CharField(max_length=30, choices=csh_type,null=True)
    TFDREMARK = models.CharField(null=True,max_length=100)
    TFDPROGSTA = models.ForeignKey(ProgressStatus, on_delete=models.SET_NULL, null=True)
    TFODCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tfdcreated',null=True, on_delete=models.SET_NULL)
    TFODCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    TFODMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tfdmodified',null=True, on_delete=models.SET_NULL)
    TFODMODION = models.DateField(null=True,max_length=100,auto_now=True)    

    class Meta:
        db_table = "TFD"





class Travelhoteldetails(models.Model):     
    THDINTRID =  models.AutoField(primary_key=True, unique=True)
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    THDTRHINTRID = models.ForeignKey(Travelrequestheader, null=True, on_delete=models.SET_NULL)
    THDPREFHOTL = models.CharField(null=True,max_length=100)    
    THDCHKINDTE = models.DateField(null=True)    
    THDCHKOTDTE = models.DateField(null=True)    
    THDSECT = models.CharField(null=True,max_length=100) 
    THDCITY = models.CharField(null=True,max_length=100)  
    THDREMK = models.CharField(null=True,max_length=200)
    # THDROMTYP = models.CharField(null=True,max_length=100)  
    hotel_choices= (
    ('Single','Single'),
    ('Double', 'Double'),
    ('Villa','Villa'),
    )  
    THDHTYPE = models.CharField(max_length=30, choices=hotel_choices,blank=True)
    THDPROGSTA = models.ForeignKey(ProgressStatus, on_delete=models.SET_NULL, null=True)
    THDCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tcreated',null=True, on_delete=models.SET_NULL)
    THDCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    THDMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tmodified',null=True, on_delete=models.SET_NULL)
    THDMODION = models.DateField(null=True,max_length=100,auto_now=True)

    
    class Meta:
        db_table = "THD"


class Non_Emp_Details(models.Model):    
    TNEDINTRID =  models.AutoField(primary_key=True, unique=True)
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    TNEDTMINTID = models.ForeignKey(Travelrequestheader, null=True, on_delete=models.SET_NULL)
    TNEDNONEMPNAM = models.CharField(null=True,max_length=100)
    TNEDPPRSOFVIS = models.CharField(null=True,max_length=100)
    TNEDMOBLNO = models.CharField(null=True,max_length=100)
    TNEDEML = models.EmailField(null=True,max_length=30)
    TNEDCREABY = models.CharField(null=True,max_length=100)
    TNEDCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    TNEDMODIBY = models.CharField(null=True,max_length=100)
    TNEDMODION = models.DateField(null=True,max_length=100,auto_now=True) 
    class Meta:
        db_table = "TNED"


 
class Travelcarbookingdetails(models.Model):  
    TCBDINTID =  models.AutoField(primary_key=True, unique=True)
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    TCBDTHID = models.ForeignKey(Travelrequestheader, null=True, on_delete=models.SET_NULL) 
    type_choices= (
    ('Micro','Micro'),
    ('Sedan', 'Sedan'),
    ('SUV','SUV'),
    )  
    TCBDCTYP = models.CharField(max_length=30, choices=type_choices,blank=True)
    TCBDFRLOC = models.CharField(null=True,max_length=100)
    TCBDTOLOC = models.CharField(null=True,max_length=100)
    TCBDPROGSTA = models.ForeignKey(ProgressStatus, on_delete=models.SET_NULL, null=True)
    TCBDREM = models.CharField(max_length=200,null=True) 
    TCBDPIKU = models.DateField(null=True)
    TCBDDROP = models.DateField(null=True)
    TCBDCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tcreated',null=True, on_delete=models.SET_NULL)
    TCBDCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    TCBDMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tmodified',null=True, on_delete=models.SET_NULL)
    TCBDMODION = models.DateField(null=True,max_length=100,auto_now=True)

      
    
    class Meta:
        db_table = "TCBD"


class MultiLeg(models.Model):  
    MCLINTID =  models.AutoField(primary_key=True, unique=True)
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    MCLFLID = models.ForeignKey(Travelflightdetails, null=True, on_delete=models.SET_NULL)
    MCLDEPF = models.CharField(null=True,max_length=100)
    MCLARVAT = models.CharField(null=True,max_length=100)
    MCLDEPD = models.DateField(null=True)
    MCLCREBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tcreated',null=True, on_delete=models.SET_NULL)
    MCLCREON = models.DateField(null=True,max_length=100,auto_now_add=True)
    MCLMODBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tmodified',null=True, on_delete=models.SET_NULL)
    MCLMODON = models.DateField(null=True,max_length=100,auto_now=True)

    class Meta:
        db_table = "MCL"




class Expenseclaimhead(models.Model):
    ECHINTRID = models.AutoField(primary_key=True, unique=True)
    ECHEMPCOD = models.ForeignKey(EmployeeMaster, null=True, on_delete=models.SET_NULL)
    ECHEHEDID = models.IntegerField(null=True)
    ECHCLMMNT = models.CharField(null=True,max_length=100)
    status_choices= (
    ('Applied','Applied'),
    ('Approved', 'Approved'),
    ('Decline','Decline'),
    ('Completed','Completed'),
    )
    ECHCLMSTUS = models.CharField(null=True,max_length=100)
    ECHCLMHEDASIGD = models.CharField(null=True,max_length=100)
    ECHCLMHEDPYMTDTE = models.DateField(null=True,max_length=100)   
    ECHCREABY = models.CharField(null=True,max_length=100)
    ECHCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    ECHMODIBY = models.CharField(null=True,max_length=100)
    ECHMODION = models.DateField(null=True,max_length=100,auto_now=True)  
      
    class Meta:
        db_table = "ECH"


class Workbreakdownstructure(models.Model):
    WBSINTRID = models.AutoField(primary_key=True,unique=True)
    WBSELMT = models.CharField(null=True,max_length=100)
    WBSDESP = models.CharField(null=True,max_length=100)
    WBSPMINTRID = models.ForeignKey(Projectmaster, null=True, on_delete=models.SET_NULL)
    type_choices = (
    ('Completed','Completed'),
    ('Pending','Pending'),   
    )
    WBSSTUS = models.CharField(max_length=30, choices=type_choices)
    WBSCREABY = models.CharField(max_length=100,null=True)
    WBSCREAON = models.DateTimeField(auto_now_add=True,null=True)
    WBSMODIBY = models.CharField(null=True,max_length=100)
    WBSMODION = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "WBS"
    def __str__(self) -> str:

        return f'{self.WBSELMT}'







class Pettycashheader(models.Model):
    PCHINTRID = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    PCHEMINTRID = models.ForeignKey(EmployeeMaster, null=True, on_delete=models.SET_NULL)
    PCHCLMMNT = models.CharField(null=True,max_length=100)    
    PCHCLMSTUS = models.CharField(null=True, max_length=100)
    PCHCLMHEDASIGD = models.CharField(null=True, max_length=100)
    PCHHEDPYMTDTE = models.DateField(null=True, max_length=100)
    PCHVCHRNO = models.CharField(null=True, max_length=100)
    PCHVCHRDTE = models.CharField(null=True, max_length=100)
    PCHCREABY = models.CharField(null=True,max_length=100)
    PCHCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)
    PCHMODIBY = models.CharField(null=True,max_length=100)
    PCHMODION = models.DateField(null=True,max_length=100,auto_now=True)   
    
    
    class Meta:
        db_table = "PCH"



class Pettycashdetails(models.Model):
    PCDINTRID = models.AutoField(primary_key=True, unique=True)
    PCDPCHINTRID = models.ForeignKey(Pettycashheader, null=True, on_delete=models.SET_NULL)
    PCDTYP = models.CharField(null=True, max_length=100)
    PCDHEDID = models.ForeignKey(Expenseclaimhead, null=True, on_delete=models.SET_NULL)
    PCDSBHDID = models.ForeignKey(Expensesubheadmaster, null=True, on_delete=models.SET_NULL)
    PCDPROJID = models.ForeignKey(Projectmaster, null=True, on_delete=models.SET_NULL)
    PCDWRKBRKDWNSTRCTRID = models.ForeignKey(Workbreakdownstructure, null=True, on_delete=models.SET_NULL)
    PCDINTRLORDRID = models.ForeignKey(Internalorder, null=True, on_delete=models.SET_NULL)
    PCDDTEOFCLM = models.DateField(null=True,max_length=100)   
    PCDWRKCNTR = models.ForeignKey(WorkcenterModel, null=True, on_delete=models.SET_NULL)
    PCDBSECSTCNTR = models.ForeignKey(Basecostcenter, null=True, on_delete=models.SET_NULL)
    PCDEXPCSTCNTR = models.ForeignKey(Basecostcenter,related_name='%(class)s_expensecostcenter', null=True, on_delete=models.SET_NULL)
    PCDDESP = models.CharField(null=True,max_length=100)
    PCDAMT = models.CharField(null=True,max_length=100)
    PCDAPPVDAMT = models.CharField(null=True,max_length=100)
    PCDCREABY = models.CharField(null=True,max_length=100)
    PCDCREAON = models.DateField(null=True,max_length=100,auto_now_add=True)   
    PCDMODIBY = models.CharField(null=True,max_length=100)
    PCDMODION = models.DateField(null=True,max_length=100,auto_now=True)   
    
    class Meta:
        db_table = "PCD"




class Expenseclaimdetails(models.Model):
    ECDINTRID = models.AutoField(primary_key=True, unique=True)
    ECDECHINTRID = models.ForeignKey(Expenseclaimhead, related_name='%(class)s_epenseclaimhead',null=True, on_delete=models.SET_NULL)
    ECDTYP = models.CharField(null=True, max_length=100)
    ECDECHEHEDID = models.ForeignKey(Expenseclaimhead, null=True, on_delete=models.SET_NULL)
    ECDEXSSBHDID = models.ForeignKey(Expensesubheadmaster, null=True, on_delete=models.SET_NULL)
    ECDPMPROJID = models.ForeignKey(Projectmaster, null=True, on_delete=models.SET_NULL)
    ECDWRKBRKDWNSTRCTRID = models.ForeignKey(Workbreakdownstructure, null=True, on_delete=models.SET_NULL)
    ECDINTRLORDRID = models.ForeignKey(Internalorder, null=True, on_delete=models.SET_NULL)
    ECDDTEOFCLM = models.DateField(null=True,max_length=100)   
    ECDWRKCNTR = models.ForeignKey(WorkcenterModel, null=True, on_delete=models.SET_NULL)
    ECDBSECSTCNTR = models.ForeignKey(Basecostcenter, null=True, on_delete=models.SET_NULL)
    ECDEXPCSTCNTR = models.ForeignKey(Basecostcenter,related_name='%(class)s_expense_cost_center', null=True, on_delete=models.SET_NULL)
    ECDDESP = models.CharField(null=True,max_length=100)
    ECDAMT = models.CharField(null=True,max_length=100)
    ECDAPPVDAMT = models.CharField(null=True,max_length=100)
    ECDMODIBY = models.CharField(null=True,max_length=100)
    ECDMODION = models.DateField(null=True,max_length=100,auto_now_add=True)   
    ECDMODIBY = models.CharField(null=True,max_length=100)
    ECDMODION = models.DateField(null=True,max_length=100,auto_now=True)   
    
    class Meta:
        db_table = "ECD"




class AdvanceRequestdetails(models.Model):
    ARDINTRID = models.AutoField(primary_key=True, unique=True)
    ARDECDINTRID = models.ForeignKey(Basecostcenter,related_name='%(class)s_base_cst_cntr', null=True, on_delete=models.SET_NULL)
    ARDTYP = models.CharField(null=True, max_length=100)
    ARDECDHEDID = models.ForeignKey(Expenseclaimhead, null=True, on_delete=models.SET_NULL)
    ARDECDSBHDID = models.ForeignKey(Expensesubheadmaster, null=True, on_delete=models.SET_NULL)
    AARDECDPROJID = models.ForeignKey(Projectmaster, null=True, on_delete=models.SET_NULL)
    ARDECDWRKBRKDWNSTRCTRID = models.ForeignKey(Workbreakdownstructure, null=True, on_delete=models.SET_NULL)
    ARDECDINTRLORDRID = models.ForeignKey(Internalorder, null=True, on_delete=models.SET_NULL)
    ARDDTEOFCLM = models.DateField(null=True,max_length=100)   
    ARDWRKCNTR = models.ForeignKey(WorkcenterModel, null=True, on_delete=models.SET_NULL)
    ARDBSECSTCNTR = models.ForeignKey(Basecostcenter, null=True, on_delete=models.SET_NULL)
    ARDDESP = models.CharField(null=True,max_length=100)
    ARDAMT = models.CharField(null=True,max_length=100)
    ARDAPPVDAMT = models.CharField(null=True,max_length=100)
    ARDCREABY = models.CharField(max_length=100,null=True)
    ARDCREAON = models.DateTimeField(auto_now_add=True,null=True)
    ARDMODIBY = models.CharField(null=True,max_length=100)
    ARDMODION = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "ARD"



    
class Tileautherizationdetails(models.Model):
    TADINTRID = models.AutoField(primary_key=True, unique=True)
    TADTITDID = models.ForeignKey(TitledetailsModel , null=True, on_delete=models.SET_NULL)
    TADURROLTLE = models.ForeignKey(UserroleModel, null=True, on_delete=models.SET_NULL)
    TADDIVMINTRID = models.ForeignKey(DivmasterModel, null=True, on_delete=models.SET_NULL)
    TADSEQ = models.IntegerField(null=True)
    TADCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    TADCREAON = models.DateTimeField(auto_now_add=True,null=True)
    TADMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_tile_auth',null=True, on_delete=models.SET_NULL)
    TADMODION = models.DateTimeField(auto_now=True,null=True)

    def save(self, *args, **kwargs):
        if self.TADSEQ is None:
            # Get the maximum TADSEQ value and increment it by 1
            max_seq = Tileautherizationdetails.objects.aggregate(models.Max('TADSEQ'))['TADSEQ__max']
            self.TADSEQ = (max_seq or 0) + 1

        super().save(*args, **kwargs)
    

    class Meta:
            db_table = "TAD"



class Divassignmentuser(models.Model):
    DIVASSUINTRID = models.AutoField(primary_key=True, unique=True)
    DIVASSUURROLTLE = models.ForeignKey(UserroleModel, null=True, on_delete=models.SET_NULL)
    DIVASSUDIVMID = models.ForeignKey(DivmasterModel, null=True, on_delete=models.SET_NULL)
    DIVASSUSEQ = models.IntegerField(null=True)
    DIVASSUCREABY = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    DIVASSUCREAON = models.DateTimeField(auto_now_add=True,null=True)
    DIVASSUMODIBY = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_div_ass',null=True, on_delete=models.SET_NULL)
    DIVASSUMODION = models.DateTimeField(auto_now=True,null=True)
    
    def save(self, *args, **kwargs):
        if self.DIVASSUSEQ is None:
            # Get the maximum TADSEQ value and increment it by 1
            max_seq = Divassignmentuser.objects.aggregate(models.Max('DIVASSUSEQ'))['DIVASSUSEQ__max']
            self.DIVASSUSEQ = (max_seq or 0) + 1

        super().save(*args, **kwargs)

    class Meta:
            db_table = "DIVASSU"
