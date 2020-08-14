# StuRa-Mitgliederdatenbank
<!-- Badges -->
![Test_Linux](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/workflows/Test_Linux/badge.svg)
![build_documentation](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/workflows/build_documentation/badge.svg)
![flake8](https://github.com/mribrgr/StuRa-Mitgliederdatenbank/workflows/flake8/badge.svg)

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
aemter/__init__.py                                            1      0   100%
aemter/admin.py                                              26      0   100%
aemter/apps.py                                                6      0   100%
aemter/models.py                                             59      4    93%
aemter/signals/handlers.py                                   17      3    82%
aemter/tests/__init__.py                                      0      0   100%
aemter/tests/test_apps.py                                     7      0   100%
aemter/tests/test_models.py                                  17      0   100%
aemter/tests/test_urls.py                                     8      0   100%
aemter/tests/test_views.py                                   24      0   100%
aemter/urls.py                                                7      0   100%
aemter/views.py                                              23      0   100%
bin/__init__.py                                               0      0   100%
bin/asgi.py                                                   4      4     0%
bin/management/__init__.py                                    0      0   100%
bin/management/commands/__init__.py                           0      0   100%
bin/management/commands/delete_old_historie.py               37     37     0%
bin/settings.py                                              19      0   100%
bin/urls.py                                                   3      0   100%
bin/wsgi.py                                                   4      4     0%
checklisten/__init__.py                                       0      0   100%
checklisten/admin.py                                          4      0   100%
checklisten/apps.py                                           3      0   100%
checklisten/models.py                                        41      0   100%
checklisten/templatetags/t_checklisten/__init__.py            0      0   100%
checklisten/templatetags/t_checklisten/get_perms.py           7      2    71%
checklisten/templatetags/t_checklisten/get_tasks.py           7      2    71%
checklisten/tests/__init__.py                                 0      0   100%
checklisten/tests/test_apps.py                                7      0   100%
checklisten/tests/test_models.py                             30      0   100%
checklisten/tests/test_urls.py                               20      0   100%
checklisten/tests/test_views.py                              29      0   100%
checklisten/urls.py                                           7      0   100%
checklisten/views.py                                         92     75    18%
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
mitglieder/apps.py                                            3      0   100%
mitglieder/forms.py                                          12      0   100%
mitglieder/funktions.py                                      13      7    46%
mitglieder/models.py                                         46      0   100%
mitglieder/templatetags/__init__.py                           0      0   100%
mitglieder/templatetags/mitglieder_extras.py                  7      3    57%
mitglieder/tests/__init__.py                                  0      0   100%
mitglieder/tests/test_apps.py                                 7      0   100%
mitglieder/tests/test_models.py                              17      0   100%
mitglieder/tests/test_urls.py                                50      0   100%
mitglieder/tests/test_views.py                               51      0   100%
mitglieder/urls.py                                            4      0   100%
mitglieder/views.py                                         249     70    72%
tests/MyFuncAemter.py                                        44      3    93%
tests/MyFuncLogin.py                                         33      8    76%
tests/MyFuncMitglieder.py                                   103     14    86%
tests/MyTestCase.py                                          31      4    87%
tests/__init__.py                                             0      0   100%
tests/test_001_admin.py                                       6      0   100%
tests/test_002_user.py                                        6      0   100%
tests/test_003_multiuser.py                                   1      0   100%
tests/test_004_mitgliedHinzufuegen.py                        38      4    89%
tests/test_005_mitgliedEntfernen.py                          13      0   100%
tests/test_006_mitgliedAendern.py                            13      0   100%
tests/test_007_aemtHinzufuegen.py                            63      0   100%
tests/test_008_aemtEntfernen.py                              47      0   100%
tests/test_009_aemtAendern.py                                92      0   100%
-----------------------------------------------------------------------------
TOTAL                                                      1752    336    81%
```
