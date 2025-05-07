# aiguesManresa
Prova per a Aigues Manresa


## 1. Clone this repository
```
git clone https://github.com/x14119641/aiguesManresa.git
```

## 2. Install python 3.11
```
pipenv --python $(which python3.11)
pepenv shell
```

## 3. Clone odoo repository (I am using version 17)
```
git clone https://github.com/odoo/odoo.git -b 17.0 --depth=1
```

## 4. Install dependencies
```
pip install python-ldap 
# Remove python-ldap from odoo/requirementesand
pip install -r odoo/requirements.txt
```


## 5. Test appplication
```
# Test odoo
./odoo/odoo-bin -c odoo.conf -d postgres --dev=all
# Initialize db (need to do this at the beggining!)
./odoo/odoo-bin -c odoo.conf -d postgres -i base
# To register
./odoo/odoo-bin -c odoo.conf -d postgres -i manresa_demo --dev=all
```



Achiviment: Show counter

Then visit http://localhost:8069/
Then visit http://localhost:8069/mqtt/dashboard