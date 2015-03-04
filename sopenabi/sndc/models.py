#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# from stdimage import StdImageField
import datetime

# ===============================================================================
# Team
# ===============================================================================
class Team(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nom', help_text=u'votre prénom et nom')
    function = models.CharField(max_length=150, verbose_name='Fonction', help_text='votre fonction dans la société')
    image = models.ImageField(upload_to='upload/team', blank=True, verbose_name='Photo')
    description = models.TextField(help_text="Parlez un peu de votre Job")

    tweeter = models.CharField(max_length=50, blank=True, verbose_name='twitter', help_text='ex. https://twitter.com/mosisga')
    facebook = models.CharField(max_length=50, blank=True, help_text='ex. https://facebook.com/mosis.thiaw')
    pinterest = models.CharField(max_length=50, blank=True)
    google = models.CharField(max_length=50, verbose_name="Google plus", blank=True)

    slug = models.SlugField(verbose_name='url')

    is_active = models.BooleanField(default=True, verbose_name='actif', help_text='cocher pour activer le membre')

    class Meta:
        verbose_name = u"membre équipe"
        verbose_name_plural = u'membres équipe'

    def __unicode__(self):
        return self.name

#===============================================================================
# Nos partenaires
#===============================================================================
class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    image = models.ImageField(upload_to='upload/partners', blank=True)
    url = models.URLField(blank=True, verbose_name='site web', help_text='site web de votre partenaire')

    class Meta:
        verbose_name = 'partenaire'
        verbose_name_plural = 'Nos Partenaires'

    def __unicode__(self):
        return self.name

#===============================================================================
# Qui sommes Nous
#===============================================================================
class AboutUs(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titre')
    image = models.ImageField(upload_to='upload/apropos', blank=True, verbose_name='Image', help_text=u'Une photo de votre société')
    content = models.TextField(verbose_name='Description')

    slug = models.SlugField(verbose_name='url')

    class Meta:
        verbose_name = u"qui sommes nous?"
        verbose_name_plural = u"qui sommes nous?"

    def __unicode__(self):
        return self.title

#===============================================================================
# Nos Services
#===============================================================================
class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name='service', help_text='nom du service')
    image = models.ImageField(upload_to='upload/services', blank=True)
    content = models.TextField()

    slug = models.SlugField(verbose_name='url')

    class Meta:
        verbose_name_plural = 'nos services'

    def __unicode__(self):
        return self.name

#==================================================================
# CATEGORIE PRODUIT
#===================================================================

class ProductCategory (models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Categorie', help_text='ex.  andoid, E-commerce, responsive design, apple I0S, web app')

    class Meta:
        verbose_name = u'Type de Service'
        verbose_name_plural = u'Types de Services'

    # unicode
    def __unicode__(self):
        return self.name

#==========================================================================================
#   PRODUITS
#==========================================================================================
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Categorie', help_text=u'senlyrics.com')
    image = models.ImageField(upload_to='upload/products', blank=True)
    category = models.ForeignKey(ProductCategory, verbose_name='Catégorie')
    description = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date ajout")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Service'
        verbose_name_plural = 'Services'

    def __unicode__(self):
        return self.name

#==========================================================================================
#   A PROPOS DE NOUS
#==========================================================================================
class WelcomeMessage(models.Model):
    title = models.CharField(max_length=100, verbose_name='titre')
    image = models.ImageField(upload_to="upload/welcome", blank=True)
    content = models.TextField(verbose_name='Description')

    date_ajout = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=True, verbose_name='actif')

    class Meta:
        verbose_name = 'Message d\'accueil'
        verbose_name = 'Messages d\'accueil'

    def __unicode__(self):
        return self.title