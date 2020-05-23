Historie
========

Die Historie zeichnet sämtliche Änderungen (hinzufügen, bearbeiten, löschen) an den folgenden Models des Systems auf:

* django.contrib.auth.models.User (Systemnutzer)
* aemter.* (alle Models der App aemter)
* mitglieder.* (alle Models der App mitglieder)

Diese Einträge können von Administratoren des Systems auf der entsprechenden Seite unter ./admin/historie eingesehen werden.

Abhängigkeiten
--------------

django-simple-history
~~~~~~~~~~~~~~~~~~~~~

* Installation: ``pip install django-simple-history``
* Dokumentation: `https://django-simple-history.readthedocs.io/en/latest/ <https://django-simple-history.readthedocs.io/en/latest/>`_

django-simple-history ermöglicht das automatische Aufzeichnen des Zustands eines Models beim Ausführen einer Änderungsoperation (hinzufügen, bearbeiten, löschen).

Template Tags
-------------

.. automodule:: historie.templatetags.to_class_name
    :members:
    :undoc-members:

.. automodule:: historie.templatetags.get_associated_data
    :members:
    :undoc-members: