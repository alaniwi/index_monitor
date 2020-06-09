# wrapper for the entry points

# changes to app directory, sources the setup and runs the relevant 
# script (with the same name as the shell script but ending .py), 
# with the specified arguments

# this can be symlinked (or copied) to create shell scripts entry points 
# as required

script_dir=`dirname $0`
sh_script_name=`basename $0`
py_script_name=`echo $sh_script_name | sed 's/.sh$/.py/'`

if [ "$script_dir" = "." ]
then
    base_dir=..
else
    base_dir=`dirname $script_dir`
fi

cd $base_dir || exit 1

. ./setup_env.sh

exec scripts/$py_script_name "$@"
