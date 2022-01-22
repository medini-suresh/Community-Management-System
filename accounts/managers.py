from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, phone, aadhar, last_name=None, occupation=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            phone=phone,
            aadhar=aadhar,
            last_name=last_name,
            occupation=occupation
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name='admin',
            phone=2000000000,
            aadhar=323456789012,
        )
        user.is_superuser=True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user