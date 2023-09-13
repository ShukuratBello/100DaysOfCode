# Managing Multiple Projects, Virtual Environments and Environmental Variables.

# This was practiced on my hp laptop terminal.

# mkdir my_project
# cd my_project/
# conda create --name my_project_env flask sqlalchemy numpy pandas
# activate my_project_env
# pip list - see all packages in the environment
# environmnet.yaml   yml ~ file that captures everything in th environment

# To export ~ so that if a person want to install the same project on another PC, the can recreate the environment.


# conda env export > environment.yaml
# cat environment.yaml

# How to set environmental Variables
# conda env list - to see env location, then change dir

# Create 2 directory tree
# -p means the directory does not have to exist yet
# mkdir -p etc/conda/activate.d
# mkdir -p etc/conda/deactivate.d
# touch etc/conda/activate.d/env_vars.sh
# touch etc/conda/deactivate.d/env_vars.sh

# subl . ~ to open sublime script

# in activate, create a fake database script
# #!/bin/sh
# export DATABASE_URI="postgresql://user:pass@db_server:5432/test_db"

# in deactivate
# #!/bin/sh
# unset DATABASE_URI

# back to terminal; Activate and Deactivate
# echo $DATABASE_URI

# Dependencies and Env Variables.
# 

# Conda_auto_env()

# This video was hard for me to understand, I'll come back for it.