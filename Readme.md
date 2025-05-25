# Рекомендательная система направлений подготовки

## API Docs:

> POST /api/v1/recommendations/?top_n={количество рекомендаций}

<b>Тело запроса</b></br>
```json
{
  "gender": "male",
  "gpa": 3,
  "points": 310,
  "exams": [
    {
      "subject": "Русский язык",
      "points": 100
    }
  ]
}
```
### Требования к полям:
 * <b>gender</b>: Literal["male", "female"] </br>
 * <b>gpa</b>: >= 3 and <= 5 </br>
 * <b>points</b>: >= 0 anf <= 310


> GET /api/v1/directions/{direction_id}

<b>Тело запроса</b></br>
```json
{
  "direction_id": 0,
  "name": "string",
  "education_form": "ОФО",
  "description": "string",
  "entrance_exams": [
    {
      "name": "string",
      "priority": 0,
      "min_points": 0
    }
  ],
  "passing_points": [
    {
      "year": 0,
      "points": 0
    }
  ]
}
```
