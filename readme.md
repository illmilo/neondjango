<img src="neondjango/static/img/django_icon.png" width=35px align=right>

# NeonDjango

## Demo
https://neondjango.vercel.app

## Description

This is a template repository for your Django project to deploy it on Vercel with Neon DataBase integration.

## Requirements

- Vercel-CLI
- Django

## Usage

<iframe width="560" height="315" src="https://www.youtube.com/embed/qHZnufFz3Is?si=EE7t2drLQ2QkIORO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

1. Use this repository as a template to create your new GitHub repository
2. Clone this repository with `git clone https://github.com/illmilo/neondjango.git`
3. Copy & paste files `vercel.json`, `build.sh`, `.gitignore`, `requirements.txt` (if you have one, copy & paste content of the file to your existing file)
4. Activate `venv`
5. `pip install -r requirements.txt`
6. Open `settings.py` of both projects
7. Copy & paste variables `ALLOWED_HOSTS`, `DEBUG`, `DATABASES`, `STATIC_URL`, `STATICFILES_DIRS`, `STATIC_ROOT`
8. Copy & paste imports
9. Replace `neondjango` with your project name in `STATICFILES_DIRS` variable
10. Place **all the static files** inside `$rootApplicationFolder$/static`
11. In `wsgi.py`, put `app = application` in the end of the file
12. In `vercel.json`, replace `neondjango` with the name of your project
13. `python manage.py migrate`
14. `python manage.py createsuperuser` (if needed)
15. `vercel`

If everything's fine in preview, you can deploy it to production via `git push` or `vercel --prod`.

> Preview logs might indicate the absence of `requirements.txt`, ignore it. You should only care about `Inspect` page `Logs` & output of `Preview` page

> MAKE SURE THAT `.env` IS ADDED TO YOUR `.gitignore` FILE!

## License
This project is licensed under MIT License. Feel free to use this template. See [LICENSE](license) to learn more.
