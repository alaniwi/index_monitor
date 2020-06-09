thisdir=$(dirname $BASH_SOURCE)
local_script=$thisdir/setup_env_local.sh
if [ -e $local_script ]
then
    . $local_script
fi


export DJANGO_SETTINGS_MODULE=index_monitor.settings

if [ -z "$PYTHONPATH" ]
then
    export PYTHONPATH=.
else
    export PYTHONPATH=.:$PYTHONPATH
fi
