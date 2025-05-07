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