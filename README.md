The archive script is a windows python script that allow when you select a projet file, a scene maya location and a folder destination to recreate the hierarchy, duplicate necessaries files and repath all path in files to make the selected scene work in another location.

for exemple:

in the project, D:\TRAJECTOIRE,
select scene path, D:\TRAJECTOIRE\05_shot\seq_0030\seq_0030_sh0010\maya\scenes\anim\TRJ_sq0030_sh0010_anim_0001.ma
and the new location, C:\

the script will list the files used by the maya scene, and if maya scenes references is path in the initial scene, it'll list the files used by refences scenes too until there is no more references increments.
It'll recreate the folder hierarchy for the necessaries scenes and files, duplicates the files and repath in all the maya scenes with the news directory path.

In the Script_Archivage_Clean.py, I clean the script and it'll work like describe above.
In the Script_Archivage_WIP.py, this is the script in which I tried to implement the same operation for a sequence or an entire project. But that's too much data, so I don't know if it's worth to do it, and if I am able to optimize it to make it viable.
