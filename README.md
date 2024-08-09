#  Summary

Moodle backup & restore in batch
Useful to move hundreds of courses from one Moodle instance to another

###  Notes
It assumes the second instance is empty and has:

 - same categories' structure (Use Moosh for that)
 - same **course custom fields created upfront**

### Instructions
#### Batch backup
**Change paths directly as needed**
You need a csv file for each category containing courses **Id** and **shortname**. Moosh can help you with that:
`moosh -n course-list -c 1 -f id,shortname -o csv > /var/www/moodledata/backupsdev/category1.csv`

Takes the category Id you wish to backup as an argument. It will then look for category1.csv
`python3 batch_backup.py 1`

#### Batch restore
**Change paths as needed** and run the script.
Assuming it's the same categories' structure, it will restore all mbz files to the same category

###  TODO
Batch backup all categories at once