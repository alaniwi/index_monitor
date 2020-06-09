export DJANGO_SETTINGS_MODULE=index_monitor.settings

if [ -z "$PYTHONPATH" ]
then
    export PYTHONPATH=.
else
    export PYTHONPATH=.:$PYTHONPATH
fi
