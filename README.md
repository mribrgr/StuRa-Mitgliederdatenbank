# StuRa-Mitgliederdatenbank
<!-- Badges -->
![Test_Linux](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/workflows/Test_Linux/badge.svg)
![flake8](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/workflows/flake8/badge.svg)
![doc_sphinx](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/workflows/doc_sphinx/badge.svg)

## Dokumentation

[Website der Dokumentation](https://mribrgr.github.io/StuRa-Mitgliederdatenbank/)

- [Anforderungsanalyse](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/tree/master/docs/anforderung)
- [Projektbericht](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/tree/master/docs/projektbericht)
- [Dokumentation](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/tree/master/docs/sphinx)


## Nützliches

[Aufgabenstellung](docs\anforderung\orga\task.adoc)

[Abgabeformat](https://github.com/htwdd-se/VorlageBelegabgabe)

[a successful git branching model](https://nvie.com/posts/a-successful-git-branching-model)

[OpenUP Dokumentation](https://www2.htw-dresden.de/~anke/openup/index.htm)

[Derzeitige Mitgliederdatenbank (man muss angemeldet sein)](https://stura.htw-dresden.de/stura/ref/verwaltung/mitglieder/mitgliederdatenbank)

## Infos zum Datenmodell
+ [Organigramm](https://stura.htw-dresden.de/stura/ref/personal/posten/plenum/stellenplan-organigramm-2019) - Enthält (eigentlich alle) Infos zu den abzubildenden Referaten und Ämtern
+ [Diskussion Mitgliederdatenbank](https://wiki.stura.htw-dresden.de/index.php/Diskussion:Mitgliederdatenbank) - Enthält einen möglichen, bereits vom StuRa ausgearbeiteten Ansatz zur Strukturierung der Daten

## Latest Test Coverage Report

```console
Name                                                      Stmts   Miss  Cover
-----------------------------------------------------------------------------
aemter/__init__.py                                            0      0   100%
aemter/admin.py                                              17      0   100%
aemter/apps.py                                                3      0   100%
aemter/models.py                                             56      5    91%
aemter/tests/__init__.py                                      0      0   100%
aemter/tests/test_apps.py                                     7      0   100%
aemter/tests/test_models.py                                  17      0   100%
aemter/tests/test_urls.py                                     8      0   100%
aemter/tests/test_views.py                                   24      0   100%
aemter/urls.py                                                7      0   100%
aemter/views.py                                              21      0   100%
bin/__init__.py                                               0      0   100%
bin/asgi.py                                                   4      4     0%
bin/settings.py                                              19      0   100%
bin/urls.py                                                   3      0   100%
bin/wsgi.py                                                   4      4     0%
checklisten/__init__.py                                       0      0   100%
checklisten/admin.py                                          1      0   100%
checklisten/apps.py                                           3      0   100%
checklisten/models.py                                        41      4    90%
checklisten/templatetags/t_checklisten/__init__.py            0      0   100%
checklisten/templatetags/t_checklisten/get_perms.py           7      2    71%
checklisten/templatetags/t_checklisten/get_tasks.py           7      2    71%
checklisten/tests/__init__.py                                 0      0   100%
checklisten/tests/test_apps.py                                7      0   100%
checklisten/urls.py                                           7      0   100%
checklisten/views.py                                         92     81    12%
historie/__init__.py                                          0      0   100%
historie/apps.py                                              3      0   100%
historie/models.py                                            4      0   100%
historie/templatetags/t_historie/__init__.py                  0      0   100%
historie/templatetags/t_historie/get_associated_data.py      31     24    23%
historie/templatetags/t_historie/to_class_name.py             5      0   100%
historie/tests/__init__.py                                    0      0   100%
historie/tests/test_apps.py                                   7      0   100%
historie/tests/test_urls.py                                   8      0   100%
historie/tests/test_views.py                                 22      0   100%
historie/urls.py                                              4      0   100%
historie/views.py                                           123     66    46%
login/__init__.py                                             0      0   100%
login/apps.py                                                 3      0   100%
login/tests/__init__.py                                       0      0   100%
login/tests/test_apps.py                                      7      0   100%
login/tests/test_urls.py                                     11      0   100%
login/tests/test_views.py                                    35      0   100%
login/urls.py                                                 4      0   100%
login/views.py                                               27      2    93%
mitglieder/__init__.py                                        0      0   100%
mitglieder/admin.py                                           2      0   100%
mitglieder/apps.py                                            3      0   100%
mitglieder/models.py                                         51      1    98%
mitglieder/tests/__init__.py                                  0      0   100%
mitglieder/tests/test_apps.py                                 7      0   100%
mitglieder/tests/test_models.py                              17      0   100%
mitglieder/tests/test_urls.py                                47      0   100%
mitglieder/tests/test_views.py                               51      0   100%
mitglieder/urls.py                                            4      0   100%
mitglieder/views.py                                         205     66    68%
-----------------------------------------------------------------------------
TOTAL                                                      1036    261    75%
```
