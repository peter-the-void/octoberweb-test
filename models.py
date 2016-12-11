from django.db import models


class EventManager(models.Manager):

    def current(self):
        from datetime import datetime
        from django.db.models import Q

        now = datetime.now().date()
        term = (Q(date__lte=now) & Q(date_end__gte=now)) | (Q(date__exact=now) & Q(date_end__isnull=True))

        return self.filter(term)

    def archive(self):
        from datetime import datetime
        from django.db.models import Q

        now = datetime.now().date()
        term = (Q(date_end__lt=now)) | ((Q(date__lt=now) & Q(date_end__isnull=True)))

        return self.filter(term)
        
        

class Event(models.Model):
    """
    Событие
    """
    title = models.CharField(
        verbose_name=u'Название',
        max_length=255, )
    announce = models.CharField(
        verbose_name=u'Анонс',
        max_length=255,
        blank=True, )
    date = models.DateField(
        verbose_name=u'Дата', )
    date_end = models.DateField(
        verbose_name=u'Дата до',
        null=True,
        blank=True, )

    objects = EventManager()

    class Meta:
        """
        Дополнительные настройки
        """
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

    def __unicode__(self):
        """
        Представление в виде unicode строки
        """
        return self.title

