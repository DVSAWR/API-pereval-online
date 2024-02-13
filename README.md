# Pereval.online API

### Описание проекта
API приложение для Федерации Спортивного Туризма России (ФСТР) с помощью Django Rest Framework.


В ходе создания проекта применялись различные инстументы и технологии.

django_orm, django_rest_framework, django_filter, swagger



| **URLs**                             | **Description**                         |
|--------------------------------------|-----------------------------------------|
| 	POST /submitData                    | 	Добавление записи                      |
| 	PATCH /submitData/{id}/             | 	Редактирование записи                  |
| 	GET /submitData/{id}/               | 	Извлечение данных о записи             |
| 	GET /submitData/user__email={email} | 	Извлечение списка записей по user.mail |





