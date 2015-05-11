generate-dev:
	python manage.py fasts3collectstatic --noinput --settings=botify_website.settings.dev
	python manage.py staticsitegen --settings=botify_website.settings.dev


generate-static-dev:
	python manage.py staticsitegen --settings=botify_website.settings.dev


generate-prod:
	python manage.py fasts3collectstatic --noinput --settings=botify_website.settings.prod
	python manage.py staticsitegen --settings=botify_website.settings.prod


generate-prod-html:
	python manage.py staticsitegen --settings=botify_website.settings.prod
