# Getting disks storage connected to Biomega
15 8 * * 1 ~/scripts/job1.sh >> ~/output/df_h_output.txt

# Getting history used in servers
0 5 * * 1,3,5 ~/scripts/job2.sh

# Checking merging of crontab & dirtree over Documents/tareas in Ubuntu Desktop
15 8 * * 1 ~/scripts/job5_running_dirtree.sh 2> ~/dirtree_output/error.log

